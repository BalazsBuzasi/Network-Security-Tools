# 🛡️ Python Security & Networking Toolkit

A collection of custom Python-based networking and security tools. This repository serves as a practical demonstration of core cybersecurity concepts, including packet manipulation, low-level socket programming, and multi-threaded network reconnaissance. 

Developed with a focus on offensive security principles and network diagnostics.

---

## 🛠️ The Arsenal (Included Tools)

### 1. 📡 Pro Network Sniffer (`pro_sniffer.py`)
A foundational network diagnostic tool built to capture and analyze raw network traffic in real-time.
* **Core Concept:** Deep packet inspection and network traffic analysis.
* **Features:** Captures passing packets on the interface, extracts readable payloads, and identifies source/destination addresses. Crucial for understanding how data moves across the wire.

### 2. 🔌 Pro Raw TCP Client (`pro_tcp_client.py`)
A lightweight, versatile script for establishing direct TCP connections to target servers.
* **Core Concept:** Socket programming and the TCP 3-way handshake.
* **Features:** Capable of initiating connections, sending raw encoded data, and receiving server responses (Banner Grabbing). Excellent for testing firewall rules and service availability.

### 3. ⚡ Pro Multithreaded Port Scanner (`pro_port_scanner.py`)
A high-speed, concurrent port scanner designed to rapidly identify open network ports and potential entry points on target systems.
* **Core Concept:** Network Reconnaissance & Multithreading.
* **Features:** * Utilizes Python's `concurrent.futures.ThreadPoolExecutor` to scan hundreds of ports simultaneously, drastically reducing scan times.
  * Custom socket timeout handling for precise connection attempts.
  * Advanced CLI argument parsing (`argparse`) to dynamically define target IPs, port ranges, and thread counts.

---

## 🚀 Quick Start / Usage

Clone the repository to your local machine:
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
