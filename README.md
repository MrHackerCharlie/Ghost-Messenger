# 👻 Ghost Messenger: The P2P Onion Protocol

![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Security: AES--256--GCM](https://img.shields.io/badge/Security-AES--256--GCM-green.svg)
![Network: Tor--Project](https://img.shields.io/badge/Network-Tor--Project-purple.svg)

**Ghost Messenger** is a high-security, peer-to-peer (P2P) communication framework designed for total anonymity. By leveraging **AES-256-GCM** authenticated encryption and the **Tor (Onion Router)** network, Ghost Messenger ensures that both the content and the metadata of your communications remain invisible to ISPs, governments, and third-party attackers.

---

## 🚀 The Architecture

Unlike traditional messaging apps (Signal, Telegram, WhatsApp), Ghost Messenger has **zero central servers**. 

1. **Onion Services:** The receiver generates an ephemeral `.onion` address that exists only in RAM.
2. **Triple-Layer Routing:** Messages are bounced through three different global nodes before reaching the destination.
3. **Cryptographic Integrity:** Every packet is encrypted with AES-256-GCM, ensuring that if even a single bit is altered in transit, the packet is dropped.
4. **Zero-Trace:** No logs, no history, and no forensic trail.

---

## 🛠 Installation & Setup

### 1. Prerequisites
Ensure you are running **Kali Linux** or a similar Unix-based environment with the Tor service active.

```bash
# Install system-level dependencies
sudo apt update && sudo apt install tor -y

# Install Python dependencies
pip3 install cryptography stem PySocks
```

### 2. Tor Configuration
To allow the Python controller to interface with the Tor circuit, modify your torrc file:

```bash
sudo nano /etc/tor/torrc
Add or uncomment the following lines:
```

```Plaintext
ControlPort 9051
CookieAuthentication 1
CookieAuthFileGroupReadable 1
```

Restart the service and update permissions:

```bash
sudo service tor restart
sudo usermod -a -G debian-tor $USER
```

## 📖 Usage Guide
Ghost Messenger operates in a Receiver-First architecture.

### Step 1: Initialize the Ghost Receiver
On the receiving machine, run the listener. This will generate your unique, one-time-use .onion ghost address.

```bash
python3 receiver.py
```

Wait for the [!!!] GHOST ADDRESS to appear. Share this address with the sender over a secure channel.

### Step 2: Inject the Message
On the sending machine, run the sender and input the ghost address provided by the receiver.

```bash
python3 sender.py
```

## ⚠️ Legal Disclaimer
Ghost Messenger is an Ethical Hacking and Privacy Research tool. It is designed for educational purposes and to demonstrate secure communication protocols. Unauthorized use of this tool for malicious activities is strictly prohibited. The developer is not responsible for any misuse.


Developed for research purposes in the 2026 Cybersecurity Landscape.
