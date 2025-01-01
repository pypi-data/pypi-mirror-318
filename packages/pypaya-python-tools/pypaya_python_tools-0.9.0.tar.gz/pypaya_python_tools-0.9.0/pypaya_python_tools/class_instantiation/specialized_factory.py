from typing import Dict, Any, TypeVar, Generic, Optional, Type, List, Callable, Union
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from pypaya_python_tools.class_instantiation.class_instance_factory import ClassInstanceFactory


T = TypeVar('T')


class FactoryValidationError(Exception):
    """Raised when factory validation fails."""
    pass


class FactoryCreationError(Exception):
    """Raised when object creation fails."""
    pass


@dataclass
class FactoryConfig:
    """Configuration for factory instance creation."""
    class_name: str
    args: List[Any] = None
    kwargs: Dict[str, Any] = None
    module: Optional[str] = None
    base_path: Optional[str] = None
    file: Optional[str] = None


class SpecializedFactory(ABC, Generic[T]):
    """Base factory for creating specialized types of objects.

    Primary purpose:
    - Provides convenient mappings for predefined framework classes to their module paths
    - Allows custom implementations through explicit module/file specifications

    Features:
    - Built-in type mappings for framework classes
    - Support for custom implementations via module path or file path
    - Special case handling
    - Type validation
    - Flexible configuration formats
    """

    def __init__(
            self,
            base_class: Optional[Type[T]] = None,
            allow_custom: bool = True,
            class_instance_factory: Optional[ClassInstanceFactory] = None,
            base_path: Optional[Union[str, Path]] = None
    ):
        """Initialize factory.

        Args:
            base_class: Base class that all created objects must inherit from
            allow_custom: Whether to allow custom implementations
            class_instance_factory: Optional custom ClassInstanceFactory instance
            base_path: Optional base path for module imports
        """
        self.base_class = base_class
        self.allow_custom = allow_custom
        self.base_path = base_path
        self.type_mapping: Dict[str, str] = {}
        self.special_handlers: Dict[str, Callable[[Dict[str, Any]], T]] = {}
        self.class_instance_factory = class_instance_factory or ClassInstanceFactory()

        self._initialize_type_mapping()
        self._initialize_special_handlers()
        self._validate_factory_setup()

    @abstractmethod
    def _initialize_type_mapping(self) -> None:
        """Initialize the mapping between type names and module paths."""
        pass

    def _initialize_special_handlers(self) -> None:
        """Initialize special case handlers. Override in subclasses if needed."""
        pass

    def _validate_factory_setup(self) -> None:
        """Validate factory configuration."""
        if not self.type_mapping:
            raise ValueError(
                f"Factory {self.__class__.__name__} must define at least one type mapping"
            )

    def register_type(self, name: str, module_path: str) -> None:
        """Register a new type mapping.

        Args:
            name: The exact class name
            module_path: Full module path to the class
        """
        if not isinstance(name, str) or not isinstance(module_path, str):
            raise ValueError("Both name and module_path must be strings")
        self.type_mapping[name] = module_path

    def unregister_type(self, name: str) -> None:
        """Remove a type mapping.

        Args:
            name: The exact class name to unregister
        """
        self.type_mapping.pop(name, None)

    def _normalize_config(self, config: Dict[str, Any]) -> FactoryConfig:
        """Normalize different config formats into standard format."""
        config = config.copy()

        if "class_name" not in config:
            raise FactoryValidationError(
                "Configuration must include 'class_name' field"
            )

        class_name = config.pop("class_name")

        # Handle explicit args/kwargs format
        if "args" in config or "kwargs" in config:
            return FactoryConfig(
                class_name=class_name,
                args=config.pop("args", []),
                kwargs=config.pop("kwargs", {}),
                module=config.pop("module", None),
                base_path=config.pop("base_path", None),
                file = config.pop("file", None)
            )

        # Handle flat format
        module = config.pop("module", None)
        base_path = config.pop("base_path", None)
        file = config.pop("file", None)

        return FactoryConfig(
            class_name=class_name,
            args=[],
            kwargs=config,
            module=module,
            base_path=base_path,
            file=file
        )

    def build(self, config: Dict[str, Any]) -> T:
        """Build an instance based on configuration.

        Args:
            config: Configuration dictionary for object creation.
                   Must include:
                   - 'class_name': Name of the class to instantiate
                   Optional fields:
                   - 'module': Module path for custom implementations
                   - 'file': File path for custom implementations
                   - 'base_path': Base path for import resolution
                   - 'args': List of positional arguments
                   - 'kwargs': Dictionary of keyword arguments

        Returns:
            Created instance

        Raises:
            FactoryValidationError: If configuration is invalid
            FactoryCreationError: If object creation fails
        """
        try:
            normalized_config = self._normalize_config(config)

            # Handle special cases first
            if normalized_config.class_name in self.special_handlers:
                return self._validate_instance(
                    self.special_handlers[normalized_config.class_name](
                        normalized_config.kwargs
                    )
                )

            # Handle custom implementations
            if normalized_config.module or "file" in config:
                if not self.allow_custom:
                    raise FactoryValidationError(
                        f"Custom implementations not allowed in {self.__class__.__name__}"
                    )
                return self._create_custom_implementation(normalized_config)

            # Handle built-in implementations
            return self._create_builtin_implementation(normalized_config)

        except Exception as e:
            if isinstance(e, (FactoryValidationError, FactoryCreationError)):
                raise
            raise FactoryCreationError(
                f"Failed to create instance: {str(e)}"
            ) from e

    def _create_custom_implementation(self, config: FactoryConfig) -> T:
        """Create instance from custom implementation."""
        factory_config = {
            "class": config.class_name,
            "args": config.args or [],
            "kwargs": config.kwargs or {}
        }

        # Handle file-based custom implementation
        if config.file:
            factory_config["file"] = config.file
        # Handle module-based custom implementation
        else:
            factory_config["module"] = config.module
            if config.base_path or self.base_path:
                factory_config["base_path"] = config.base_path or self.base_path

        instance = self.class_instance_factory.create(factory_config)
        return self._validate_instance(instance)

    def _create_builtin_implementation(self, config: FactoryConfig) -> T:
        """Create instance from built-in implementation."""
        if config.class_name not in self.type_mapping:
            available_types = list(self.type_mapping.keys())
            raise FactoryValidationError(
                f"Unknown class: {config.class_name}. "
                f"Available types: {available_types}"
            )

        instance = self.class_instance_factory.create({
            "module": self.type_mapping[config.class_name],
            "base_path": self.base_path,
            "class": config.class_name,
            "args": config.args,
            "kwargs": config.kwargs
        })
        return self._validate_instance(instance)

    def _validate_instance(self, instance: Any) -> T:
        """Validate created instance."""
        if self.base_class and not isinstance(instance, self.base_class):
            raise FactoryValidationError(
                f"Invalid type: expected {self.base_class.__name__}, "
                f"got {type(instance).__name__}"
            )
        return instance

    def build_many(self, configs: List[Dict[str, Any]]) -> List[T]:
        """Build multiple instances from configurations.

        Args:
            configs: List of configuration dictionaries

        Returns:
            List of created instances
        """
        return [self.build(config) for config in configs]
