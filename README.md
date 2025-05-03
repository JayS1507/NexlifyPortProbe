NexlifyPortProbe

NexlifyPortProbe is a uniquely crafted Python-based port scanner designed to uncover open ports on a target IP address with precision and speed. Built for educational purposes, this tool empowers users to explore network programming and cybersecurity concepts through an innovative and robust interface.

Features





Robust input validation for IP addresses and port numbers.



Scans a customizable port range (1 to 65535) with high efficiency.



Leverages multi-threading for rapid port scanning.



Provides detailed scan reports, including start/end times and open ports.



Gracefully handles errors, such as invalid inputs or network disruptions.



User-friendly command-line interface for seamless operation.

Prerequisites





Python 3.x: Install Python from python.org if not already installed.



No external dependencies required; uses standard Python libraries (socket, threading, queue, ipaddress, sys, datetime).

Installation





Clone the repository to your local machine:

git clone https://github.com/yourusername/NexlifyPortProbe.git



Navigate to the project directory:

cd NexlifyPortProbe

Usage





Execute the script with Python:

python nexlify_port_probe.py



Enter the requested details:





Target IP address (e.g., 192.168.1.1 or a public IP like 8.8.8.8).



Start port (1–65535).



End port (must be greater than or equal to the start port).



NexlifyPortProbe will scan the specified ports and report any open ports, along with scan timestamps.

Example

=== NexlifyPortProbe ===
Enter target IP address: 127.0.0.1
Enter start port (1-65535): 80
Enter end port (1-65535): 85

Starting NexlifyPortProbe scan on 127.0.0.1 from port 80 to 85
Scan started at: 2025-05-04 12:30:45

Open ports discovered:
Port 80 is open

Scan completed at: 2025-05-04 12:30:47

Notes





Ethical Use: Only scan networks and IP addresses you are authorized to probe. Unauthorized scanning may violate laws or network policies.



Performance: The script defaults to 100 threads for efficient scanning. Modify the num_threads parameter in the port_scanner function if needed.



Limitations: As a basic scanner, it may not detect ports in complex network environments (e.g., behind advanced firewalls).

Contributing

We welcome contributions to enhance NexlifyPortProbe! To contribute:





Fork the repository.



Create a feature branch (git checkout -b feature-branch).



Commit your changes (git commit -m "Add feature").



Push to the branch (git push origin feature-branch).



Submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Disclaimer

NexlifyPortProbe is intended for educational use only. The author is not liable for any misuse or damages resulting from this tool.
