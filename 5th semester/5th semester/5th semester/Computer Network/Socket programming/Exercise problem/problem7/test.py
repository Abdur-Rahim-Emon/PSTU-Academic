import socket
import struct
import threading
import sys

# Multicast Group Address (Class D IP range: 224.0.0.0 to 239.255.255.255)
MULTICAST_GROUP = '224.1.1.1'
MULTICAST_PORT = 5007

def receive_messages(sock):
    """
    Background worker thread function that continuously listens for 
    incoming multicast messages from any process in the group.
    """
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            message = data.decode('utf-8')
            # Print incoming message without interrupting the current input prompt line
            print(f"\r{message}\n> ", end="", flush=True)
        except Exception:
            break

def main():
    user_name = input("Enter your username: ").strip()
    if not user_name:
        user_name = "Anonymous"

    # 1. Create UDP socket (SOCK_DGRAM)
    #socket.IPPROTO_UDP Specify the UDP protocol
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    # 2. Set socket options to allow multiple processes on the same machine to bind to the port
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if hasattr(socket, 'SO_REUSEPORT'):#hasattr() checks something exists in the os or python provide so_reusport exists
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

    # 3. Bind to the multicast port on all network interfaces
    sock.bind(('', MULTICAST_PORT))

    # 4. Join the multicast group (IP_ADD_MEMBERSHIP)
    group = socket.inet_aton(MULTICAST_GROUP) #converts the ip to binary
    mreq = struct.pack('4sL', group, socket.INADDR_ANY) # convert binary 
    # 4sl = 4 byte string unsinged long integer
    #INADDR_ANY=ANY LOCAL NETWORKS
    #
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
 
    # 5. Set Multicast TTL (Time to Live) -> 1 limits to local subnet
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    # 6. Enable Multicast Loopback so processes (including self) receive group copies
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

    # Start the receiver thread in daemon mode (it means the thread stops when the main program stops)
    receiver_thread = threading.Thread(target=receive_messages, args=(sock,), daemon=True)
    receiver_thread.start()

    print(f"\n[+] Joined Multicast Chat Group ({MULTICAST_GROUP}:{MULTICAST_PORT})")
    print("[+] Type a message and press Enter. Press Ctrl+C or type 'exit' to leave.\n")

    try:
        while True:
            msg = input("> ")
            if msg.strip().lower() == 'exit':
                break
            
            if msg.strip():
                formatted_msg = f"[{user_name}]: {msg}"
                # Broadcast message to the entire multicast group
                sock.sendto(formatted_msg.encode('utf-8'), (MULTICAST_GROUP, MULTICAST_PORT))

    except KeyboardInterrupt:
        print("\n[*] Exiting multicast chat...")
    finally:
        # Drop membership and close socket gracefully
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq)
        sock.close()
        print("[*] Disconnected.")

if __name__ == '__main__':
    main()