import socket
from stem.control import Controller
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# 1. Start the Onion Service (The Ghost Server)
def start_onion_receiver(key):
    port = 9999
    aesgcm = AESGCM(key)
    
    with Controller.from_port(port=9051) as controller:
        controller.authenticate() # Use your Tor control password if set
        
        # Create an ephemeral onion service
        response = controller.create_ephemeral_hidden_service({80: port}, await_publication=True)
        onion_address = f"{response.service_id}.onion"
        print(f"\n[!!!] GHOST ADDRESS: {onion_address}")
        print("[*] Waiting for incoming encrypted data...")

        # Create a local socket to catch the forwarded Tor traffic
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('127.0.0.1', port))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                nonce, encrypted_payload = data[:12], data[12:]
                msg = aesgcm.decrypt(nonce, encrypted_payload, None)
                print(f"\n[RECEIVED]: {msg.decode()}")

KEY = b'12345678901234567890123456789012' # Must be 32 bytes
start_onion_receiver(KEY)