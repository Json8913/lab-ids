# Lab IDS

A Python prototype that checks an authorised saved packet capture for a possible TCP SYN scan by counting unique destination ports contacted by each source address.

**Stage:** Initial prototype.

## Scope and safety

The detector reads saved PCAP or PCAPNG files and does not monitor a live interface or transmit traffic. Use generated lab traffic or a capture you are authorised to inspect.

## Requirements

- Python 3.10 or newer
- Scapy

Install dependencies:

    python3 -m pip install -r requirements.txt

## Generate a safe sample

    python3 make_sample_pcap.py

This writes a local sample.pcap with synthetic TCP SYN packets and a synthetic DNS query. The generated file is ignored by Git.

## Usage

    python3 detect_syn_scan.py sample.pcap --threshold 3

The expected result is a possible scan alert for source 10.0.0.5. The default threshold is 20.

## Smoke check

The generated sample produced an alert for 10.0.0.5 after three unique destination ports were contacted.

## Detection logic

A possible scan is reported when one source sends TCP SYN packets to at least the configured number of unique destination ports.

## Findings and limits

This is a simple detection exercise, not a production IDS. A threshold match is an alert for investigation, not proof of malicious activity. Busy services, incomplete captures, and unusual applications can affect results.

## Mitigations

Validate alerts against host and firewall logs, review whether the source is expected, and apply network restrictions only after confirming the activity.

## Screenshots

Add a redacted output screenshot using generated or authorised lab traffic.
