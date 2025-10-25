"""
Cursor AI Hello World Test Agent

A simple test agent demonstrating basic Cursor AI agent patterns.
"""

import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HelloWorldAgent:
    """
    A simple Hello World agent for testing Cursor AI framework integration.
    
    This agent demonstrates basic agent patterns including:
    - Input validation
    - Error handling
    - Response formatting
    """
    
    def __init__(self):
        """Initialize the HelloWorldAgent."""
        self.name = "hello_world_test"
        logger.info(f"Initialized {self.name} agent")
    
    def execute(self, input_text: str) -> str:
        """
        Standard hello world response mechanism.
        
        Args:
            input_text (str): Incoming test string
        
        Returns:
            str: Formatted hello world response
            
        Examples:
            >>> agent = HelloWorldAgent()
            >>> agent.execute("world")
            'Hello, world! This is a Cursor AI test.'
        """
        logger.info(f"Executing with input: {input_text}")
        
        # Validate input
        if not self.validate_input(input_text):
            error_msg = "Error: No input provided"
            logger.warning(error_msg)
            return error_msg
        
        # Generate response
        response = f"Hello, {input_text}! This is a Cursor AI test."
        logger.info(f"Generated response: {response}")
        
        return response

    def validate_input(self, input_text: str) -> bool:
        """
        Input validation method.
        
        Args:
            input_text (str): Input string to validate
            
        Returns:
            bool: True if input is valid, False otherwise
        """
        is_valid = isinstance(input_text, str) and len(input_text) > 0
        logger.debug(f"Input validation result: {is_valid}")
        return is_valid
    
    def get_agent_info(self) -> dict:
        """
        Get information about the agent.
        
        Returns:
            dict: Agent metadata
        """
        return {
            "name": self.name,
            "version": "1.0.0",
            "description": "Hello World Test Agent for Cursor AI"
        }
