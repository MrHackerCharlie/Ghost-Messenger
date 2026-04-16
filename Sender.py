import socks  # pip install PySocks
import socket
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def send_via_tor(onion_address, msg, key):
    # Setup SOCKS5 proxy to route through Tor (Default port 9050)
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

    # Encrypt
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    encrypted_msg = aesgcm.encrypt(nonce, msg.encode(), None)
    
    # Send
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            print(f"[*] Tunneling to {onion_address}...")
            s.connect((onion_address, 80))
            s.sendall(nonce + encrypted_msg)
            print("[+] Injection Successful.")
        except Exception as e:
            print(f"[-] Failed: {e}")

KEY = b'12345678901234567890123456789012'
target = input("Enter Receiver's .onion address: ")
message = input("Secret Message: ")
send_via_tor(target, message, KEY)