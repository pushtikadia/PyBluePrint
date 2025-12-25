import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from modules.brain import load_ai_engine, query_ai
from modules.inspector import get_deep_metrics, scan_security

# --- Page Config & Dark Theme ---
st.set_page_config(page_title="PyBlueprint Architect", page_icon="🏗️", layout="wide")

st.markdown("""
<style>
    /* Dark Theme Adjustments */
    .reportview-container { background: #0e1117; }
    .stTextArea textarea { background-color: #1f2937; color: #e5e7eb; border-radius: 5px; }
    .stMetric { background-color: #111827; padding: 15px; border-radius: 8px; border: 1px solid #374151; }
    h1, h2, h3 { color: #60a5fa; font-family: 'Segoe UI', sans-serif; }
    .stAlert { background-color: #1f2937; color: #e5e7eb; border: 1px solid #374151; }
</style>
""", unsafe_allow_html=True)

# --- Header ---
c1, c2 = st.columns([1, 10])
with c1:
    st.title("🏗️")
with c2:
    st.title("PyBlueprint: Architect Edition")
    st.caption("Advanced Static Analysis & Neural Interpretation Engine")

# --- Load AI Model ---
with st.sidebar:
    st.header("System Status")
    with st.status("Booting Neural Engine...", expanded=True):
        st.write("Loading CodeT5 Model...")
        tokenizer, model = load_ai_engine()
        st.write("Engine Online.")
    
    st.divider()
    st.info("Paste your Python code in the main window to generate an architectural blueprint.")

# --- Main Input ---
default_code = """import os

def database_connect(user, password):
    # This is a dummy function to test the scanner
    api_key = "12345-SECRET"  # Hardcoded secret check
    
    if user == "admin":
        cmd = f"echo Hello {user}"
        eval(cmd)  # Dangerous eval check
        return True
    elif user == "guest":
        return False
    else:
        # Complex nested logic to test Complexity score
        for i in range(10):
            if i % 2 == 0:
                print("Even")
            else:
                print("Odd")
        return None
"""

code_input = st.text_area("Source Code Input", height=300, value=default_code)

if st.button("Generate Blueprint ⚡", type="primary", use_container_width=True):
    if not code_input.strip():
        st.error("Input buffer empty.")
        st.stop()

    # --- Run Analysis ---
    with st.spinner("Analyzing Architecture..."):
        metrics = get_deep_metrics(code_input)
        security_issues = scan_security(code_input)
        ai_summary = query_ai(code_input, tokenizer, model, "summarize")

    if not metrics:
        st.error("Syntax Error: The code provided is not valid Python.")
        st.stop()

    # --- Layout: 2 Columns ---
    col_left, col_right = st.columns([1, 1])

    # --- LEFT: METRICS ---
    with col_left:
        st.subheader("1. Code Health Metrics")
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Maintainability (MI)", f"{metrics['maintainability_index']}", 
             delta="Healthy" if metrics['maintainability_index'] > 75 else "-Risk",
             help="0-100 Score. Higher is better.")
        
        m2.metric("Cyclomatic Complexity", metrics['cyclomatic_complexity'], 
             delta="High" if metrics['cyclomatic_complexity'] > 10 else "Normal", delta_color="inverse",
             help="Number of independent paths. Lower is better.")
        
        m3.metric("Mental Effort", int(metrics['effort']), help="Halstead Effort Score")

        st.subheader("2. Neural Explanation")
        st.success(f"**AI Analysis:** {ai_summary}")

    # --- RIGHT: VISUALIZATION ---
    with col_right:
        st.subheader("3. Risk Radar")
        
        # Normalize metrics for the chart
        mi_score = min(metrics['maintainability_index'], 100)
        # Invert CC (Lower is better, so 100 - (CC*5))
        cc_score = max(100 - (metrics['cyclomatic_complexity'] * 5), 0)
        # Security Score (100 - 25 points per issue)
        sec_score = max(100 - (len(security_issues) * 25), 0)

        fig = go.Figure(data=go.Scatterpolar(
            r=[mi_score, cc_score, sec_score, mi_score],
            theta=['Maintainability', 'Structural Simplicity', 'Security', 'Maintainability'],
            fill='toself',
            name='Health Profile',
            line_color='#60a5fa',
            fillcolor='rgba(96, 165, 250, 0.3)'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100], showticklabels=False),
                bgcolor='#111827'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=40, r=40, t=20, b=20),
            font=dict(color="white")
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # --- BOTTOM: SECURITY & REFACTORING ---
    c_sec, c_ref = st.columns(2)

    with c_sec:
        st.subheader("🛡️ Security Audit")
        if security_issues:
            for issue in security_issues:
                st.error(issue)
        else:
            st.success("✅ No static vulnerabilities detected.")

    with c_ref:
        st.subheader("💡 Architect's Advice")
        if metrics['cyclomatic_complexity'] > 8:
            st.warning("High Complexity: Consider breaking this function into smaller sub-functions.")
        elif metrics['maintainability_index'] < 60:
            st.warning("Low Maintainability: Code is dense. Add comments and meaningful variable names.")
        else:

            st.info("Structure looks solid. Ready for deployment.")
