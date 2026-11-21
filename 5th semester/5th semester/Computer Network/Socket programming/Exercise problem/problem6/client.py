import socket
import sys

HOST = '127.0.0.1'  # Server IP address
PORT = 65432        # Server Port

def start_client():
    # Connection-oriented (TCP) socket creation
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print(f"[*] Connected to Server at {HOST}:{PORT}")
        print("[*] Type a message and press Enter. Press Ctrl+C to exit.\n")

        while True:
            # 1. Send input when 'Enter' key is pressed
            message = input("Client: ")
            if not message:
                continue

            client_socket.sendall(message.encode('utf-8'))

            # 2. Lockstep rule: Block until a reply comes back from the server thread
            print("Waiting for server response...")
            reply = client_socket.recv(1024)
            if not reply:
                print("\n[!] Server disconnected.")
                break

            print(f"Server: {reply.decode('utf-8')}\n")

    except KeyboardInterrupt:
        print("\n[*] Chat stopped by client user (Ctrl+C). Exiting...")
    except ConnectionRefusedError:
        print("[!] Could not connect. Ensure server.py is running.")
    finally:
        client_socket.close()

if __name__ == '__main__':
    start_client()