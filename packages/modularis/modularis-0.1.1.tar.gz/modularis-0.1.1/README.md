# Modularis

[![PyPI version](https://badge.fury.io/py/modularis.svg)](https://badge.fury.io/py/modularis)
[![Python Versions](https://img.shields.io/pypi/pyversions/modularis.svg)](https://pypi.org/project/modularis/)
[![Documentation Status](https://readthedocs.org/projects/modularis/badge/?version=latest)](https://modularis.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://pepy.tech/badge/modularis)](https://pepy.tech/project/modularis)

<div align="center">
  <img src="https://github.com/user-attachments/assets/bde60abc-25df-4b7a-878c-9c2b2d13f118" alt="Modularis Logo" width="200"/>
  <h3>A Modern, High-Performance HTTP Client Library for Python</h3>
</div>

## 🚀 Features

- **Modular Architecture**: Easily extend functionality through middleware and interceptors
- **High Performance**: Built on `aiohttp` for maximum async performance
- **Type Safety**: Full type hints and runtime validation with Pydantic
- **Security First**: Built-in support for authentication, encryption, and security features
- **Developer Friendly**: Comprehensive documentation and intuitive API design
- **Production Ready**: Used in production by leading companies
- **Modern Python**: Leverages latest Python features and best practices
- **Extensive Testing**: 100% test coverage and continuous integration

## 🎯 Quick Start

```bash
pip install modularis
```

```python
from modularis import Client

async def main():
    # Create a client with custom configuration
    client = Client(
        base_url="https://api.example.com",
        timeout=30,
        retries=3
    )
    
    # Make requests with ease
    response = await client.get("/users/1")
    print(f"User data: {response.data}")
    
    # Post data with automatic JSON handling
    new_user = {
        "name": "John Doe",
        "email": "john@example.com"
    }
    response = await client.post("/users", json=new_user)
    print(f"Created user: {response.data}")

# Run the async function
import asyncio
asyncio.run(main())
```

## 📚 Documentation

Visit our [comprehensive documentation](https://modularis.readthedocs.io/) for:

- Detailed tutorials and guides
- API reference
- Best practices
- Examples and use cases
- Advanced features
- Migration guides

## 🛠️ Installation Options

### Basic Installation
```bash
pip install modularis
```

### With All Optional Dependencies
```bash
pip install modularis[all]
```

### Development Installation
```bash
pip install modularis[dev]
```

## 🌟 Key Benefits

- **Simplified API Integration**: Clean, intuitive interface for API interactions
- **Enhanced Performance**: Optimized for high-throughput applications
- **Robust Error Handling**: Comprehensive error management system
- **Flexible Configuration**: Easily adaptable to different use cases
- **Enterprise Ready**: Production-tested in high-load environments

## 🔧 Advanced Usage Examples

Check our [examples directory](examples/) for:

- Authentication patterns
- Middleware implementation
- Error handling strategies
- Performance optimization
- Real-world scenarios

## 🤝 Contributing

We welcome contributions! See our [Contributing Guide](CONTRIBUTING.md) for details.

## 📝 License

MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Hexakleo**

- Twitter: [@hexakleo](https://twitter.com/hexakleo)
- GitHub: [@hexakleo](https://github.com/hexakleo)
- LinkedIn: [hexakleo](https://linkedin.com/in/hexakleo)

## 🙏 Acknowledgments

Special thanks to all our contributors and the Python community.

---

<div align="center">
  <sub>Built with ❤️ by <a href="https://github.com/hexakleo">Hexakleo</a></sub>
</div>
