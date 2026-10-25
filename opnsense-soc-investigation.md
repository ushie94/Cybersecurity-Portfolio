# OPNsense SOC Investigation: ICMP and HTTPS Connectivity

**Project:** Cybersecurity Portfolio

**Investigation date:** 23 October 2026

**Environment:** Local OPNsense and Ubuntu lab
**Status:** Initial connectivity investigation documented; follow-up items remain open.

---

## 1. Objective

Validate connectivity between the SOC client and the OPNsense firewall, correlate firewall events with packet-level evidence, and document the findings using a defensive security investigation workflow.

## 2. Lab Environment

| Component | Details |
|---|---|
| Firewall | OPNsense (`opnsense-fw01`) |
| SOC client | Ubuntu Server (`soc-client01`; hostname `ubuntu-srv01`) |
| SOC client IP | `192.168.10.187/24` |
| Firewall LAN IP | `192.168.10.1/24` |
| Host packet-capture interface | `virbr10` |
| HTTPS service port | TCP/443 |
| Virtual network | `soc-lan` |

## 3. Investigation Method

The investigation used three sources of evidence:

1. Connectivity test output from the SOC client.
2. OPNsense firewall Live View events.
3. Packet captures collected on the Ubuntu host with `tcpdump`.

The sources were correlated by endpoint addresses, protocol, port, and event timing. A firewall PASS event was interpreted as evidence that the firewall permitted the observed traffic, not as proof that the application authorized every request.

## 4. Test A — ICMP Connectivity

### Test performed

Four ICMP echo requests were sent from the SOC client to the OPNsense LAN address:

`192.168.10.187 → 192.168.10.1`

### Observations

- The client received four replies out of four requests.
- The host packet capture showed ICMP echo requests and echo replies.
- OPNsense Live View recorded a matching ICMP PASS event.
- The observed rule label was `Default allow LAN to any rule`.

### Finding

**Result: Successful.**

The evidence confirms ICMP communication between the SOC client and the firewall LAN interface during the test.

### Evidence files

- [OPNsense ICMP PASS event](soc-lab/evidence/opnsense-icmp-pass-log.png)
- [ICMP request/reply packet capture](soc-lab/evidence/tcpdump-icmp-request-reply.png)


## 5. Test B — HTTPS and TCP Connectivity

### Test performed

An HTTPS request was made from the SOC client to:

`https://192.168.10.1/`

The request used `curl -k -I --connect-timeout 5`, which skips certificate verification and requests response headers.

### Packet-level observations

The host capture showed traffic between:

- Client: `192.168.10.187:39478`
- Firewall: `192.168.10.1:443`

The capture included the TCP SYN, SYN-ACK, and ACK handshake, followed by bidirectional traffic and connection teardown.

This confirms that the TCP connection was established. A reset or connection teardown packet by itself is not proof of malicious activity.

### Firewall log observations

OPNsense Live View recorded a TCP PASS event with these details:

- Interface/direction: LAN / In
- Client: `192.168.10.187:39478`
- Destination: `192.168.10.1:443`
- Action: PASS
- Rule label: `anti-lockout rule`

The event matches the observed connection's endpoints and destination port.

### Application-level observations

Two different HTTP response statuses were observed across requests:

- `HTTP/2 200`: a successful HTTP response.
- `HTTP/2 403`: the server refused the particular request.

These responses are not equivalent. The available evidence does not yet establish why the status differed between requests. Do not describe this discrepancy as resolved.

### Finding

**Result: TCP connectivity confirmed; application behavior requires follow-up.**

The firewall permitted the observed HTTPS connection and the TCP handshake completed. The differing HTTP responses remain unexplained. A firewall PASS event does not guarantee an HTTP 200 response.

### Evidence files

- [OPNsense HTTPS PASS event](soc-lab/evidence/opnsense-https-pass-anti-lockout.png)
- [HTTPS TCP handshake packet capture](soc-lab/evidence/tcpdump-https-handshake.png)

## 6. Test C — ICMP Firewall Rule Enforcement

### Objective

Test whether an explicit OPNsense LAN rule blocks ICMP traffic from the Ubuntu client to a specific destination, and validate the result using firewall logs and a repeated connectivity test.

### Rule Configuration

- Interface: LAN
- Direction: In
- Protocol: ICMP
- Source: `192.168.10.187/32`
- Destination: `1.1.1.1/32`
- Action: Block
- Logging: Enabled
- Rule order: Above the default IPv4 LAN allow rule

