# Simple Python Port Scanner

A lightweight TCP port scanner built with Python for learning
network programming, socket connections, and multithreading.

## Features

- TCP port scanning
- Multithreaded scanning with worker threads
- Configurable socket timeout
- Hostname-to-IPv4 resolution
- Open port detection
- Scan start and completion timestamps
- Scan duration reporting
- Command-line target input
- Graceful handling of invalid hostnames and interruptions

## Requirements

- Python 3.10 or newer
- pyfiglet

The `socket`, `threading`, `queue`, `datetime`, `sys`, and `time`
modules are included in Python's standard library.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/simple-port-scanner.git
cd simple-port-scanner
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Scan your own machine:

```bash
python port_scanner.py 127.0.0.1
```

Scan an authorized lab target:

```bash
python port_scanner.py <TARGET_IP_OR_HOSTNAME>
```

Replace the placeholder with an IP address or hostname you are
authorized to test.

## How It Works

The scanner places ports into a queue. A pool of worker threads
takes ports from that queue and attempts TCP connections.
A successful connection indicates that the port accepted the
TCP connection at the time of the scan.

The scan timeout limits how long an individual connection attempt
waits. Results may vary depending on network conditions and
firewall rules.

## Limitations

- Scans TCP ports only.
- Does not identify service versions.
- Does not perform UDP scanning.
- A closed or filtered port may both appear as not open.
- Scanning all ports may take time, depending on the target and
  network conditions.

## Responsible Use

Use this tool only against systems you own or have explicit
permission to test. Follow applicable laws, lab rules, and
network policies.

## Future Improvements

- Custom port ranges
- Configurable thread count and timeout
- Service detection and banner grabbing
- CSV and JSON report export
- Progress indicator
- IPv6 support

## License

This project is available under the MIT License. See `LICENSE`
for details.
