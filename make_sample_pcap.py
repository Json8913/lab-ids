#!/usr/bin/env python3
"""Write a tiny synthetic PCAP for offline analysis demonstrations."""

from pathlib import Path

from scapy.all import DNS, DNSQR, IP, TCP, UDP, wrpcap


def main() -> None:
    packets = [
        IP(src="10.0.0.5", dst="10.0.0.1") / TCP(sport=40000 + index, dport=port, flags="S")
        for index, port in enumerate((22, 80, 443))
    ]
    packets.append(
        IP(src="10.0.0.8", dst="10.0.0.1")
        / UDP(sport=53000, dport=53)
        / DNS(rd=1, qd=DNSQR(qname="example.test"))
    )
    output = Path("sample.pcap")
    wrpcap(str(output), packets)
    print(f"Wrote {len(packets)} synthetic packets to {output}.")
    print("The file contains no captured network traffic.")


if __name__ == "__main__":
    main()
