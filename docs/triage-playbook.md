# SYN Scan Alert Triage Playbook

## Purpose and scope

Use this guide to review a possible SYN-scan alert produced by this repository. The detector reads saved PCAP or PCAPNG files; it does not monitor live traffic. A threshold match is a lead for investigation, not proof of malicious activity.

## Preserve the evidence

1. Keep the original authorised capture unchanged.
2. Record the capture source, collection time and timezone, and any known test activity.
3. Calculate a SHA-256 hash for the file and store it with the case notes.
4. Share only a sanitised capture or synthetic sample.

## Validate the alert

1. Confirm the detector command and threshold used.
2. Record the source address, destination addresses, unique destination ports, and time window visible in the capture.
3. Check whether the source belongs to an approved scanner, administrator, or lab exercise.
4. Compare the activity with firewall, endpoint, authentication, and service logs for the same time window.
5. Check whether the capture is complete enough to support the conclusion.

## Assess and respond

- **Expected activity:** document the owner and purpose, then close as authorised testing.
- **Unexplained activity with no confirmed impact:** preserve relevant logs, notify the system owner, and continue monitoring.
- **Corroborated compromise or service impact:** follow the organisation's incident response process and escalate to the incident lead.
- Apply blocks or isolate systems only with the system owner's or incident lead's approval.

## Record the outcome

Document the evidence reviewed, decision, actions and approver, remaining uncertainty, and lessons learned. Avoid recording passwords, tokens, or unnecessary personal data.