The `/32` prefix matches one IPv4 address. The specific block rule was placed above the broader allow rule.

### Test A — Rule Enabled

From the Ubuntu client, executed:

`ping -c 4 1.1.1.1`

**Result:** Four packets transmitted, zero received, and 100% packet loss.

OPNsense Live View displayed four matching ICMP block events labelled `LAB - Block ICMP test`.

### Test B — Rule Disabled

After disabling the temporary rule and applying the configuration, the same ping test was repeated.

**Result:** Four packets transmitted, four received, and 0% packet loss.

OPNsense Live View showed ICMP PASS events under the default IPv4 LAN allow rule.

### Finding

The results support the conclusion that the temporary firewall rule blocked the tested ICMP traffic. After the rule was disabled, the same test succeeded. The matching firewall logs provide evidence consistent with the client-side results.

This finding is limited to the source, destination, protocol, and lab configuration tested.

### Evidence

- E-06 — [OPNsense ICMP block rule configuration](soc-lab/evidence/opnsense-icmp-block-rule.png)
- E-07 — [OPNsense blocked ICMP events](soc-lab/evidence/opnsense-icmp-block-logs.png)
- E-08 — [Before-and-after ICMP ping results](soc-lab/evidence/icmp-block-test-before-after.png)

### Cleanup

The temporary block rule was disabled after testing and retained in the configuration for future practice.

## 7. Timestamp Correlation

The Ubuntu host reported:

- Local time zone: WAT (UTC+1)
- UTC time: one hour behind WAT

The packet capture showed an event around `13:43:58`, while OPNsense Live View showed a matching event around `12:43:58`.

The OPNsense shell reports UTC (+0000), while the Ubuntu host reports WAT (UTC+1). This timezone difference explains the one-hour difference in displayed times, assuming both system clocks are synchronized. Clock synchronization has not yet been independently verified. Preserve the original timestamps and record the timezone used when interpreting them.

Do not silently adjust the original evidence timestamps.

## 8. NIST Cybersecurity Framework 2.0 Alignment

This exercise supports selected activities associated with the following functions:

- **Govern:** Maintain documented investigation procedures and evidence-handling expectations.
- **Identify:** Record lab assets, network interfaces, addresses, and relevant services.
- **Protect:** Observe the configured firewall enforcement and management-access rule.
- **Detect:** Review firewall events and packet captures to identify and understand network activity.
- **Respond:** Correlate evidence and investigate the unexplained HTTP response difference.
- **Recover:** No recovery activity was performed or demonstrated in this investigation.

These are practical learning alignments, not a claim of formal NIST CSF compliance.

## 9. Evidence Register

| Evidence ID | Evidence description | Status |
|---|---|---|
| E-01 | Client ICMP test output | Test result documented; terminal-output screenshot not listed among the four confirmed files |
| E-02 | OPNsense ICMP PASS event | File confirmed present |
| E-03 | ICMP request/reply packet capture | File confirmed present |
| E-04 | OPNsense HTTPS PASS event | File confirmed present |
| E-05 | HTTPS TCP handshake packet capture | File confirmed present |
| E-06 | OPNsense ICMP block rule configuration | File added for review |
| E-07 | OPNsense Live View showing blocked ICMP events | File added for review |
| E-08 | Before-and-after ICMP ping results | File added for review |

Evidence should remain unaltered. Keep original screenshots and avoid including passwords, session cookies, or unrelated sensitive information.

## 10. Outstanding Actions

- [x] Confirm the four screenshot filenames and locations.
- [x] Confirm the TCP handshake screenshot exists.
- [ ] Verify the OPNsense time zone and clock.
- [ ] Investigate the HTTP 200 versus HTTP 403 difference using relevant logs and repeatable observations only if needed.
- [ ] Record any additional findings before closing the investigation.

## 11. Overall Conclusion

The lab demonstrated successful ICMP communication and successful TCP connection establishment to the OPNsense HTTPS service. Firewall logs and packet captures provided complementary evidence of the observed traffic.

The difference between the HTTP 200 and HTTP 403 responses, and the one-hour timestamp discrepancy, remain open investigation items. These should be resolved or explicitly left as limitations before the report is marked complete.

---

**Report status:** Initial documentation prepared; evidence verification and follow-up investigation pending.
