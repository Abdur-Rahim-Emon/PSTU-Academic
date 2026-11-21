import socket
import os
HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 1000
#reciever receive 1000bytes max 
def request_file(filename):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print(f"[CLIENT] Connected to server at {HOST}:{PORT}")

        # Send requested file name to the server
        client_socket.sendall(filename.encode('utf-8'))

        output_filename = f"downloaded_{filename}"
       # output_filename = f"downloaded_{os.path.basename(filename)}"
        print(f"[CLIENT] Requesting '{filename}'...")

        with open(output_filename, 'wb') as f:
            while True:
                chunk = client_socket.recv(BUFFER_SIZE)
                if not chunk:
                    break  # Server finished sending and closed socket
                
                # Handle file not found error signal from server
                if chunk.startswith(b"ERROR:"):
                    print(f"[CLIENT] Server error: {chunk.decode('utf-8')}")
                    f.close()
                    import os
                    os.remove(output_filename)  # Clean up empty local file
                    return

                f.write(chunk)

        print(f"[CLIENT] Download complete! File saved as '{output_filename}'.")

    except ConnectionRefusedError:
        print("[CLIENT] Could not connect to the server. Is server.py running?")
    except Exception as e:
        print(f"[CLIENT] Error: {e}")
    finally:
        client_socket.close()

#if __name__ == "__main__": #check it run directly or not
file_to_download = input("Enter the filename to download from server: ").strip()
if file_to_download:
        request_file(file_to_download)
else:
        print("Filename cannot be empty.")