import socket
# from constants import HOST, PORT  # Ensure these are defined elsewhere



HOST = "0.0.0.0"
PORT = 6379

def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server((HOST, PORT))

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        with conn:
            buffer = b""

            while True:
                chunk = conn.recv(1024)
                if not chunk:
                    break  # Client disconnected
                buffer += chunk

                # Look for full lines terminated by \n or \r
                while b'\n' in buffer or b'\r' in buffer:
                    # Use whichever comes first
                    split_char = b'\r' if b'\r' in buffer else b'\n'
                    line, buffer = buffer.split(split_char, 1)
                    message = line.strip().decode()
                    
                    print("Received:", message)

                    # Handle PING case-insensitively
                    if message.lower() == "ping":
                        conn.sendall(b"PONG\n")
                    # else:
                    #     conn.sendall(line + b'\n')


if __name__ == "__main__":
    main()
