import secrets

from libp2p.crypto.ed25519 import create_new_key_pair as create_new_ed25519_key_pair
from libp2p.peer.id import ID as PeerID
from libp2p.peer.pb import crypto_pb2


def store_key(path: str):
    key_pair = create_new_ed25519_key_pair(secrets.token_bytes(32))

    peer_id = PeerID.from_pubkey(key_pair.public_key)
    print(f"Peer ID: {peer_id}")

    protobuf = crypto_pb2.PrivateKey(Type=crypto_pb2.KeyType.Ed25519, Data=key_pair.private_key.to_bytes())

    # Store main private key
    with open(path, "wb") as f:
        f.write(protobuf.SerializeToString())
