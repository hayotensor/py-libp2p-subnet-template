from multiaddr import Multiaddr


def get_public_ip_interfaces(ip: str, port: int, protocol: str = "tcp") -> list[Multiaddr]:
    return [Multiaddr(f"/ip4/{ip}/{protocol}/{port}")]
