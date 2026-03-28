# 🛡️ Hybrid SOC Lab Infrastructure & Technical Documentation

## 📌 Project Overview

This project documents the deployment of a professional-grade, multi-tier Security Operations Center (SOC) laboratory. The environment is designed for threat simulation, log analysis, and defensive posture testing using a **Bastion Host (Jump Box)** architecture.

## 🏗️ Network Architecture

- **Host:** Windows 11 (Physical Workstation)
- **Tier 1 (Jump Box):** Ubuntu Desktop 22.04 LTS (Primary Management GUI)
- **Tier 2 (Production):** Ubuntu Server 22.04 LTS (Headless Security Tool Hosting)
- **Tier 3 (Target):** Windows 10 Pro (Analysis & Vulnerability Endpoint)

## 🛠️ Technical Implementation & Troubleshooting

This project wasn't just about clicking "Install." It involved solving real-world infrastructure hurdles:

- **Headless Data Migration:** Overcame Guest-to-Host integration failures (VirtualBox Clipboard) by pivoting to a professional **SCP (Secure Copy Protocol)** and **SSH** workflow.
- **Service Hardening:** Identified and resolved "Connection Refused" errors by deploying and configuring `openssh-server` on the Ubuntu endpoints.
- **Package Management:** Resolved `dpkg` lock-frontend issues and naming conflicts (`openssh` vs `openssl`) to ensure 100% system uptime.
- **Documentation Governance:** Authored a comprehensive Standard Operating Procedure (SOP) with integrity watermarking to ensure repeatable lab builds.

## 📜 Standard Operating Procedure (SOP)

The full technical breakdown, including network diagrams and hardening steps, is available here:
👉 **[View the Full SOP (PDF)](https://github.com/ushie94/Cybersecurity-Portfolio/blob/main/home-lab-setup/Victor_Ushie_SOC_SOCP.pdf)**

## 🚀 Key Skills Demonstrated

- **Linux Administration:** Advanced CLI, SSH Tunneling, and Path Troubleshooting.
- **Network Security:** ICMP Validation, Secure Remote Access, and Port Management.
- **Problem Solving:** Ability to pivot from GUI-based tools to CLI-based networking solutions under pressure.
