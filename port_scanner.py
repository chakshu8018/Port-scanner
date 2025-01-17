import socket

def port_scan(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()

target = input("Enter target IP address: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

port_scan(target, start_port, end_port)

