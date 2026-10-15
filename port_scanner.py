
import socket
from pyfiglet import figlet_format
import sys
from datetime import datetime
import queue
import threading
import time

THREAD_COUNT = 100
TIMEOUT = 0.5
PORT_RANGE = range(1, 65536)

port_queue = queue.Queue()
print_lock = threading.Lock()

art_banner = figlet_format("Simple port scanner")
print(art_banner)

if len(sys.argv) != 2:
    print("Usage: python3 scanner.py <target>")
    sys.exit(1)

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Hostname could not be resolved!")
    sys.exit(1)

print("-" * 50)
print(f"Scanning target: {target}")
print(f"Scan started at: {datetime.now()}")
print("-" * 50)

start_time = time.time()


def scan_port(port):
    try:
        with socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        ) as scan_socket:
            scan_socket.settimeout(TIMEOUT)
            result = scan_socket.connect_ex((target, port))

            if result == 0:
                with print_lock:
                    print(f"[+] Port {port} is OPEN")

    except OSError:
        pass


def worker():
    while True:
        port = port_queue.get()

        try:
            if port is None:
                return

            scan_port(port)

        finally:
            port_queue.task_done()


try:
    for port in PORT_RANGE:
        port_queue.put(port)

    threads = []

    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=worker, daemon=True)
        thread.start()
        threads.append(thread)

    port_queue.join()

    for _ in threads:
        port_queue.put(None)

    port_queue.join()

    for thread in threads:
        thread.join()

except KeyboardInterrupt:
    print("\nScan interrupted by user.")
    sys.exit(0)

print("-" * 50)
print(f"Scan completed at: {datetime.now()}")
print(f"Time taken: {time.time() - start_time:.2f} seconds")
print("-" * 50)
