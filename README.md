🕵️‍♂️ Network Device Scanner (Python)

A simple Python-based network scanner that detects all devices connected to your local network using ARP requests. Built for **ethical hacking practice**, network monitoring, and educational purposes.

---

## 📌 Features

- Scans a local IP range (e.g., `192.168.0.1/24`)
- Detects:
  - IP Address
  - MAC Address
- Fast and lightweight using `scapy`

---

## 📷 Demo

Enter IP range (e.g. 192.168.1.1/24): 192.168.0.1/24
IP MAC
192.168.0.1 20:cf:30:ab:12:34
192.168.0.5 34:23:87:cd:56:78

yaml
Copy
Edit

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.6+
- `scapy` library

### 💻 Installation

Clone the repo:

```bash
git clone https://github.com/your-username/network-device-scanner.git
cd network-device-scanner
Install dependencies:

bash
Copy
Edit
pip install scapy
🧪 Usage
🪟 On Windows (PowerShell):
powershell
Copy
Edit
python network_scanner.py
🐧 On Linux/Mac:
bash
Copy
Edit
sudo python3 network_scanner.py
When prompted, enter your local IP range:

Copy
Edit
192.168.1.1/24
You can find this using:

Windows: ipconfig

Linux/Mac: ifconfig or ip a

⚠️ Disclaimer
This tool is intended only for educational and ethical use. Do not use it on networks you don't own or have permission to analyze.

📁 File Structure
Copy
Edit
network-device-scanner/
├── network_scanner.py
└── README.md
🧠 Future Features (Optional Ideas)
Export results to CSV

GUI version using Tkinter

MAC vendor lookup

Real-time scanning with refresh
