import socket

HOST = '127.0.0.1'
PORT = 65432

def run_tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        print(f"Connecting to TCP Server at {HOST}:{PORT}...")
        client_socket.connect((HOST, PORT))
        print("Connected! Start typing your message (Press Ctrl+C to exit).\n")

        while True:
            # 1. Type message and send (Triggers on "Enter")
            msg = input("Client: ")
            client_socket.sendall(msg.encode('utf-8'))

            # 2. Wait for reply before allowing another send
            print("Waiting for server reply...\n")
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Server: {data.decode('utf-8')}")

    except KeyboardInterrupt:
        print("\n[+] TCP Client closed by user (Ctrl+C).")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_tcp_client()