import socket
import threading
import sys
from queue import Queue
import ipaddress
from datetime import datetime

def validate_ip(ip):
    """Validate the IP address format."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def validate_port(port):
    """Validate port number."""
    try:
        port = int(port)
        return 1 <= port <= 65535
    except ValueError:
        return False

def scan_port(ip, port, open_ports):
    """Scan a single port and store if open."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    except socket.error:
        pass

def worker(ip, port_queue, open_ports):
    """Worker thread to process ports from queue."""
    while not port_queue.empty():
        port = port_queue.get()
        scan_port(ip, port, open_ports)
        port_queue.task_done()

def port_scanner(ip, start_port, end_port, num_threads=100):
    """Main port scanning function."""
    print(f"\nStarting NexlifyPortProbe scan on {ip} from port {start_port} to {end_port}")
    print(f"Scan started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    port_queue = Queue()
    open_ports = []
    
    # Populate queue with ports
    for port in range(start_port, end_port + 1):
        port_queue.put(port)
    
    # Create and start threads
    threads = []
    for _ in range(min(num_threads, end_port - start_port + 1)):
        thread = threading.Thread(target=worker, args=(ip, port_queue, open_ports))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Sort and display results
    open_ports.sort()
    if open_ports:
        print("Open ports discovered:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports discovered.")
    
    print(f"\nScan completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return open_ports

def main():
    """Main function to handle user input and run scanner."""
    print("=== NexlifyPortProbe ===")
    
    # Get IP address
    while True:
        ip = input("Enter target IP address: ").strip()
        if validate_ip(ip):
            break
        print("Invalid IP address. Please try again.")
    
    # Get port range
    while True:
        try:
            start_port = input("Enter start port (1-65535): ").strip()
            if validate_port(start_port):
                start_port = int(start_port)
                break
            print("Invalid port number. Please enter a number between 1 and 65535.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            end_port = input("Enter end port (1-65535): ").strip()
            if validate_port(end_port):
                end_port = int(end_port)
                if end_port >= start_port:
                    break
                print("End port must be greater than or equal to start port.")
            else:
                print("Invalid port number. Please enter a number between 1 and 65535.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Run the scanner
    try:
        port_scanner(ip,47 start_port, end_port)
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()