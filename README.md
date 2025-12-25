# 🏗️ PyBluePrint

> **The Software Physics & Neural Architecture Engine.**
> *Decode Complexity. Visualize Technical Debt. Secure Your Logic.*

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
![AI](https://img.shields.io/badge/Neural_Engine-CodeT5-purple?style=for-the-badge)
![Physics](https://img.shields.io/badge/Metric-Halstead_Physics-success?style=for-the-badge)

**PyBlueprint** is an advanced static analysis dashboard designed for software architects and senior developers. Unlike standard linters that merely check syntax, PyBlueprint combines **Neural Intelligence (AI)** with **Halstead Software Physics** to provide a deep, structural health scan of your Python codebase.

It answers the critical question: *"Is this code maintainable, secure, and logically sound?"*

---

## ⚡ Key Capabilities

### 📡 The Risk Radar
A unique, real-time visualization (powered by **Plotly**) that triangulates code health across three vectors:
* **Maintainability:** How hard is it to modify this code later?
* **Structural Simplicity:** Is the Cyclomatic Complexity too high?
* **Security:** Are there logic vulnerabilities?

### 🧠 Neural Interpretation Engine
Leverages the **Salesforce CodeT5** transformer model to:
* Generate "Technical Briefs" (plain-English summaries of complex logic).
* Provide AI-driven **refactoring strategies** to reduce nesting and improve readability.

### ⚛️ Halstead Software Physics
Goes beyond line counts to calculate scientific metrics:
* **Program Volume (Bits):** The information density of your logic.
* **Mental Effort:** The cognitive load required for a human to understand the algorithm.
* **Difficulty:** The statistical probability of introducing errors during changes.

### 🛡️ Security Sentry
An AST-based static scanner that proactively detects:
* Hardcoded secrets (API Keys, Passwords, Tokens).
* Dangerous execution vectors (`eval()`, `exec()`, `os.system`).

---

## 🛠️ Technical Stack

* **Core:** Python 3.x
* **Interface:** Streamlit (Custom "Blueprint" Dark Mode)
* **Visualization:** Plotly Interactive Radar Charts
* **AI Backend:** Hugging Face Transformers (`Salesforce/codet5-base-multi-sum`)
* **Static Analysis:** Radon & Python AST

---

## 🚀 Deployment Guide

1. InstallationClone the repo and install the required scientific and AI libraries.
   git clone [https://github.com/yourusername/PyBlueprint.git](https://github.com/yourusername/PyBlueprint.git)
   cd PyBlueprint
   pip install -r requirements.txt
   
2. Launch the Architect Engine
   Start the local server. The AI model (approx. 500MB) will auto-download on the first run.

   streamlit run app.py
   
3. Usage
   Paste Code: Input raw Python source code into the dashboard buffer.
   Generate Blueprint: Click the analysis trigger.
   Review:
   - Check the Radar Chart for immediate health visualization.
   - Read the Neural Brief for logic verification.
   - Consult the Security Audit for vulnerabilities.

## 📂 Repository Structure

```text
PyBlueprint_v2/
├── app.py                  # 🖥️ The Architect Dashboard entry point
├── requirements.txt        # 📦 ML and Analytics dependencies
└── modules/
    ├── brain.py            # 🧠 AI Logic (Neural Network Interface)
    └── inspector.py        # 🕵️ Static Analysis & Security Scanner

```
---

<p align="center">
  PyBluePrint - Created by <a href="https://github.com/pushtikadia"><b>Pushti Kadia</b></a>
</p>




