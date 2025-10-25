"""
Test suite for HelloWorldAgent

Run tests with: pytest src/tests/test_hello_world.py -v
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src.agents.hello_world_agent import HelloWorldAgent


class TestHelloWorldAgent:
    """Test cases for HelloWorldAgent"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.agent = HelloWorldAgent()
    
    def test_hello_world_basic(self):
        """Test basic hello world functionality"""
        result = self.agent.execute("world")
        assert "Hello, world!" in result
        assert "Cursor AI test" in result
    
    def test_empty_input(self):
        """Test handling of empty input"""
        result = self.agent.execute("")
        assert "Error: No input provided" in result
    
    def test_custom_name(self):
        """Test with custom name input"""
        result = self.agent.execute("Alice")
        assert "Hello, Alice!" in result
    
    def test_validate_input_valid(self):
        """Test input validation with valid input"""
        assert self.agent.validate_input("test") is True
    
    def test_validate_input_empty(self):
        """Test input validation with empty string"""
        assert self.agent.validate_input("") is False
    
    def test_validate_input_type(self):
        """Test input validation with non-string type"""
        assert self.agent.validate_input("valid_string") is True
    
    def test_agent_name(self):
        """Test agent name initialization"""
        assert self.agent.name == "hello_world_test"
    
    def test_get_agent_info(self):
        """Test agent info retrieval"""
        info = self.agent.get_agent_info()
        assert "name" in info
        assert "version" in info
        assert "description" in info
        assert info["name"] == "hello_world_test"
    
    def test_long_input(self):
        """Test with longer input string"""
        long_name = "A" * 100
        result = self.agent.execute(long_name)
        assert f"Hello, {long_name}!" in result
    
    def test_special_characters(self):
        """Test with special characters in input"""
        result = self.agent.execute("User-123")
        assert "Hello, User-123!" in result


@pytest.fixture
def agent():
    """Pytest fixture for agent instance"""
    return HelloWorldAgent()


def test_with_fixture(agent):
    """Test using pytest fixture"""
    result = agent.execute("pytest")
    assert "Hello, pytest!" in result
