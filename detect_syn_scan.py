#!/usr/bin/env python3
"""Flag possible SYN scans in an authorised saved PCAP file."""

import argparse
from collections import Counter

from scapy.all import IP, IPv6, TCP, rdpcap


def source_ip(packet) -> str:
    if IP in packet:
        return packet[IP].src
    if IPv6 in packet:
        return packet[IPv6].src
    return "unknown"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pcap", help="path to a saved PCAP or PCAPNG file")
    parser.add_argument("--threshold", type=int, default=20,
                        help="unique destination ports from one source (default: 20)")
    args = parser.parse_args()
    if args.threshold < 2:
        parser.error("threshold must be at least 2")

    ports_by_source = {}
    for packet in rdpcap(args.pcap):
        if TCP not in packet or not (IP in packet or IPv6 in packet):
            continue
        flags = int(packet[TCP].flags)
        # SYN set, ACK clear: a connection initiation, not a completed handshake.
        if flags & 0x02 and not flags & 0x10:
            ports_by_source.setdefault(source_ip(packet), set()).add(int(packet[TCP].dport))

    findings = [(source, len(ports)) for source, ports in ports_by_source.items()
                if len(ports) >= args.threshold]
    if not findings:
        print("No SYN scan pattern met the configured threshold.")
        return

    for source, port_count in sorted(findings, key=lambda item: item[1], reverse=True):
        print(f"Possible SYN scan: source={source}, unique_destination_ports={port_count}")


if __name__ == "__main__":
    main()
