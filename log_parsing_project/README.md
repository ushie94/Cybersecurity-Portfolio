# Project: Correlating Windows & Netflow Logs for Brute Force Detection

TO BE EDITED AFTER LOG ANALYSIS IS COMPLETEED

## 1. Project Objective (The "Why")

- **Scenario:** Brute Force Attack Leading to Unauthorized Account Access.
- **Goal:** Demonstrate the ability to correlate host-based authentication logs with network flow data to identify an attacker's movement.
- **Why this matters:** Correlation provides a complete narrative of an attack, proving the ability to reconstruct an attack path beyond simple log parsing.

## 2. Tools & Technologies

- **Environment:** VSCode
- **Language:** Python
- **Libraries:** Pandas (for data manipulation/normalization)
- **Analysis:** Jupyter Notebooks
- **Version Control:** Git/GitHub

## 3. Methodology (The "How")

### A. Data Acquisition

- **Source:** Kaggle: Cyber-security Datasets by The Devastator
- **Data Types:** Windows Security Event Logs and Netflow Data

### B. Normalization Process

- **Challenge:** Datasets used inconsistent naming conventions (e.g., `IpAddress` vs `src_addr`).
- **Solution:** Python script normalizes all fields to a unified format (e.g., `source_ip`) to ensure consistency for future detection rules.

## 4. Analysis & Findings (The "So What?")

- **Observation:** [Insert identified Event IDs, e.g., 4625 (Failed Logon), 4624 (Successful Logon)]
- **Correlation:** [Describe how the Source_IP found in Windows logs links to specific network connections in Netflow logs]
- **Evidence:** [Insert placeholders for your charts/graphs/output here]

## 5. Next Steps / Future Scope

- **Current Status:** Transformation and Preparation (Stage 2)
- **Future Goal:** Transition to Detection Engineering (Stage 3) to ingest these findings into a SIEM (Wazuh/Elastic) and write automated detection rules.
