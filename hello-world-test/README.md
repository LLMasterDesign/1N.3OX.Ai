# Cursor AI "Hello World" Test Agent

A lightweight test agent demonstrating Cursor AI agent framework patterns and best practices.

## 🚀 Features

- Simple and extensible agent architecture
- Comprehensive input validation
- Built-in error handling
- Extensive test coverage
- Logging support
- CLI interface

## 📁 Project Structure

```
hello-world-test/
├── src/
│   ├── agents/
│   │   └── hello_world_agent.py    # Main agent implementation
│   ├── tests/
│   │   └── test_hello_world.py     # Test suite
│   └── main.py                     # CLI entry point
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🔧 Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup

1. Clone or navigate to the project directory:
```bash
cd hello-world-test
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎯 Usage

### Basic Usage

Run the agent with default settings:
```bash
python src/main.py
```

Output:
```
Hello, World! This is a Cursor AI test.
```

### Custom Name

Provide a custom name:
```bash
python src/main.py --name "Alice"
```

Output:
```
Hello, Alice! This is a Cursor AI test.
```

### Verbose Logging

Enable detailed logging:
```bash
python src/main.py --name "Bob" --verbose
```

### Agent Information

Display agent metadata:
```bash
python src/main.py --info
```

## 🧪 Testing

Run the test suite using pytest:

```bash
# Run all tests
pytest src/tests/test_hello_world.py -v

# Run with coverage report
pytest src/tests/test_hello_world.py --cov=src/agents --cov-report=html

# Run specific test
pytest src/tests/test_hello_world.py::TestHelloWorldAgent::test_hello_world_basic -v
```

### Test Coverage

The test suite includes:
- ✅ Basic functionality tests
- ✅ Input validation tests
- ✅ Error handling tests
- ✅ Edge case tests (empty input, long strings, special characters)
- ✅ Agent metadata tests

## 📚 API Reference

### HelloWorldAgent

#### `__init__()`
Initialize the agent.

#### `execute(input_text: str) -> str`
Process input and return formatted response.

**Parameters:**
- `input_text` (str): The name or text to greet

**Returns:**
- `str`: Formatted hello world message or error message

**Example:**
```python
from src.agents.hello_world_agent import HelloWorldAgent

agent = HelloWorldAgent()
result = agent.execute("World")
print(result)  # "Hello, World! This is a Cursor AI test."
```

#### `validate_input(input_text: str) -> bool`
Validate input string.

**Parameters:**
- `input_text` (str): Input to validate

**Returns:**
- `bool`: True if valid, False otherwise

#### `get_agent_info() -> dict`
Get agent metadata.

**Returns:**
- `dict`: Agent information including name, version, and description

## 🔍 Code Example

```python
from src.agents.hello_world_agent import HelloWorldAgent

# Initialize agent
agent = HelloWorldAgent()

# Execute with valid input
response = agent.execute("Cursor AI")
print(response)  # "Hello, Cursor AI! This is a Cursor AI test."

# Handle invalid input
response = agent.execute("")
print(response)  # "Error: No input provided"

# Get agent info
info = agent.get_agent_info()
print(info["name"])  # "hello_world_test"
```

## 🛠️ Development

### Code Style

Format code with Black:
```bash
black src/
```

Lint with flake8:
```bash
flake8 src/
```

Type check with mypy:
```bash
mypy src/
```

## 📝 Performance Considerations

- **Minimal overhead**: Lightweight design with fast string processing
- **Efficient validation**: Quick input checks
- **Low memory footprint**: No heavy dependencies

## 🔄 Extensibility

This agent serves as a template for building more complex agents. Extend by:

1. **Adding new methods** to the `HelloWorldAgent` class
2. **Implementing additional validation** rules
3. **Integrating with external APIs** or services
4. **Creating new agent classes** using similar patterns

## 📊 Error Handling

The agent handles various error scenarios:

| Scenario | Response |
|----------|----------|
| Empty input | "Error: No input provided" |
| Valid input | "Hello, {input}! This is a Cursor AI test." |

## 🤝 Contributing

To contribute:
1. Add new features to the agent
2. Write comprehensive tests
3. Update documentation
4. Follow Python best practices

## 📄 License

This is a test agent for demonstration purposes.

## 🎓 Recommended Next Steps

- [ ] Implement advanced logging with log rotation
- [ ] Add configuration file support (YAML/JSON)
- [ ] Create integration tests
- [ ] Add async/await support for scalability
- [ ] Implement agent chaining capabilities
- [ ] Add metrics and monitoring
- [ ] Create Docker containerization
- [ ] Build web API wrapper (FastAPI/Flask)

## 📞 Support

For issues or questions, please refer to the Cursor AI documentation.

---

**Version:** 1.0.0  
**Last Updated:** 2025-10-25  
**Framework:** Cursor AI Agent System
