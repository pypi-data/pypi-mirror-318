from typing import Any, Callable, Optional
from functools import wraps

class Middleware:
    _instances = {}

    def __init__(self):
        self.__pre: Optional[Callable[..., Any]] = None  # 'pre' is a function that accepts any type and returns any type
        self.__pos: Optional[Callable[[Any], Any]] = None  # 'post' takes a value and returns something (could be any type)
        self.__class__._instances[self.__class__] = self

    @property
    def pre(self) -> Optional[Callable[..., Any]]:
        return self.__pre

    @pre.setter
    def pre(self, value: Callable[..., Any]) -> None:
        # Validates that the value is callable (a function or method)
        if not callable(value):
            raise TypeError(f"Expected a callable function, got {type(value).__name__}.")
        self.__pre = value

    @property
    def post(self) -> Optional[Callable[[Any], Any]]:
        return self.__pos

    @post.setter
    def post(self, value: Callable[[Any], Any]) -> None:
        # Validates that the value is callable (a function or method)
        if not callable(value):
            raise TypeError(f"Expected a callable function, got {type(value).__name__}.")
        self.__pos = value

    @classmethod
    def get_instance(cls) -> "Middleware":
        # Retrieves the singleton instance of the Middleware class
        if cls not in cls._instances:
            raise ValueError(f"No active instance found for {cls.__name__}")
        return cls._instances[cls]

    @classmethod
    def middleware_in(cls, **decorator_kwargs: Any) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """Decorator function to apply middleware logic before the decorated function."""
        def outer_decorator(function: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(function)
            def wrapper(*args, **kwargs):
                instance = cls.get_instance()
                if not instance.pre:
                    raise ValueError(f"Middleware '{cls.__name__}' does not have a 'pre' function defined")
                # Call the pre function with additional decorator arguments
                pre_value = instance.pre(*args, **kwargs, **decorator_kwargs)
                return function(pre=pre_value, *args, **kwargs)
            return wrapper
        return outer_decorator

    @classmethod
    def middleware_out(cls, **decorator_kwargs: Any) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """Decorator function to apply middleware logic after the decorated function."""
        def outer_decorator(function: Callable[..., Any]) -> Callable[..., Any]:
            @wraps(function)
            def wrapper(*args, **kwargs):
                instance = cls.get_instance()
                if not (instance.pre and instance.post):
                    raise ValueError(f"Middleware '{cls.__name__}' does not have both 'pre' and 'post' functions defined")
                # Call the pre function with additional decorator arguments
                pre_value = instance.pre(*args, **kwargs, **decorator_kwargs)
                result = function(pre=pre_value, *args, **kwargs)
                # Call the post function with additional decorator arguments
                return instance.post(result, **decorator_kwargs)
            return wrapper
        return outer_decorator