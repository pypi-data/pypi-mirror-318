# Caddy API Client

A Python client for managing Caddy server configurations through its API.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/migetapp/caddy-api-client.git
cd caddy-api-client
```

2. Install the package in development mode:
```bash
pip install -e .
```

## Usage

```python
from caddy_api_client import CaddyAPIClient

# Initialize the client
client = CaddyAPIClient("http://localhost:2019")  # Default Caddy admin endpoint

# Add a domain with automatic TLS (Let's Encrypt)
client.add_domain_with_auto_tls(
    domain="example.org",
    target="nginx",
    target_port=80
)

# Add a domain with TLS certificates using PEM data
with open('cert.pem', 'r') as f:
    certificate = f.read()
with open('key.pem', 'r') as f:
    private_key = f.read()

client.add_domain_with_tls(
    domain="example.net",
    target="192.168.10.101",
    target_port=80,
    certificate=certificate,
    private_key=private_key
)

# Get domain configuration
config = client.get_domain_config("example.com")
print(config)

# Update domain configuration
client.update_domain(
    domain="example.com",
    target="172.16.0.2",
    target_port=8080
)

# Delete domain
client.delete_domain("example.com")
```

## Features

- Add domains with TLS certificates using PEM data
- Add domains with automatic TLS (Let's Encrypt/ZeroSSL)
- Delete domain configurations
- Get domain configurations
- Update domain configurations

## Error Handling

The client includes basic error handling for API requests. All methods will raise exceptions with descriptive messages if something goes wrong during the API calls.

## License

This project is licensed under the Apache License, Version 2.0 - see the [LICENSE](LICENSE) file for details.

Copyright 2025 Krzysztof Taraszka and The Miget Authors.
