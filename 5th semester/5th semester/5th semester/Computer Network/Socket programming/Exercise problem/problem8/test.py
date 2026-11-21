import socket
import struct
import threading
import time
import sys

MULTICAST_GROUP = '224.1.1.1'
MULTICAST_PORT = 5005

class ElectorateProcess:
    def __init__(self, electorate_id: int, vote: str):
        self.id = electorate_id
        self.vote = vote.upper()
        self.votes_collected = {self.id: self.vote}  # Record own vote
        self.running = True

        # 1. Create UDP socket for connectionless multicast
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        
        # 2. Allow port reuse so 5 processes can bind to the same multicast port
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        if hasattr(socket, 'SO_REUSEPORT'):
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        self.sock.bind(('', MULTICAST_PORT))

        # 3. Join the Multicast Group
        mreq = struct.pack('4sL', socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)

    def vote_broadcaster(self):
        """Background thread: Periodically broadcasts vote until all 5 votes are collected."""
        message = f"{self.id}:{self.vote}".encode('utf-8')
        while self.running and len(self.votes_collected) < 5:
            try:
                self.sock.sendto(message, (MULTICAST_GROUP, MULTICAST_PORT))
            except Exception:
                pass
            time.sleep(1)

    def vote_receiver(self):
        """Background thread: Listens for multicast votes from other electorates."""
        while len(self.votes_collected) < 5:
            try:
                data, _ = self.sock.recvfrom(1024)
                message = data.decode('utf-8')
                
                if ':' in message:
                    sender_id_str, sender_vote = message.split(':', 1)
                    sender_id = int(sender_id_str)
                    sender_vote = sender_vote.strip().upper()

                    # Record vote if it's from a new electorate and valid
                    if sender_id not in self.votes_collected and sender_vote in ['A', 'B']:
                        self.votes_collected[sender_id] = sender_vote
                        print(f"[+] Received vote from Electorate {sender_id}. "
                              f"Progress: [{len(self.votes_collected)}/5] votes collected.")
            except Exception:
                break

    def start_election(self):
        print(f"\n[*] Electorate {self.id} successfully cast vote for Candidate '{self.vote}'.")
        print(f"[*] Waiting for all 5 electorate votes...\n")

        # Start receiver and broadcaster threads
        recv_thread = threading.Thread(target=self.vote_receiver, daemon=True)
        broad_thread = threading.Thread(target=self.vote_broadcaster, daemon=True)

        recv_thread.start()
        broad_thread.start()

        # Wait until votes from all 5 electorates are collected
        while len(self.votes_collected) < 5:
            time.sleep(0.2)

        # Cleanup socket
        self.running = False
        self.sock.close()

        # Independently calculate and print results
        self.display_winner()

    def display_winner(self):
        count_a = sum(1 for v in self.votes_collected.values() if v == 'A')
        count_b = sum(1 for v in self.votes_collected.values() if v == 'B')

        print("\n" + "=" * 45)
        print(f"       INDEPENDENT ELECTION RESULTS (Process {self.id})")
        print("=" * 45)
        print("Individual Votes:")
        for electorate_id in sorted(self.votes_collected.keys()):
            print(f"  • Electorate {electorate_id}: Voted Candidate {self.votes_collected[electorate_id]}")
        
        print("-" * 45)
        print(f"Tally -> Candidate A: {count_a} vote(s) | Candidate B: {count_b} vote(s)")
        
        if count_a > count_b:
            print("🏆 WINNER: Candidate A")
        elif count_b > count_a:
            print("🏆 WINNER: Candidate B")
        else:
            print("🤝 RESULT: Tie Game")
        print("=" * 45 + "\n")



try:
        electorate_id = int(input("Enter Electorate ID (1 to 5): "))
        if electorate_id < 1 or electorate_id > 5:
            print("Error: Electorate ID must be between 1 and 5.")
            sys.exit(1)

        vote = input("Cast your vote (A or B): ").strip().upper()
        if vote not in ['A', 'B']:
            print("Error: Vote must be 'A' or 'B'.")
            sys.exit(1)

        process = ElectorateProcess(electorate_id, vote)
        process.start_election()
except ValueError:
        print("Invalid input. Please enter a valid number for ID and 'A' or 'B' for vote.")
except KeyboardInterrupt:
        print("\nExiting election process...")