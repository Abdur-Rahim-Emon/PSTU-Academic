import socket
import subprocess# FOR LAUNCHES EXTERNAL PROGRAM
import os
import platform# DETECTS THE OS 
import time

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999
EOF_MARKER = b"__EOF__"

# Buffer threshold (e.g., 500 KB) required before triggering media player
BUFFER_THRESHOLD = 500 * 1024  

def launch_media_player(filepath: str):
    """Launches system media player asynchronously while downloading continues."""
    print(f"\n>>> [CLIENT] Buffer threshold reached! Launching player for '{filepath}' <<<\n")
    system_name = platform.system()
    # [CLIENT ] USE WHICH PROGRAM MESSAGE IS HOWING
    try:
        if system_name == "Windows":
            os.startfile(filepath)
        elif system_name == "Darwin":  # macOS
            subprocess.Popen(["open", filepath])
        else:  # Linux / Unix
            subprocess.Popen(["xdg-open", filepath])
    except Exception as e:
        print(f"[CLIENT] Warning: Failed to launch automatic player ({e})")

def start_streaming_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5.0) # TIME OUT FOR RECEVING PACKET

    requested_file = input("Enter requested media filename (e.g., sample.mp4 / sample.mp3): ").strip()
    output_file = f"downloaded_{os.path.basename(requested_file)}"

    # Send stream request packet to server
    client_socket.sendto(requested_file.encode('utf-8'), (SERVER_IP, SERVER_PORT))

    try:
        response, _ = client_socket.recvfrom(1024)
        if response != b"OK":
            print(f"[CLIENT] Server Error: {response.decode('utf-8')}")
            return
    except socket.timeout:
        print("[CLIENT] Error: Server did not respond (connection timeout).")
        return

    print(f"[CLIENT] Receiving stream... Saving to '{output_file}'")

    total_bytes = 0
    packets_received = 0
    player_launched = False

    with open(output_file, "wb") as f:
        while True:
            try:
                # Receive datagram packet (max buffer 2048 to fit 1000-2000 byte payloads)
                packet, _ = client_socket.recvfrom(2048)

                if packet == EOF_MARKER:
                    print("\n[CLIENT] End of file stream marker received.")
                    break

                # Write chunk and flush stream immediately to disk
                f.write(packet)
                f.flush()
                
                total_bytes += len(packet)
                packets_received += 1

                print(f"\r[CLIENT] Received: {total_bytes} bytes ({packets_received} packets)", end="")

                # Launch Media Player when enough bytes are buffered
                if not player_launched and total_bytes >= BUFFER_THRESHOLD:
                    launch_media_player(output_file)
                    player_launched = True

            except socket.timeout:
                print("\n[CLIENT] Timeout: Stream interrupted or completed without EOF marker.")
                break

    print(f"\n[CLIENT] Download finished. Total received: {total_bytes} bytes.")

    # Launch player if total file size was smaller than threshold
    if not player_launched and os.path.exists(output_file) and total_bytes > 0:
        launch_media_player(output_file)

if __name__ == "__main__":
    start_streaming_client()