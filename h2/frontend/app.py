import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import random

st.set_page_config(
    page_title="FakeBuster AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MODERN GLASSMORPHISM CYBERSECURITY CSS ---
st.markdown("""
<style>
    /* Simplistic Card Layout */
    div[data-testid="stVerticalBlock"] > div > div > div[data-testid="stVerticalBlock"] {
        background-color: transparent;
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    }

    /* Reduce Font Sizes */
    div[data-testid="stMetricValue"] {
        font-size: 2rem !important;
    }
    
    div[data-testid="stMetricLabel"] {
        font-size: 1rem !important;
    }

    h1 {
        font-size: 2.2rem !important;
        margin-bottom: 1.5rem !important;
    }

    h3 {
        font-size: 1.3rem !important;
    }
    
    /* Responsive Content Boxes */
    .status-box {
        background: rgba(128, 128, 128, 0.05); 
        padding: 16px; 
        border-radius: 8px; 
        border: 1px solid rgba(128, 128, 128, 0.2); 
    }
    
    .status-text-row {
        margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)

# --- CONFIGURATION ---
API_BASE_URL = "http://localhost:8000"

def local_css(file_name):
    # Fallback to load css if we ever need external css file
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except Exception:
        pass

# --- API HELPER FUNCTIONS ---
def fetch_api(endpoint, method="POST", data=None, files=None):
    """Generic API fetcher to handle backend requests"""
    url = f"{API_BASE_URL}{endpoint}"
    try:
        if method == "POST":
            if files:
                response = requests.post(url, files=files, timeout=10)
            else:
                response = requests.post(url, json=data, timeout=10)
        elif method == "GET":
             response = requests.get(url, timeout=10)
             
        response.raise_for_status()
        return response.json()
    except Exception as e:
        # Fallback dummy data for visual testing during development
        st.sidebar.error(f"API Error: {e}")
        return None

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/144/null/cyber-security.png", width=80)
    st.title("FakeBuster AI")
    st.caption("Advanced Threat Defense Platform")
    st.markdown("---")
    
    page = st.radio(
        "NAVIGATION MAP",
        [
            "⚡ System Dashboard",
            "📧 Email Analysis",
            "🔗 URL Scanner",
            "📸 Deepfake Detection",
            "🛡️ Trust Score Analysis",
            "📈 System Analytics",
            "🔐 Authentication"
        ],
        label_visibility="hidden"
    )
    
    st.markdown("---")
    st.markdown("### SYSTEM STATUS")
    
    # Fake terminal effect for sidebar
    with st.container():
        st.markdown("""
        <div class="status-box">
            <div class="status-text-row">> Neural Engine: <b>ONLINE</b></div>
            <div class="status-text-row">> Threat Intel: <b>SYNCHED</b></div>
            <div class="status-text-row">> Active Scans: 23</div>
            <div class="status-text-row">> System Secure</div>
        </div>
        """, unsafe_allow_html=True)

# Main App Routing
if page == "⚡ System Dashboard":
    st.markdown("<h1>⚡ Global Defense Matrix</h1>", unsafe_allow_html=True)
    st.write("Real-time threat detection and mitigation overview.")
    
    # KPIs
    st.markdown("<br>", unsafe_allow_html=True)
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric(label="TOTAL SCANS", value="14,293", delta="↑ 12% vs last week")
    with kpi2:
        st.metric(label="THREATS BLOCKED", value="3,102", delta="↑ 5%", delta_color="inverse")
    with kpi3:
        st.metric(label="DEEPFAKES IDENTIFIED", value="184", delta="↓ 2%", delta_color="normal")
    with kpi4:
        st.metric(label="AVERAGE TRUST SCORE", value="82.4", delta="↑ 1.2%")
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Charts Row
    chart_col1, chart_col2 = st.columns([2, 1])
    
    with chart_col1:
        st.markdown("<h3>🎯 Threat Detection Activity (24h)</h3>", unsafe_allow_html=True)
        # Dummy data for chart
        hours = list(range(24))
        phishing = [random.randint(10, 50) for _ in hours]
        malware = [random.randint(5, 30) for _ in hours]
        df_activity = pd.DataFrame({
            "Hour": hours,
            "Phishing": phishing,
            "Malicious URLs": malware
        })
        
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=df_activity['Hour'], y=df_activity['Phishing'], 
                                  mode='lines+markers', name='Phishing Emails'))
        fig1.add_trace(go.Scatter(x=df_activity['Hour'], y=df_activity['Malicious URLs'], 
                                  mode='lines+markers', name='Malicious URLs'))
        
        fig1.update_layout(
            margin=dict(l=0, r=0, t=20, b=0),
            legend=dict(orientation="h", yanchor="bottom", y=1.05, xanchor="right", x=1),
            xaxis=dict(title="Hour of Day"),
            yaxis=dict(title="Threats Detected")
        )
        st.plotly_chart(fig1, width="stretch")
        
    with chart_col2:
        st.markdown("<h3>🛡️ Threat Distribution</h3>", unsafe_allow_html=True)
        labels = ['Phishing', 'Malicious URLs', 'Deepfakes', 'Safe']
        values = [35, 25, 10, 30]
        fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.65)])
        fig2.update_traces(hoverinfo='label+percent', textinfo='none')
        fig2.update_layout(
            margin=dict(l=20, r=20, t=20, b=20),
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig2, width="stretch")
        
    # Live Activity Feed
    st.markdown("<h3>📡 Live Activity Feed</h3>", unsafe_allow_html=True)
    
    feed_html = """
    <div class="status-box">
        <div class="status-text-row"><b>[18:42:05]</b> Scanned url: security-update-apple.net <b>[BLOCKED - Phishing]</b></div>
        <div class="status-text-row"><b>[18:41:30]</b> Analysed email: "Urgent: Invoice Overdue" <b>[FLAGGED - Suspicious]</b></div>
        <div class="status-text-row"><b>[18:40:12]</b> Scanned video: CEO_announcement.mp4 <b>[CLEAN - Real]</b></div>
        <div class="status-text-row"><b>[18:39:55]</b> Scanned url: github.com/microsoft <b>[CLEAN - Safe]</b></div>
        <div class="status-text-row"><b>[18:38:20]</b> Scanned file: resume_2026.pdf <b>[BLOCKED - Malware]</b></div>
    </div>
    """
    st.markdown(feed_html, unsafe_allow_html=True)
elif page == "📧 Email Analysis":
    st.markdown("<h1>📧 Neural Email Inspection</h1>", unsafe_allow_html=True)
    st.write("Deep semantic analysis of email content to detect phishing and social engineering.")
    
    email_content = st.text_area("Paste email content or headers here for analysis:", height=250, 
                                 placeholder="Dear Customer,\n\nYour account has been suspended...")
                                 
    if st.button("RUN DEEP SCAN"):
        if not email_content.strip():
            st.warning("⚠️ Please provide email content for analysis.")
        else:
            with st.spinner("Analyzing semantics and linguistic patterns..."):
                # Call to backend API
                data = fetch_api("/detect/email", data={"content": email_content})
                
                # Mock processing if backend fails
                if not data:
                    time.sleep(1.5)
                    data = {
                        "risk_score": random.randint(75, 95),
                        "risk_level": "CRITICAL",
                        "suspicious_keywords": ["urgent", "account suspended", "verify", "login"],
                        "explanation": "High linguistic urgency detected combined with an imperative call to action affecting account security. The grammatical structure matches known credential harvesting templates."
                    }
                
                score = data.get("risk_score", 0)
                level = data.get("risk_level", "UNKNOWN")
                
                st.markdown("<br>", unsafe_allow_html=True)
                st.write("### ANALYSIS RESULTS")
                
                res_col1, res_col2 = st.columns([1, 2])
                
                with res_col1:
                    st.metric("THREAT PROBABILITY", f"{score}%")
                    if score > 70:
                        st.error(f"RISK LEVEL: {level}")
                    elif score > 30:
                        st.warning(f"RISK LEVEL: {level}")
                    else:
                        st.success(f"RISK LEVEL: {level}")
                        
                with res_col2:
                    st.markdown("#### 🧠 AI Explanation")
                    st.info(data.get("explanation", "Analysis complete."))
                    
                    st.markdown("#### 🚩 Flagged Vectors")
                    for word in data.get("suspicious_keywords", []):
                        st.markdown(f"• `{word}`")

elif page == "🔗 URL Scanner":
    st.markdown("<h1>🔗 Quantum Link Analysis</h1>", unsafe_allow_html=True)
    st.write("Real-time inspection of domains, redirects, and SSL signatures for malicious intent.")
    
    url_input = st.text_input("Enter target URL:", placeholder="https://example.com/login")
    
    if st.button("INITIATE SCAN"):
        if not url_input.strip():
            st.warning("⚠️ Please enter a URL.")
        else:
            with st.spinner("Inspecting domain reputation and payload vectors..."):
                data = fetch_api("/detect/url", data={"url": url_input})
                
                if not data:
                    time.sleep(1.2)
                    data = {
                        "risk_score": random.randint(60, 99),
                        "ssl_status": "Invalid / Self-Signed",
                        "domain_age": "2 Days",
                        "threat_level": "HIGH",
                        "patterns_detected": ["Typosquatting", "Hidden redirect", "Freshly registered domain"]
                    }
                    
                score = data.get("risk_score", 0)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                t_col1, t_col2, t_col3 = st.columns(3)
                t_col1.metric("DOMAIN RISK", f"{score}%")
                t_col2.metric("SSL SIGNATURE", data.get("ssl_status", "Unknown"))
                t_col3.metric("DOMAIN AGE", data.get("domain_age", "Unknown"))
                
                if score > 70:
                    st.error(f"THREAT LEVEL: {data.get('threat_level', 'HIGH')}")
                elif score > 30:
                    st.warning(f"THREAT LEVEL: {data.get('threat_level', 'MEDIUM')}")
                else:
                    st.success(f"THREAT LEVEL: {data.get('threat_level', 'LOW')}")
                    
                st.markdown("### 🔍 Extracted Threat Patterns")
                for pattern in data.get("patterns_detected", []):
                    st.markdown(f"- **{pattern}**")
elif page == "📸 Deepfake Detection":
    st.markdown("<h1>📸 Visual Authenticity Engine</h1>", unsafe_allow_html=True)
    st.write("Advanced biometric and artifact analysis to detect AI-generated manipulation.")
    
    uploaded_file = st.file_uploader("Upload Image or Video (MP4, JPG, PNG)", type=["mp4", "jpg", "png", "jpeg"])
    
    if st.button("INITIATE MEDIA SCAN"):
        if uploaded_file is None:
            st.warning("⚠️ Please upload a media file.")
        else:
            with st.spinner("Extracting frames and running DeepFake detection models..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                data = fetch_api("/detect/deepfake", files=files)
                
                if not data:
                    time.sleep(2)
                    data = {
                        "authenticity_score": random.randint(15, 85),
                        "label": "Deepfake Detected" if random.choice([True, False]) else "Authentic Media",
                        "anomalies": ["Inconsistent blinking pattern", "Unnatural facial boundary reflections"],
                        "frame_scores": [random.randint(10, 45) for _ in range(30)]
                    }
                    
                score = data.get("authenticity_score", 0)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    st.metric("AUTHENTICITY SCORE", f"{score}%")
                    if score < 40:
                        st.error("🚨 RESULT: DEEPFAKE DETECTED")
                    elif score < 75:
                        st.warning("⚠️ RESULT: SUSPICIOUS MEDIA")
                    else:
                        st.success("✅ RESULT: VERIFIED AUTHENTIC")
                        
                with col2:
                    st.markdown("### 📊 Frame-by-Frame Authenticity Variance")
                    frames = data.get("frame_scores", [])
                    if frames:
                        df_frames = pd.DataFrame({"Frame": range(len(frames)), "Authenticity %": frames})
                        fig = px.area(df_frames, x="Frame", y="Authenticity %")
                        fig.update_layout(
                            margin=dict(l=0, r=0, t=10, b=0),
                            yaxis=dict(range=[0, 100])
                        )
                        st.plotly_chart(fig, width="stretch")
                        
                st.markdown("### 🔎 Detected Anomalies")
                for anomaly in data.get("anomalies", []):
                    st.markdown(f"- ⚠️ {anomaly}")

elif page == "🛡️ Trust Score Analysis":
    st.markdown("<h1>🛡️ Global Trust Profiling</h1>", unsafe_allow_html=True)
    st.write("Aggregated security posture based on system-wide telemetry.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_gauge, col_recs = st.columns([1, 1])
    
    with col_gauge:
        # Fetch global trust score
        data = fetch_api("/trustscore", method="GET")
        if not data:
            data = {"overall_trust_score": 68.5}
            
        trust_score = data.get("overall_trust_score", 0)
        
        # Determine color
        bar_color = "#ef4444" if trust_score < 40 else "#f59e0b" if trust_score < 80 else "#10b981"
        
        # Gauge Chart
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = trust_score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Organization Trust Index", 'font': {'size': 20}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1},
                'bar': {'color': bar_color, 'thickness': 0.25},
                'bgcolor': "rgba(128, 128, 128, 0.1)",
                'borderwidth': 0,
                'steps': [
                    {'range': [0, 40], 'color': 'rgba(239, 68, 68, 0.15)'},
                    {'range': [40, 80], 'color': 'rgba(245, 158, 11, 0.15)'},
                    {'range': [80, 100], 'color': 'rgba(16, 185, 129, 0.15)'}],
                'threshold': {
                    'line': {'color': "gray", 'width': 3},
                    'thickness': 0.75,
                    'value': trust_score}
            }
        ))
        fig.update_layout(
            margin=dict(l=20, r=20, t=50, b=20)
        )
        st.plotly_chart(fig, width="stretch")
        
    with col_recs:
        st.markdown("<h3>💡 Tactical Recommendations</h3>", unsafe_allow_html=True)
        st.markdown("""
        <div class="status-box">
            <p style="margin-bottom: 15px;">🔴 <b>Critical Action Required:</b> Review flagged phishing campaigns targeting the Finance department.</p>
            <p style="margin-bottom: 15px;">🟡 <b>Warning:</b> 15% increase in suspicious URL redirects compared to last week.</p>
            <p style="margin-bottom: 15px;">🟢 <b>System Status:</b> Endpoint detection agents are fully active and updating signatures normally.</p>
            <hr style="border-color: rgba(128, 128, 128, 0.2); margin: 20px 0;">
            <p style="font-size: 0.9em; font-style: italic;">Last updated: 2 mins ago</p>
        </div>
        """, unsafe_allow_html=True)
elif page == "📈 System Analytics":
    st.markdown("<h1>📈 Threat Intelligence Analytics</h1>", unsafe_allow_html=True)
    st.write("Deep dive into historical data, system performance, and threat landscapes.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Date Range Selector
    dates = st.date_input("Analysis Window", [])
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.markdown("<h3>📊 Detection Efficacy Trends</h3>", unsafe_allow_html=True)
        # Dummy data
        dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
        df_trends = pd.DataFrame({
            "Date": dates,
            "Emails": [random.randint(50, 150) for _ in range(30)],
            "URLs": [random.randint(80, 200) for _ in range(30)],
            "Deepfakes": [random.randint(5, 20) for _ in range(30)]
        })
        
        fig = px.line(df_trends, x="Date", y=["Emails", "URLs", "Deepfakes"])
        fig.update_layout(
            margin=dict(l=0, r=0, t=20, b=0),
            legend=dict(title=None, orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            xaxis=dict(title="Date"),
            yaxis=dict(title="Count")
        )
        fig.update_traces(line=dict(width=3))
        st.plotly_chart(fig, width="stretch")
        
    with chart_col2:
        st.markdown("<h3>🎯 Severity Distribution</h3>", unsafe_allow_html=True)
        # Dummy Data
        df_sev = pd.DataFrame({
            "Severity": ["Critical", "High", "Medium", "Low"],
            "Count": [120, 350, 800, 1500]
        })
        
        fig2 = px.bar(df_sev, x="Severity", y="Count", color="Severity")
                     
        fig2.update_layout(
            margin=dict(l=0, r=0, t=20, b=0)
        )
        st.plotly_chart(fig2, width="stretch")
        
    st.markdown("<h3>🗺️ Global Attack Origins (Simulated Heatmap)</h3>", unsafe_allow_html=True)
    # Dummy geographical data
    df_map = pd.DataFrame({
        "lat": [random.uniform(-90, 90) for _ in range(100)],
        "lon": [random.uniform(-180, 180) for _ in range(100)],
        "intensity": [random.randint(1, 10) for _ in range(100)]
    })
    
    st.map(df_map, size="intensity")

elif page == "🔐 Authentication":
    import streamlit.components.v1 as components
    
    st.markdown('''
        <style>
            .block-container { padding: 0rem !important; max-width: 100% !important; }
            header { visibility: hidden; }
        </style>
    ''', unsafe_allow_html=True)
    
    html_code = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Auth — Lumina</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --ink: #0d0d12;
    --ink-soft: #1a1a24;
    --ink-muted: #2a2a38;
    --gold: #c9a96e;
    --gold-pale: #e8d5b0;
    --gold-dim: #7a5e34;
    --cream: #f5f0e8;
    --cream-dim: #b0a898;
    --cream-ghost: rgba(245, 240, 232, 0.06);
    --border: rgba(201, 169, 110, 0.18);
    --border-soft: rgba(245, 240, 232, 0.08);
  }

  html, body {
    height: 100%;
    font-family: 'DM Sans', sans-serif;
    background: var(--ink);
    color: var(--cream);
    overflow: hidden;
  }

  .wrapper {
    display: flex;
    height: 100vh;
  }

  /* ── LEFT PANEL ── */
  .panel-art {
    flex: 0 0 42%;
    position: relative;
    background: var(--ink-soft);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .panel-art::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
      radial-gradient(ellipse 60% 50% at 30% 35%, rgba(201,169,110,0.12) 0%, transparent 70%),
      radial-gradient(ellipse 40% 60% at 70% 70%, rgba(100,80,160,0.10) 0%, transparent 70%);
  }

  /* Decorative geometric SVG */
  .art-svg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    opacity: 0.55;
  }

  .art-content {
    position: relative;
    z-index: 2;
    text-align: center;
    padding: 3rem;
  }

  .brand-logo {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.6rem;
    font-weight: 300;
    letter-spacing: 0.22em;
    color: var(--gold-pale);
    text-transform: uppercase;
    line-height: 1;
    margin-bottom: 1rem;
  }

  .brand-tagline {
    font-size: 0.78rem;
    font-weight: 300;
    letter-spacing: 0.35em;
    color: var(--cream-dim);
    text-transform: uppercase;
  }

  .art-divider {
    width: 48px;
    height: 1px;
    background: var(--gold);
    margin: 2.2rem auto;
    opacity: 0.5;
  }

  .art-quote {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-size: 1.15rem;
    line-height: 1.7;
    color: var(--cream-dim);
    max-width: 280px;
    margin: 0 auto;
  }

  .art-quote cite {
    display: block;
    font-style: normal;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--gold-dim);
    margin-top: 1.2rem;
  }

  /* Floating orbs */
  .orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(40px);
    animation: drift 8s ease-in-out infinite alternate;
  }
  .orb-1 { width: 180px; height: 180px; background: rgba(201,169,110,0.12); top: 10%; left: 5%; animation-delay: 0s; }
  .orb-2 { width: 120px; height: 120px; background: rgba(130,100,200,0.10); bottom: 15%; right: 8%; animation-delay: -3s; }
  .orb-3 { width: 90px; height: 90px; background: rgba(201,169,110,0.08); top: 55%; left: 35%; animation-delay: -5s; }

  @keyframes drift {
    from { transform: translate(0, 0) scale(1); }
    to { transform: translate(20px, -15px) scale(1.08); }
  }

  /* ── RIGHT PANEL ── */
  .panel-form {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    background: var(--ink);
    position: relative;
    overflow: hidden;
  }

  .panel-form::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 50% 60% at 60% 40%, rgba(201,169,110,0.04) 0%, transparent 70%);
  }

  .form-card {
    position: relative;
    z-index: 2;
    width: 100%;
    max-width: 400px;
  }

  /* Tab switcher */
  .tab-row {
    display: flex;
    gap: 0;
    margin-bottom: 2.8rem;
    border-bottom: 1px solid var(--border-soft);
  }

  .tab-btn {
    flex: 1;
    background: none;
    border: none;
    border-bottom: 2px solid transparent;
    margin-bottom: -1px;
    padding: 0 0 1rem;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.8rem;
    font-weight: 400;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--cream-dim);
    cursor: pointer;
    transition: color 0.3s, border-color 0.3s;
  }

  .tab-btn.active {
    color: var(--gold);
    border-bottom-color: var(--gold);
  }

  /* Form heading */
  .form-heading {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.2rem;
    font-weight: 300;
    color: var(--cream);
    line-height: 1.2;
    margin-bottom: 0.5rem;
  }

  .form-sub {
    font-size: 0.82rem;
    color: var(--cream-dim);
    margin-bottom: 2.4rem;
    line-height: 1.6;
  }

  /* Views */
  .view { display: none; animation: fadeIn 0.4s ease; }
  .view.active { display: block; }
  @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

  /* Inputs */
  .field {
    margin-bottom: 1.2rem;
  }

  .field label {
    display: block;
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--cream-dim);
    margin-bottom: 0.5rem;
  }

  .input-wrap {
    position: relative;
  }

  .input-wrap input {
    width: 100%;
    background: var(--cream-ghost);
    border: 1px solid var(--border);
    border-radius: 3px;
    padding: 0.85rem 1rem;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    font-weight: 300;
    color: var(--cream);
    outline: none;
    transition: border-color 0.25s, background 0.25s;
    letter-spacing: 0.03em;
  }

  .input-wrap input::placeholder { color: rgba(176,168,152,0.4); }

  .input-wrap input:focus {
    border-color: rgba(201,169,110,0.5);
    background: rgba(245,240,232,0.09);
  }

  /* Row for name fields */
  .field-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
  }

  /* Checkbox row */
  .check-row {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin-bottom: 1.8rem;
  }

  .check-row input[type="checkbox"] {
    width: 15px; height: 15px;
    accent-color: var(--gold);
    cursor: pointer;
  }

  .check-row span {
    font-size: 0.78rem;
    color: var(--cream-dim);
  }

  .check-row a { color: var(--gold); text-decoration: none; }
  .check-row a:hover { text-decoration: underline; }

  /* Submit button */
  .btn-primary {
    width: 100%;
    background: transparent;
    border: 1px solid var(--gold);
    border-radius: 3px;
    padding: 0.9rem 1rem;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem;
    font-weight: 400;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: var(--gold);
    cursor: pointer;
    transition: background 0.25s, color 0.25s;
    margin-bottom: 1.8rem;
  }

  .btn-primary:hover {
    background: var(--gold);
    color: var(--ink);
  }

  /* Divider */
  .or-line {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
  }

  .or-line::before, .or-line::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border-soft);
  }

  .or-line span {
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--cream-dim);
  }

  /* Social buttons */
  .social-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.8rem;
    margin-bottom: 2rem;
  }

  .btn-social {
    background: var(--cream-ghost);
    border: 1px solid var(--border-soft);
    border-radius: 3px;
    padding: 0.7rem 1rem;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.78rem;
    color: var(--cream-dim);
    cursor: pointer;
    transition: background 0.2s, border-color 0.2s, color 0.2s;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    letter-spacing: 0.05em;
  }

  .btn-social:hover {
    background: rgba(245,240,232,0.1);
    border-color: rgba(201,169,110,0.3);
    color: var(--cream);
  }

  .btn-social svg { width: 16px; height: 16px; flex-shrink: 0; }

  /* Forgot */
  .forgot-row {
    text-align: right;
    margin-bottom: 1.5rem;
    margin-top: -0.6rem;
  }

  .forgot-row a {
    font-size: 0.73rem;
    color: var(--gold-dim);
    text-decoration: none;
    letter-spacing: 0.05em;
    transition: color 0.2s;
  }

  .forgot-row a:hover { color: var(--gold); }

  /* Password strength */
  .strength-bar {
    height: 2px;
    margin-top: 6px;
    border-radius: 2px;
    background: var(--border-soft);
    overflow: hidden;
    display: none;
  }

  .strength-bar .fill {
    height: 100%;
    transition: width 0.4s, background 0.4s;
    border-radius: 2px;
  }

  .strength-label {
    font-size: 0.67rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-top: 4px;
    display: none;
  }

  /* Bottom note */
  .bottom-note {
    text-align: center;
    font-size: 0.75rem;
    color: var(--cream-dim);
  }

  .bottom-note a { color: var(--gold); text-decoration: none; cursor: pointer; }
  .bottom-note a:hover { text-decoration: underline; }

  /* Responsive */
  @media (max-width: 700px) {
    .panel-art { display: none; }
  }
</style>
</head>
<body>

<div class="wrapper">

  <!-- LEFT: Art Panel -->
  <div class="panel-art">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>

    <svg class="art-svg" viewBox="0 0 420 700" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- Concentric arcs top-right -->
      <circle cx="400" cy="80" r="180" stroke="rgba(201,169,110,0.12)" stroke-width="1"/>
      <circle cx="400" cy="80" r="130" stroke="rgba(201,169,110,0.1)" stroke-width="1"/>
      <circle cx="400" cy="80" r="80" stroke="rgba(201,169,110,0.14)" stroke-width="1"/>
      <!-- Large diagonal lines -->
      <line x1="0" y1="250" x2="420" y2="500" stroke="rgba(245,240,232,0.05)" stroke-width="1"/>
      <line x1="0" y1="290" x2="420" y2="540" stroke="rgba(245,240,232,0.04)" stroke-width="1"/>
      <line x1="0" y1="330" x2="420" y2="580" stroke="rgba(245,240,232,0.03)" stroke-width="1"/>
      <!-- Bottom left arcs -->
      <circle cx="20" cy="680" r="200" stroke="rgba(130,100,200,0.10)" stroke-width="0.8"/>
      <circle cx="20" cy="680" r="150" stroke="rgba(130,100,200,0.08)" stroke-width="0.8"/>
      <circle cx="20" cy="680" r="100" stroke="rgba(130,100,200,0.07)" stroke-width="0.8"/>
      <!-- Center diamond -->
      <polygon points="210,280 240,310 210,340 180,310" stroke="rgba(201,169,110,0.22)" stroke-width="1" fill="none"/>
      <polygon points="210,260 260,310 210,360 160,310" stroke="rgba(201,169,110,0.12)" stroke-width="0.8" fill="none"/>
      <!-- Small cross -->
      <line x1="210" y1="300" x2="210" y2="322" stroke="rgba(201,169,110,0.4)" stroke-width="1"/>
      <line x1="199" y1="311" x2="221" y2="311" stroke="rgba(201,169,110,0.4)" stroke-width="1"/>
      <!-- Dot grid bottom-right -->
      <circle cx="320" cy="560" r="1.5" fill="rgba(201,169,110,0.25)"/>
      <circle cx="340" cy="560" r="1.5" fill="rgba(201,169,110,0.25)"/>
      <circle cx="360" cy="560" r="1.5" fill="rgba(201,169,110,0.25)"/>
      <circle cx="380" cy="560" r="1.5" fill="rgba(201,169,110,0.25)"/>
      <circle cx="320" cy="580" r="1.5" fill="rgba(201,169,110,0.20)"/>
      <circle cx="340" cy="580" r="1.5" fill="rgba(201,169,110,0.20)"/>
      <circle cx="360" cy="580" r="1.5" fill="rgba(201,169,110,0.20)"/>
      <circle cx="380" cy="580" r="1.5" fill="rgba(201,169,110,0.20)"/>
      <circle cx="320" cy="600" r="1.5" fill="rgba(201,169,110,0.15)"/>
      <circle cx="340" cy="600" r="1.5" fill="rgba(201,169,110,0.15)"/>
      <circle cx="360" cy="600" r="1.5" fill="rgba(201,169,110,0.15)"/>
      <circle cx="380" cy="600" r="1.5" fill="rgba(201,169,110,0.15)"/>
    </svg>

    <div class="art-content">
      <div class="brand-logo">FakeBuster AI</div>
      <div class="brand-tagline">Design Studio</div>
      <div class="art-divider"></div>
      <p class="art-quote">
        "Design is not just what it looks like. Design is how it works."
        <cite>— Steve Jobs</cite>
      </p>
    </div>
  </div>

  <!-- RIGHT: Form Panel -->
  <div class="panel-form">
    <div class="form-card">

      <!-- Tab Switcher -->
      <div class="tab-row">
        <button class="tab-btn active" onclick="switchTab('signin')">Sign In</button>
        <button class="tab-btn" onclick="switchTab('signup')">Create Account</button>
      </div>

      <!-- ── SIGN IN VIEW ── -->
      <div id="view-signin" class="view active">
        <h1 class="form-heading">Welcome<br>back.</h1>
        <p class="form-sub">Sign in to continue to your workspace.</p>

        <div class="field">
          <label>Email address</label>
          <div class="input-wrap">
            <input type="email" id="signin-email" placeholder="you@example.com" autocomplete="email">
          </div>
        </div>

        <div class="field">
          <label>Password</label>
          <div class="input-wrap">
            <input type="password" id="signin-password" placeholder="••••••••" autocomplete="current-password">
          </div>
        </div>

        <div class="forgot-row"><a href="#">Forgot password?</a></div>
        <div id="signin-error" style="color: #e57373; font-size: 0.8rem; margin-bottom: 1rem; display: none;"></div>
        <div id="signin-success" style="color: #66bb6a; font-size: 0.8rem; margin-bottom: 1rem; display: none;">Successfully logged in! Returning to dashboard...</div>

        <button class="btn-primary" onclick="handleSignIn()">Continue</button>

        <div class="or-line"><span>or</span></div>

        <div class="social-row">
          <button class="btn-social">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
              <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
              <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" fill="#FBBC05"/>
              <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
            </svg>
            Google
          </button>
          <button class="btn-social">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
            </svg>
            GitHub
          </button>
        </div>

        <p class="bottom-note">No account? <a onclick="switchTab('signup')">Create one →</a></p>
      </div>

      <!-- ── SIGN UP VIEW ── -->
      <div id="view-signup" class="view">
        <h1 class="form-heading">Create<br>account.</h1>
        <p class="form-sub">Join Lumina and start creating today.</p>

        <div class="field-row">
          <div class="field">
            <label>First name</label>
            <div class="input-wrap">
              <input type="text" id="signup-fname" placeholder="Jane">
            </div>
          </div>
          <div class="field">
            <label>Last name</label>
            <div class="input-wrap">
              <input type="text" id="signup-lname" placeholder="Smith">
            </div>
          </div>
        </div>

        <div class="field">
          <label>Email address</label>
          <div class="input-wrap">
            <input type="email" id="signup-email" placeholder="you@example.com" autocomplete="email">
          </div>
        </div>

        <div class="field">
          <label>Password</label>
          <div class="input-wrap">
            <input type="password" id="signup-password" placeholder="Create a strong password" autocomplete="new-password" oninput="checkStrength(this.value)">
          </div>
          <div class="strength-bar" id="strength-bar"><div class="fill" id="strength-fill"></div></div>
          <div class="strength-label" id="strength-label"></div>
        </div>

        <div class="check-row">
          <input type="checkbox" id="terms">
          <span>I agree to the <a href="#">Terms of Service</a> and <a href="#">Privacy Policy</a></span>
        </div>
        
        <div id="signup-error" style="color: #e57373; font-size: 0.8rem; margin-bottom: 1rem; display: none;"></div>
        <div id="signup-success" style="color: #66bb6a; font-size: 0.8rem; margin-bottom: 1rem; display: none;">Registration complete! Switch to login.</div>

        <button class="btn-primary" onclick="handleSignUp()">Create Account</button>

        <div class="or-line"><span>or</span></div>

        <div class="social-row">
          <button class="btn-social">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
              <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
              <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l3.66-2.84z" fill="#FBBC05"/>
              <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
            </svg>
            Google
          </button>
          <button class="btn-social">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/>
            </svg>
            GitHub
          </button>
        </div>

        <p class="bottom-note">Already have an account? <a onclick="switchTab('signin')">Sign in →</a></p>
      </div>

    </div>
  </div>
</div>

<script>
  function switchTab(tab) {
    document.querySelectorAll('.tab-btn').forEach((b, i) => {
      b.classList.toggle('active', (tab === 'signin' && i === 0) || (tab === 'signup' && i === 1));
    });
    document.getElementById('view-signin').classList.toggle('active', tab === 'signin');
    document.getElementById('view-signup').classList.toggle('active', tab === 'signup');
    
    // Clear messages
    document.getElementById('signin-error').style.display = 'none';
    document.getElementById('signup-error').style.display = 'none';
    document.getElementById('signin-success').style.display = 'none';
    document.getElementById('signup-success').style.display = 'none';
  }

  async function handleSignUp() {
    const fname = document.getElementById('signup-fname').value;
    const lname = document.getElementById('signup-lname').value;
    const email = document.getElementById('signup-email').value;
    const password = document.getElementById('signup-password').value;
    const errObj = document.getElementById('signup-error');
    const sucObj = document.getElementById('signup-success');
    
    errObj.style.display = 'none';
    sucObj.style.display = 'none';

    if (!fname || !lname || !email || !password) {
        errObj.textContent = "Please fill in all fields.";
        errObj.style.display = 'block';
        return;
    }

    try {
        const response = await fetch('http://localhost:8000/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ first_name: fname, last_name: lname, email: email, password: password })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            errObj.textContent = data.detail || "Registration failed.";
            errObj.style.display = 'block';
        } else {
            sucObj.style.display = 'block';
            setTimeout(() => { switchTab('signin'); }, 2000);
        }
    } catch (e) {
        errObj.textContent = "Unable to reach server.";
        errObj.style.display = 'block';
    }
  }

  async function handleSignIn() {
    const email = document.getElementById('signin-email').value;
    const password = document.getElementById('signin-password').value;
    const errObj = document.getElementById('signin-error');
    const sucObj = document.getElementById('signin-success');
    
    errObj.style.display = 'none';
    sucObj.style.display = 'none';

    if (!email || !password) {
        errObj.textContent = "Please provide email and password.";
        errObj.style.display = 'block';
        return;
    }

    try {
        const response = await fetch('http://localhost:8000/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email, password: password })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            errObj.textContent = data.detail || "Sign in failed.";
            errObj.style.display = 'block';
        } else {
            sucObj.style.display = 'block';
        }
    } catch (e) {
        errObj.textContent = "Unable to reach server.";
        errObj.style.display = 'block';
    }
  }

  function checkStrength(val) {
    const bar = document.getElementById('strength-bar');
    const fill = document.getElementById('strength-fill');
    const label = document.getElementById('strength-label');

    if (!val) {
      bar.style.display = 'none';
      label.style.display = 'none';
      return;
    }

    bar.style.display = 'block';
    label.style.display = 'block';

    let score = 0;
    if (val.length >= 8) score++;
    if (/[A-Z]/.test(val)) score++;
    if (/[0-9]/.test(val)) score++;
    if (/[^A-Za-z0-9]/.test(val)) score++;

    const levels = [
      { pct: '25%', color: '#c0392b', text: 'Weak', textColor: '#e57373' },
      { pct: '50%', color: '#e67e22', text: 'Fair', textColor: '#ffa726' },
      { pct: '75%', color: '#a89340', text: 'Good', textColor: '#c9a96e' },
      { pct: '100%', color: '#27ae60', text: 'Strong', textColor: '#66bb6a' },
    ];

    const lvl = levels[Math.min(score - 1, 3)] || levels[0];
    fill.style.width = lvl.pct;
    fill.style.background = lvl.color;
    label.style.color = lvl.textColor;
    label.textContent = lvl.text;
  }
</script>

</body>
</html>
"""
    components.html(html_code, height=900, scrolling=True)