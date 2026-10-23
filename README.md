
# Cybersecurity Portfolio — Victor Ushie

Welcome to my cybersecurity portfolio. This repository documents my hands-on learning, lab experiments, technical investigations, and developing skills in defensive security.

My current focus is **Security Operations (SOC), network security, security log analysis, and incident investigation**. My background in banking operations, Mathematics Education, and data analytics also informs my interest in investigating events, troubleshooting systems, and communicating technical findings.

## Current Projects

### 1. OPNsense Firewall & Network Security Lab

**Status:** In progress

Built a small OPNsense and Ubuntu Server lab to practise network defence and investigate the relationship between packet captures and firewall logs.

Completed tests include:

- Verified ICMP connectivity from the Ubuntu client to the firewall, receiving 4 replies from 4 requests.
- Captured ICMP requests and replies with `tcpdump`.
- Observed firewall PASS events in OPNsense Live View.
- Captured TCP traffic during HTTPS connectivity testing.

The HTTP/2 responses observed during testing included `200` and `403`; the difference remains under investigation. Timestamp correlation also remains provisional pending independent clock-synchronization verification.

- [View the OPNsense lab and evidence](soc-lab/README.md)
- [Read the SOC investigation report](opnsense-soc-investigation.md)

### 2. Security Log Analysis & Brute-Force Detection

**Status:** In progress

Exploring the preparation and analysis of Windows authentication events and network-flow data to investigate suspicious login activity.

Planned work includes:

- Reviewing source data and its structure.
- Normalising relevant fields for consistent analysis.
- Investigating failed and successful authentication events.
- Exploring correlations between host events and network activity.
- Documenting validated findings and limitations.

Detection claims and conclusions will be published only after they have been tested against the available data.

[View the log-analysis project](log_parsing_project/)

### 3. Security Telemetry Dashboard

**Status:** Planned

A future project to present safe sample security events, investigation findings, and lab-generated telemetry through a dashboard.

The initial development will focus on a small, testable prototype. Deployment using Vercel may be considered when the application is ready.

## Skills Under Development

- **Networking:** IP addressing, routing, DNS, and connectivity troubleshooting.
- **Network Defence:** Firewall configuration, rule testing, and traffic filtering.
- **Security Operations:** Log analysis, alert investigation, and incident-response workflows.
- **Data Analysis:** Data preparation, normalisation, and investigation-oriented analysis.
- **Automation:** Python and shell scripting fundamentals.
- **Documentation:** Reproducible procedures, test evidence, and technical findings.

## Learning Roadmap

My immediate priority is to strengthen networking and defensive-security fundamentals, then expand into packet analysis, SOC tooling, and detection engineering.

Longer-term areas of development include cloud security, cloud-native security, and AI application security.

## Repository Principles

- Document what has actually been implemented and tested.
- Distinguish completed work from work in progress and planned projects.
- Use safe, appropriately sourced sample data for public demonstrations.
- Keep virtual-machine disks, installer images, credentials, and sensitive lab data out of the public repository.
- Include screenshots and test results only when they provide genuine evidence of the work.

## Connect

- **GitHub:** [@ushie94](https://github.com/ushie94)
- **LinkedIn:** [Victor Ushie](https://www.linkedin.com/in/victor-ushie/)

---

This portfolio is a work in progress. Project documentation will be expanded as testing, validation, and evidence collection are completed.
