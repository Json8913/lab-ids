# Lab IDS

A Python prototype that checks an authorised saved packet capture for a possible TCP SYN scan by counting unique destination ports contacted by each source address.

**Stage:** Initial prototype.

## Scope and safety

The detector reads saved PCAP or PCAPNG files and does not monitor a live interface or transmit traffic. Use generated lab traffic or a capture you are authorised to inspect.

## Requirements

- Python 3.10 or newer
- Scapy

Install Scapy with:

    python3 -m pip install scapy

## Usage

    python3 detect_syn_scan.py path/to/authorised-capture.pcap
    python3 detect_syn_scan.py path/to/authorised-capture.pcap --threshold 10

## Detection logic

A possible scan is reported when one source sends TCP SYN packets to at least the configured number of unique destination ports. The default threshold is 20.

## Findings and limits

This is a simple detection exercise, not a production IDS. A threshold match is an alert for investigation, not proof of malicious activity. Busy services, incomplete captures, and unusual applications can affect results.

## Mitigations

Validate the alert against host and firewall logs, review whether the source is expected, and apply network restrictions only after confirming the activity.

## Screenshots

Add a redacted output screenshot using generated or authorised lab traffic.
