import socket
import threading
import sys

HOST = '127.0.0.1'  # Server IP address
PORT = 65432        # Server Port

def handle_client(conn, addr):
    """
    Worker thread that manages two-way, lockstep chatting with a single client.
    """
    print(f"\n[+] Client connected: {addr}")
    try:
        while True:
            # 1. Receive message from client
            data = conn.recv(1024)
            if not data:
                print(f"\n[-] Client {addr} disconnected.")
                break

            message = data.decode('utf-8')
            print(f"\n[Client {addr[1]}]: {message}")

            # 2. Strict Ping-Pong: Server must reply before client can send another message
            reply = input(f"[Reply to Client {addr[1]}]: ")
            conn.sendall(reply.encode('utf-8'))

    except (ConnectionResetError, ConnectionAbortedError):
        print(f"\n[!] Connection lost with Client {addr[1]}.")
    except KeyboardInterrupt:
        print(f"\n[*] Chat closed by server operator for Client {addr[1]}.")
    finally:
        conn.close()

def start_server():
    # Connection-oriented (TCP) socket creation
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # #reuse the port after terminating the program it still allocate for the port to avoid it used this line code
       #Says the option belongs to the socket level
        
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"[*] Multi-Threaded TCP Server listening on {HOST}:{PORT}")
        print("[*] Press Ctrl+C on either side to stop the chat.\n")

        while True:
            # Main thread accepts new incoming connections
            conn, addr = server_socket.accept()

            # Spawn a thread to handle communication with this client
            client_thread = threading.Thread(
                target=handle_client,
                args=(conn, addr),
                daemon=True  # Thread closes when main server process terminates
            )
            client_thread.start()

    except KeyboardInterrupt:
        print("\n[*] Server stopping (Ctrl+C pressed)...")
    finally:
        server_socket.close()

if __name__ == '__main__':
    start_server()