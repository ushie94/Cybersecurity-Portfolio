# SOC Home Lab: Infrastructure & Security Engineering

"It all starts with a click."

## Executive Summary

This repository contains the documentation, configuration files, and playbooks for my SOC Home Lab. The objective is to build a professional-grade, multi-node lab environment to practice network architecture, log analysis, and threat detection.

## Lab Inventory

The lab is currently architected using **VirtualBox** and consists of the following nodes:

| Role                 | OS             | Purpose                                            |
| :------------------- | :------------- | :------------------------------------------------- |
| **Operational Node** | Ubuntu Server  | Log ingestion, SIEM, and backend services.         |
| **Workstation A**    | Ubuntu Desktop | Incident response and manual network analysis.     |
| **Workstation B**    | Windows 10 Pro | User traffic simulation and host-based monitoring. |

---

## 📺 Project Series Index

This lab is documented via a multi-part video series.

| Part   | Topic                                      | Status      |
| :----- | :----------------------------------------- | :---------- |
| Part 1 | Lab Architecture & VirtualBox Setup        | ✅ Complete |
| Part 2 | Static IP Configuration & Network Security | ✅ Complete |
| Part 3 | Ubuntu Server Deployment & Operation       | ✅ Complete |
| Part 4 | Log Parsing & Data Normalization           | ⏳ Upcoming |
| Part 5 | Detection Engineering (SIEM Integration)   | ⏳ Upcoming |

---

## 🛠 Toolchain & Playbooks

Every tool used in this lab is documented for repeatability.

- **Network Analysis:** `tcpdump`, `tshark`, `Wireshark`
- **Log Ingestion:** `Wazuh` (Deployment configuration files in `/docs/wazuh/`)
- **Automation:** Python (Log parsing scripts located in `/scripts/`)

---

## Security Philosophy

This lab is built on three pillars:

1. **Visibility:** Capturing traffic and logs from multiple OS types (Linux/Windows).
2. **Detection:** Using the ingested data to identify anomalous behavior.
3. **Documentation:** Maintaining a "Playbook" approach to security engineering.

## Future Roadmap

- [ ] Implement Active Directory (Domain Controller) for identity monitoring.
- [ ] Develop automated detection rules for brute-force attacks.
- [ ] Integrate a professional-grade SIEM dashboard.

---

_Created by Victor Ushie_ | _SOC Analyst in Training_
