# 🛡️ Cybersecurity Lab: Network Defense Tools

This repository is a collection of Python-based security tools developed during my cybersecurity certification journey. Each tool is designed to demonstrate core networking principles and automated security auditing.

## 🚀 Pro TCP Client & Banner Grabber
`pro_tcp_client.py`

A professional-grade TCP client designed to establish connections with remote hosts and retrieve raw server responses. This is an essential tool for **Service Fingerprinting** and **Reconnaissance**.

### Key Features
- **Dynamic Argument Parsing:** Uses the `argparse` module to allow users to specify targets and ports directly from the terminal.
- **Service Identification:** Retrieves HTTP headers and server banners to identify running services and versions.
- **Robust Error Handling:** Managed exceptions for timeouts and connection failures.
- **Clean Code:** Adheres to Python's "Snake Case" naming conventions and best practices.

### 🛠️ Installation & Usage
No external libraries are required (uses built-in `socket` and `argparse` modules).

1. Clone or download the script.
2. Run it from your terminal:

```bash
python3 pro_tcp_client.py --target <TARGET_IP_OR_DOMAIN> --port <PORT_NUMBER>
