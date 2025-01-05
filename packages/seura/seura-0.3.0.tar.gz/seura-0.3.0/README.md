# Seura Python Client

A Python client for controlling Séura Shade Series 1 outdoor TVs.
Commands come from [Séura IP Control documents](https://storage.googleapis.com/wp-stateless/2019/10/ip-control-for-shd1-outdoor-displays.pdf).

## Installation

You can install the package using pip:

```bash
pip install .
```

## Usage

Here's a basic example of how to use the Seura Python Client:

```python
from seura import SeuraClient

# Initialize the client with IP address
client = SeuraClient(address='192.168.1.100')

# Or initialize with hostname
client = SeuraClient(address='my.tv.local')

# Turn on the TV
client.power_on()

# Set the volume to 20
client.set_volume(20)

# Turn off the TV
client.power_off()
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Discussion and Support

For any questions, discussions, or support, please open an issue on our [GitHub Issues page](https://github.com/mickeyschwab/seura/issues).

