"""
Error Handler Module
Provides centralized error handling and recovery mechanisms
"""

import logging
import traceback
import functools
from typing import Callable, Any, Optional
from datetime import datetime


class ErrorHandler:
    """
    Centralized error handling with logging and recovery
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize error handler
        
        Args:
            logger: Logger instance (creates one if not provided)
        """
        self.logger = logger or logging.getLogger(__name__)
        self.error_count = {}
    
    def log_error(
        self,
        error: Exception,
        context: str = "",
        severity: str = "ERROR"
    ):
        """
        Log an error with context
        
        Args:
            error: Exception object
            context: Additional context information
            severity: Log severity level
        """
        error_msg = f"{context}: {str(error)}" if context else str(error)
        
        if severity == "CRITICAL":
            self.logger.critical(error_msg, exc_info=True)
        else:
            self.logger.error(error_msg, exc_info=True)
        
        # Track error frequency
        error_type = type(error).__name__
        self.error_count[error_type] = self.error_count.get(error_type, 0) + 1
    
    def get_error_summary(self) -> dict:
        """
        Get summary of errors encountered
        
        Returns:
            Dictionary with error statistics
        """
        return {
            'total_errors': sum(self.error_count.values()),
            'error_types': dict(self.error_count),
            'timestamp': datetime.now().isoformat()
        }
    
    def reset_error_count(self):
        """Reset error counters"""
        self.error_count.clear()


def async_error_handler(
    default_return: Any = None,
    log_traceback: bool = True,
    reraise: bool = False
):
    """
    Decorator for async function error handling
    
    Args:
        default_return: Value to return on error
        log_traceback: Whether to log full traceback
        reraise: Whether to re-raise the exception
    
    Returns:
        Decorated function
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__module__)
            
            try:
                return await func(*args, **kwargs)
            
            except Exception as e:
                error_msg = f"Error in {func.__name__}: {str(e)}"
                
                if log_traceback:
                    logger.error(error_msg, exc_info=True)
                else:
                    logger.error(error_msg)
                
                if reraise:
                    raise
                
                return default_return
        
        return wrapper
    return decorator


def sync_error_handler(
    default_return: Any = None,
    log_traceback: bool = True,
    reraise: bool = False
):
    """
    Decorator for synchronous function error handling
    
    Args:
        default_return: Value to return on error
        log_traceback: Whether to log full traceback
        reraise: Whether to re-raise the exception
    
    Returns:
        Decorated function
    """
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__module__)
            
            try:
                return func(*args, **kwargs)
            
            except Exception as e:
                error_msg = f"Error in {func.__name__}: {str(e)}"
                
                if log_traceback:
                    logger.error(error_msg, exc_info=True)
                else:
                    logger.error(error_msg)
                
                if reraise:
                    raise
                
                return default_return
        
        return wrapper
    return decorator


class RetryHandler:
    """
    Handles retry logic with exponential backoff
    """
    
    @staticmethod
    async def async_retry(
        func: Callable,
        max_attempts: int = 3,
        backoff_factor: float = 2.0,
        exceptions: tuple = (Exception,),
        *args,
        **kwargs
    ) -> Any:
        """
        Retry an async function with exponential backoff
        
        Args:
            func: Async function to retry
            max_attempts: Maximum retry attempts
            backoff_factor: Backoff multiplier
            exceptions: Tuple of exceptions to catch
            *args: Function arguments
            **kwargs: Function keyword arguments
        
        Returns:
            Function result
        
        Raises:
            Last exception if all retries fail
        """
        import asyncio
        
        logger = logging.getLogger(__name__)
        last_exception = None
        
        for attempt in range(max_attempts):
            try:
                return await func(*args, **kwargs)
            
            except exceptions as e:
                last_exception = e
                
                if attempt < max_attempts - 1:
                    wait_time = backoff_factor ** attempt
                    logger.warning(
                        f"Attempt {attempt + 1} failed: {str(e)}. "
                        f"Retrying in {wait_time}s..."
                    )
                    await asyncio.sleep(wait_time)
                else:
                    logger.error(
                        f"All {max_attempts} attempts failed for {func.__name__}"
                    )
        
        raise last_exception


def format_exception(exception: Exception) -> dict:
    """
    Format exception into a structured dictionary
    
    Args:
        exception: Exception object
    
    Returns:
        Dictionary with exception details
    """
    return {
        'type': type(exception).__name__,
        'message': str(exception),
        'traceback': traceback.format_exc(),
        'timestamp': datetime.now().isoformat()
    }
