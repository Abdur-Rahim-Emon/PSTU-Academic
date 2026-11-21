import socket
import threading
import time
import os

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Arbitrary non-privileged port
BUFFER_SIZE = 1000  # Max size per flush operation (bytes)
SLEEP_TIME = 0.2    # 200 milliseconds delay between chunks

def handle_client_file_transfer(client_socket, filename):
    """
    Worker function run in a dedicated thread.
    Handles file reading, chunking, rate-limiting sleep, and network transfer.
    """
    thread_name = threading.current_thread().name
    print(f"[{thread_name}] Handling request for file: '{filename}'")

    try:
        # Check if the requested file exists
        if not os.path.isfile(filename):
            print(f"[{thread_name}] Error: File '{filename}' not found.")
            client_socket.sendall(b"ERROR: File not found")
            return

        # Open file in binary mode for reading
        with open(filename, 'rb') as f:
            total_bytes_sent = 0
            
            while True:
                # Read at most 1000 bytes
                chunk = f.read(BUFFER_SIZE)
                if not chunk:
                    break  # End of file reached
                
                # Send chunk to client (flush operation)
                client_socket.sendall(chunk)
                total_bytes_sent += len(chunk)
                
                # Sleep for 200ms after each chunk transmission
                time.sleep(SLEEP_TIME)

        print(f"[{thread_name}] Successfully sent '{filename}' ({total_bytes_sent} bytes).")

    except Exception as e:
        print(f"[{thread_name}] Connection error: {e}")
    finally:
        # Close the socket for this specific client connection
        client_socket.close()
        print(f"[{thread_name}] Socket closed.")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Enable immediate port reuse after termination
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[SERVER] File server listening on {HOST}:{PORT}...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"\n[SERVER] New connection from {client_address}")

            # 1. Read the filename from the client first
            filename = client_socket.recv(1024).decode('utf-8').strip()

            # 2. Spawn a new thread passing the filename as an argument to the thread constructor
            client_thread = threading.Thread(
                target=handle_client_file_transfer,
                args=(client_socket, filename)
            )
            
            # Start the thread to handle file transfer independently
            client_thread.start()

    except KeyboardInterrupt:
        print("\n[SERVER] Server shutting down...")
    finally:
        server_socket.close()

#if __name__ == "__main__":
start_server()