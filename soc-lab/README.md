
# OPNsense Firewall and SOC Network Lab

**Status:** In progress

## Overview

This project documents a small virtual network built to practise firewall configuration, network troubleshooting, packet capture, and security-event investigation.

The lab uses OPNsense as the firewall and an Ubuntu Server client on a dedicated virtual LAN. The goal is to correlate observed network traffic with firewall log events and document evidence-based findings.

## Lab Topology

| Component | Role | Lab address |
|---|---|---|
| OPNsense firewall | LAN gateway and firewall | `192.168.10.1/24` |
| Ubuntu client | Test client | `192.168.10.187/24` |
| Ubuntu client's default gateway | OPNsense LAN interface | `192.168.10.1` |

These are private lab addresses, not public service endpoints.

## Tests and Findings

### 1. ICMP Connectivity

**Result:** Successful — 4 of 4 echo requests received replies.

- Sent ICMP echo requests from the Ubuntu client (`192.168.10.187`) to the OPNsense LAN interface (`192.168.10.1`).
- Observed ICMP echo requests and replies in the `tcpdump` capture.
- Observed a corresponding PASS event in OPNsense Live View under the default LAN allow rule.

**Finding:** The test confirmed ICMP connectivity between the client and the firewall LAN interface during this test.

**Evidence:**

- [OPNsense ICMP PASS log](evidence/opnsense-icmp-pass-log.png)
- [tcpdump ICMP request and reply](evidence/tcpdump-icmp-request-reply.png)

### 2. HTTPS/TCP Connectivity

**Result:** TCP connection established; HTTP response behavior requires further investigation.

- Sent HTTPS requests to the OPNsense LAN address.
- Used `tcpdump` to observe the TCP handshake and bidirectional traffic.
- Observed a corresponding PASS event in OPNsense Live View under the anti-lockout rule.
- Recorded HTTP/2 responses including `200` and `403`. The difference remains unexplained.

A successful TCP connection does not establish that every HTTP request succeeds. A firewall PASS event confirms that the observed traffic was permitted by the matching firewall rule; it does not guarantee a successful application-level response.

**Finding:** The TCP connection was established, but the reason for the differing HTTP responses has not yet been determined.

**Evidence:**

- [OPNsense HTTPS PASS log](evidence/opnsense-https-pass-anti-lockout.png)
- [tcpdump HTTPS handshake](evidence/tcpdump-https-handshake.png)

## Timestamp Interpretation

The OPNsense interface reports UTC (`+0000`), while the Ubuntu host reports West Africa Time (WAT, UTC+1).

This timezone difference is consistent with a one-hour difference in displayed timestamps if both system clocks are synchronized. Clock synchronization has not yet been independently verified, so timestamp correlation remains provisional.

Preserve the original evidence timestamps. Do not silently adjust timestamps or claim precise correlation until clock synchronization has been checked.

## Security Framework Alignment

This exercise supports practical learning relevant to the NIST Cybersecurity Framework (CSF) 2.0, particularly:

- **Identify (ID):** Documenting lab assets, topology, and investigation scope.
- **Protect (PR):** Understanding network boundaries and firewall rules.
- **Detect (DE):** Observing network traffic and firewall log events.
- **Respond (RS):** Recording evidence and identifying follow-up questions.

These are learning alignments, not a claim of formal NIST CSF compliance.

## Outstanding Work

- Investigate why HTTPS requests returned both HTTP/2 `200` and `403`.
- Independently verify clock synchronization before drawing conclusions from timestamps.
- Continue testing firewall rules and documenting reproducible results.
- Review screenshots for sensitive information before public release.

## Scope and Limitations

This is a small virtual lab for defensive-security learning. Results apply to the tested lab configuration and do not establish the security of a production network.

The firewall virtual disk and other large virtual-machine assets are kept out of the public repository. Only selected evidence screenshots and documentation are intended for publication.
