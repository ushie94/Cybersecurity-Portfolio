# SOC Investigation: External ICMP Connectivity Analysis

## 1. Objective

Investigate ICMP connectivity between an Ubuntu client virtual machine and the external IP address `1.1.1.1` through an OPNsense firewall. Wireshark and TShark were used to capture traffic, inspect packet headers, correlate requests and replies, and calculate round-trip time (RTT).

## 2. Lab Environment

| Component | Details |
|---|---|
| Client hostname | `ubuntu-srv01` |
| Client IP address | `192.168.10.187` |
| Default gateway | `192.168.10.1` |
| External destination | `1.1.1.1` |
| Capture interface | `virbr10` |
| Analysis tools | Wireshark and TShark |
| Evidence file | `soc-lab/packet-captures/icmp-external-connectivity.pcapng` |

The raw packet capture is stored locally and excluded from Git tracking by the repository's existing `.gitignore` rules.

## 3. Methodology

A live packet capture was started on the `virbr10` virtual bridge. While Wireshark was capturing, the Ubuntu client generated four ping requests using:

`ping -c 4 1.1.1.1`

The capture was stopped and saved as `icmp-external-connectivity.pcapng`. TShark was then used to inspect the saved capture and verify the protocol hierarchy, ICMP request/reply pairs, and packet timestamps.

## 4. Protocol Hierarchy

TShark reported the following protocol hierarchy:

| Protocol | Frames | Bytes |
|---|---:|---:|
| Ethernet | 12 | 952 |
| IPv4 | 8 | 784 |
| ICMP | 8 | 784 |
| ARP | 4 | 168 |

The capture contained 12 Ethernet frames, including eight IPv4/ICMP frames and four ARP frames.

## 5. ICMP Request and Reply Analysis

The following Wireshark display filter was used to inspect ICMP traffic involving `1.1.1.1`:

`icmp && ip.addr == 1.1.1.1`

TShark confirmed four ICMP Echo Requests (type 8) and four matching Echo Replies (type 0).

| ICMP Sequence | Request Frame | Reply Frame | Result |
|---:|---:|---:|---|
| 1 | 1 | 4 | Matching reply observed |
| 2 | 5 | 6 | Matching reply observed |
| 3 | 7 | 8 | Matching reply observed |
| 4 | 9 | 10 | Matching reply observed |

**Finding:** All four requests had matching replies with the same ICMP sequence numbers. The observed request/reply loss in this test was 0%.

## 6. IPv4 and Ethernet Header Findings

### IPv4 Header

The inspected Echo Request contained the following fields:

- Source IP: `192.168.10.187`
- Destination IP: `1.1.1.1`
- Time to Live (TTL): `64`
- Protocol: ICMP (IPv4 protocol number 1)
- IPv4 Total Length: `84` bytes

### Ethernet Header

The observed MAC addresses on the local LAN were:

- Client MAC: `52:54:00:fc:fb:d4`
- OPNsense LAN MAC: `52:54:00:46:ed:37`

For the outbound frame, the Ethernet destination was the OPNsense gateway's LAN MAC address, while the IPv4 destination remained `1.1.1.1`.

For the returning LAN frame, the Ethernet source was the gateway and the Ethernet destination was the client. The reply's IPv4 source was `1.1.1.1`, and its IPv4 destination was `192.168.10.187`.

**Finding:** IP addresses identify the network-layer source and destination, while Ethernet addresses provide delivery to the next hop on the local network.

## 7. Round-Trip Time Measurements

Round-trip time (RTT) was calculated by subtracting each request's capture timestamp from the timestamp of its matching reply.

| ICMP Sequence | Request Frame | Reply Frame | RTT |
|---:|---:|---:|---:|
| 1 | 1 | 4 | 147.157 ms |
| 2 | 5 | 6 | 155.031 ms |
| 3 | 7 | 8 | 172.550 ms |
| 4 | 9 | 10 | 169.675 ms |

### RTT Summary

- Average RTT: approximately 161.103 ms
- Minimum RTT: approximately 147.157 ms
- Maximum RTT: approximately 172.550 ms
- Matching replies: 4 out of 4
- Observed request/reply loss: 0%

These measurements describe this capture only and do not guarantee typical or future network latency.

## 8. SOC Analysis and Interpretation

The capture provides evidence that the Ubuntu client exchanged ICMP Echo Requests and matching Echo Replies with `1.1.1.1` during the test.

The packet headers demonstrate how an external IP destination can be reached through the gateway's local Ethernet address. The capture also includes ARP traffic, which is used for IPv4-to-MAC address resolution on a local network.

No unmatched request was observed among the four captured requests. This supports a finding of zero observed request/reply loss during this short test. It does not prove that the network is always healthy or free of packet loss.

The measured RTT ranged from approximately 147 ms to 173 ms. These values are observations from this specific test and should not be treated as a long-term network performance baseline.

## 9. Limitations

- This was a short capture of a single connectivity test.
- The findings do not establish the absence of other network issues.
- Ethernet addresses visible in a capture depend on the capture point.
- RTT values are based on timestamps recorded in the saved capture.
- The evidence does not indicate that an attack or security incident occurred.

## 10. Tools and Skills Demonstrated

- Live packet capture on a Linux virtual bridge
- Wireshark display filtering
- TShark protocol hierarchy analysis
- IPv4 and Ethernet header interpretation
- ICMP request/reply correlation
- RTT calculation from packet timestamps
- Evidence-based reporting and cautious conclusions
