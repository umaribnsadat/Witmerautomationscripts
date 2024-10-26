import socket

def find_free_ports(start_port, end_port, num_ports=1):
    free_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                free_ports.append(port)
                if len(free_ports) == num_ports:
                    break
            except OSError:
                pass
    return free_ports

start_port = 1024  # Start of the port range
end_port = 65535   # End of the port range
num_ports = 5      # Number of free ports to find

free_ports = find_free_ports(start_port, end_port, num_ports)
print("Free ports:", free_ports)
