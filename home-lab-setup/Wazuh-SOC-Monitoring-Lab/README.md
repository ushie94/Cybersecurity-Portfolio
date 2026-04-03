# 🛡️ Enterprise SOC Ecosystem: Wazuh, Wireshark, & Jira Integration

## 📌 Project Overview

This project demonstrates the deployment and optimization of a full-stack Security Operations Center (SOC) within a resource-constrained environment (8GB RAM). Beyond simple installation, this lab focuses on the **functional integration** of log management (Wazuh), packet analysis (Wireshark), and incident response workflows (Jira).

---

## 🛠️ The Technology Stack

- **SIEM/XDR:** Wazuh Manager (Ubuntu Server 22.04)
- **Endpoint:** Windows 10 Pro (with Sysmon & Wazuh Agent)
- **Network Analysis:** Wireshark (Host and Endpoint deployment)
- **Incident Management:** Jira Service Management (Cloud Integration)
- **Virtualization:** Oracle VirtualBox

---

## 🚀 Key Technical Achievements

### 1. Performance Tuning & JVM Optimization

Running a modern SIEM on 8GB of RAM is a challenge. To stabilize the environment, I performed **manual JVM Heap tuning**.

- **Problem:** Constant OOM (Out-of-Memory) crashes of `wazuh-indexer`.
- **Action:** Modified `/etc/wazuh-indexer/jvm.options` to reduce the heap size from **1.5GB** to **1GB (1024MB)**.
- **Result:** Stabilized the Wazuh API and Authentication services, allowing for a 100% success rate in agent enrollment.

### 2. Network Visibility with Wireshark

I deployed **Wireshark** across the host and endpoint to complement log-based alerts.

- **Purpose:** Correlating Wazuh alerts with real-time packet captures (PCAPs).
- **Use Case:** Identifying the exact nature of C2 (Command & Control) traffic that logs alone might miss.

### 3. Professional Workflow: Jira Ticketing

I integrated **Jira** to simulate a Tier 1 SOC Analyst experience.

- **Workflow:** Alert (Wazuh) ➡️ Investigation (Wireshark/Sysmon) ➡️ Documentation (Jira).
- **Goal:** Ensuring every high-severity alert follows a standardized incident response lifecycle.

---

## 📈 Current Project Status (Phase 2)

- [x] Ubuntu Server & Windows 10 VM Provisioning.
- [x] Wazuh Manager Installation & Memory Optimization.
- [x] Wireshark Deployment for Network Forensics.
- [x] Jira Ticketing System Setup.
- [ ] **Next Step:** Finalizing the automated alert bridge between Wazuh and Jira.

---

## 📸 Lab Evidence

- **[Wireshark Interface](/home-lab-setup/Wazuh-SOC-Monitoring-Lab/images/wireshark.png)**
- **[Jira Ticketing](/home-lab-setup/Wazuh-SOC-Monitoring-Lab/images/jira.png)**
- **[Windows Agent Deployment](/home-lab-setup/Wazuh-SOC-Monitoring-Lab/images/windows-agent-enrollment.png)**

---

## 🎓 Career Impact

This lab showcases my ability to manage **resource-heavy security infrastructure**, perform **cross-tool correlation**, and maintain **operational discipline** through professional ticketing systems. It is a direct simulation of a junior SOC Analyst's daily environment.
