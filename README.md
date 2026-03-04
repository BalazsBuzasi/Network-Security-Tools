# 🛡️ Cybersecurity & Network Analysis Arsenal

A collection of professional-grade Python tools designed for network reconnaissance, deep packet analysis, and security auditing. These scripts are engineered using Python's standard library to ensure high performance, zero external dependencies, and maximum portability across Linux (Kali) and Windows environments.

---

## 🕵️ 1. Raw Socket Sniffer & Packet Analyzer (`pro_sniffer.py`)

A deep-dive network monitoring tool that interacts directly with the OS network stack. This script demonstrates the ability to bypass high-level abstractions and handle raw binary data from the wire.

### Key Technical Features
* **Byte-Level Header Unpacking:** Uses the `struct` module to manually dissect the 20-byte IPv4 header with surgical precision.
* **Protocol Identification:** Real-time decoding of IANA protocol numbers to identify ICMP, TCP, and UDP traffic.
* **Network Layer Forensics:** Extracts raw Source and Destination IP addresses directly from the IP header.
* **CLI Integration:** Fully automated via `argparse` for professional terminal-based workflows.

### Usage
*Note: Requires root/administrator privileges to bind to raw sockets.*
```bash
sudo python3 pro_sniffer.py --interface <YOUR_IP_ADDRESS>
