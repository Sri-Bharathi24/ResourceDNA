```python
import streamlit as st
import math
import time

# ============================================================
# RESOURCE DNA
# AI RESOURCE INTELLIGENCE AGENT
# ============================================================

st.set_page_config(
    page_title="ResourceDNA",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# RESOURCE PROFILES
# Based on the original ResourceDNA prototype assumptions
# ============================================================

PROFILES = {
    "Small Model": {
        "class": "7B-class",
        "energy": 0.4,
        "water": 1.2,
        "quality": 82
    },
    "Mid-size Model": {
        "class": "70B-class",
        "energy": 1.8,
        "water": 4.5,
        "quality": 91
    },
    "Large Frontier": {
        "class": "Frontier",
        "energy": 4.5,
        "water": 11.0,
        "quality": 97
    },
    "Image Generation": {
        "class": "Image AI",
        "energy": 25.0,
        "water": 60.0,
        "quality": 95
    }
}

CARBON_PER_WH = 0.42
PHONE_CHARGE_WH = 12
BOTTLE_ML = 500


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 5%, rgba(34,197,94,0.10), transparent 25%),
        radial-gradient(circle at 90% 10%, rgba(59,130,246,0.08), transparent 25%),
        #07110d;
    color: #f8fafc;
}

/* Remove Streamlit top space */
.block-container {
    padding-top: 2rem;
    max-width: 1150px;
}

/* Header */

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 35px;
}

.brand-icon {
    width: 48px;
    height: 48px;
    border-radius: 15px;
    background: linear-gradient(135deg,#22c55e,#16a34a);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 25px;
    box-shadow: 0 0 30px rgba(34,197,94,0.25);
}

.brand-name {
    font-size: 25px;
    font-weight: 800;
}

.brand-sub {
    color: #94a3b8;
    font-size: 13px;
}

/* Hero */

.hero {
    text-align: center;
    padding: 35px 20px 30px;
}

.badge {
    display: inline-block;
    padding: 7px 13px;
    border-radius: 30px;
    background: rgba(34,197,94,0.10);
    border: 1px solid rgba(34,197,94,0.25);
    color: #86efac;
    font-size: 13px;
    font-weight: 600;
}

.hero h1 {
    font-size: 52px;
    line-height: 1.05;
    margin: 20px 0 12px;
    font-weight: 800;
    letter-spacing: -2px;
}

.hero h1 span {
    color: #4ade80;
}

.hero p {
    color: #94a3b8;
    font-size: 17px;
    max-width: 680px;
    margin: auto;
    line-height: 1.6;
}

/* Agent card */

.agent-card {
    background: rgba(15,23,20,0.85);
    border: 1px solid rgba(148,163,184,0.15);
    border-radius: 24px;
    padding: 28px;
    box-shadow: 0 20px 70px rgba(0,0,0,0.25);
}

.agent-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 20px;
}

.agent-avatar {
    width: 42px;
    height: 42px;
    border-radius: 13px;
    background: #13251a;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 21px;
}

.agent-title {
    font-weight: 700;
}

.agent-status {
    color: #4ade80;
    font-size: 12px;
}

/* Input */

.stTextArea textarea {
    background: #0b1711 !important;
    border: 1px solid #26372d !important;
    border-radius: 16px !important;
    color: white !important;
    font-size: 15px !important;
}

.stTextArea textarea:focus {
    border: 1px solid #22c55e !important;
}

/* Select */

.stSelectbox div[data-baseweb="select"] > div {
    background: #0b1711;
    border: 1px solid #26372d;
    border-radius: 14px;
}

/* Button */

.stButton button {
    width: 100%;
    border-radius: 14px;
    border: none;
    padding: 13px;
    background: linear-gradient(135deg,#22c55e,#16a34a);
    color: white;
    font-weight: 700;
    font-size: 15px;
    transition: 0.2s;
}

.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 30px rgba(34,197,94,0.25);
}

/* Result */

.result-title {
    margin-top: 35px;
    font-size: 25px;
    font-weight: 800;
}

.result-sub {
    color: #94a3b8;
    margin-bottom: 20px;
}

/* Metrics */

.metric {
    background: #0d1812;
    border: 1px solid #203328;
    border-radius: 20px;
    padding: 22px;
    min-height: 145px;
}

.metric-icon {
    font-size: 23px;
}

.metric-label {
    color: #94a3b8;
    font-size: 12px;
    margin-top: 8px;
}

.metric-value {
    font-size: 28px;
    font-weight: 800;
    margin-top: 4px;
}

.metric-note {
    color: #64748b;
    font-size: 11px;
    margin-top: 5px;
}

/* Insight */

.insight {
    margin-top: 22px;
    padding: 22px;
    border-radius: 20px;
    background: linear-gradient(
        135deg,
        rgba(34,197,94,0.10),
        rgba(34,197,94,0.03)
    );
    border: 1px solid rgba(34,197,94,0.20);
}

.insight-title {
    font-weight: 700;
    margin-bottom: 8px;
}

.insight-text {
    color: #cbd5e1;
    line-height: 1.6;
}

/* Comparison */

.compare {
    margin-top: 18px;
    padding: 18px;
    border-radius: 18px;
    background: #0b1711;
    border: 1px solid #1d3025;
}

.compare strong {
    color: #86efac;
}

/* Footer */

.footer {
    text-align: center;
    color: #64748b;
    font-size: 12px;
    padding: 35px 0 10px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="brand">
    <div class="brand-icon">🌱</div>
    <div>
        <div class="brand-name">ResourceDNA</div>
        <div class="brand-sub">AI Resource Intelligence Agent</div>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="badge">● AI SUSTAINABILITY INTELLIGENCE</div>

<h1>
Every AI answer has a <span>footprint.</span>
</h1>

<p>
ResourceDNA turns the hidden environmental cost of AI
into a simple nutrition label — so you can understand
what your AI usage really costs.
</p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# AGENT INPUT
# ============================================================

st.markdown("""
<div class="agent-card">

<div class="agent-header">
    <div class="agent-avatar">🤖</div>
    <div>
        <div class="agent-title">ResourceDNA Agent</div>
        <div class="agent-status">● Ready to analyse</div>
    </div>
</div>

</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:

    st.markdown("**Choose your AI model**")

    model = st.selectbox(
        "Model",
        list(PROFILES.keys()),
        label_visibility="collapsed"
    )

with col2:

    st.markdown("**What are you asking AI?**")

    prompt = st.text_area(
        "Prompt",
        placeholder="Example: Explain climate change to a 10-year-old...",
        height=120,
        label_visibility="collapsed"
    )


st.write("")

analyse = st.button(
    "✨ Analyse my AI footprint",
    use_container_width=True
)


# ============================================================
# ANALYSIS
# ============================================================

if analyse:

    if not prompt.strip():

        st.warning("Please enter an AI prompt first.")

    else:

        # --------------------------------------------
        # Agent-like processing
        # --------------------------------------------

        with st.status("🤖 ResourceDNA is analysing your request...", expanded=False) as status:

            time.sleep(0.5)

            st.write("🔍 Estimating token demand...")
            time.sleep(0.4)

            st.write("⚡ Calculating energy footprint...")
            time.sleep(0.4)

            st.write("💧 Estimating cooling water...")
            time.sleep(0.4)

            st.write("🌍 Calculating carbon impact...")
            time.sleep(0.4)

            status.update(
                label="✅ Analysis complete",
                state="complete"
            )

        profile = PROFILES[model]

        # --------------------------------------------
        # Token estimation
        # Original prototype assumption:
        # approximately 4 characters = 1 token
        # output approximately 3x input
        # --------------------------------------------

        input_tokens = max(
            1,
            math.ceil(len(prompt) / 4)
        )

        output_tokens = input_tokens * 3

        total_tokens = input_tokens + output_tokens

        # --------------------------------------------
        # Resource calculation
        # --------------------------------------------

        energy = (
            total_tokens / 1000
        ) * profile["energy"]

        water = (
            total_tokens / 1000
        ) * profile["water"]

        carbon = energy * CARBON_PER_WH

        phone_charges = energy / PHONE_CHARGE_WH

        bottle_fraction = water / BOTTLE_ML


        # ====================================================
        # RESULT HEADER
        # ====================================================

        st.markdown(
            '<div class="result-title">🏷️ Your AI Nutrition Label</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="result-sub">'
            f'Estimated footprint • {model} • {total_tokens:,} tokens'
            f'</div>',
            unsafe_allow_html=True
        )


        # ====================================================
        # METRICS
        # ====================================================

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown(f"""
            <div class="metric">
                <div class="metric-icon">💧</div>
                <div class="metric-label">WATER</div>
                <div class="metric-value">{water:.2f} mL</div>
                <div class="metric-note">cooling estimate</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="metric">
                <div class="metric-icon">⚡</div>
                <div class="metric-label">ENERGY</div>
                <div class="metric-value">{energy:.2f} Wh</div>
                <div class="metric-note">inference estimate</div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="metric">
                <div class="metric-icon">🌍</div>
                <div class="metric-label">CARBON</div>
                <div class="metric-value">{carbon:.2f} g</div>
                <div class="metric-note">CO₂e estimate</div>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown(f"""
            <div class="metric">
                <div class="metric-icon">🔤</div>
                <div class="metric-label">TOKENS</div>
                <div class="metric-value">{total_tokens:,}</div>
                <div class="metric-note">estimated processing</div>
            </div>
            """, unsafe_allow_html=True)


        # ====================================================
        # AI INSIGHT
        # ====================================================

        if model == "Small Model":
            insight = (
                "Your request is relatively lightweight. "
                "A small model can handle it with a lower estimated "
                "resource footprint."
            )

        elif model == "Mid-size Model":
            insight = (
                "This is a balanced configuration between estimated "
                "AI quality and resource consumption."
            )

        elif model == "Large Frontier":
            insight = (
                "This model provides higher estimated capability, "
                "but its resource footprint is significantly higher."
            )

        else:
            insight = (
                "Image generation is considerably more resource-intensive "
                "than a typical text-generation request."
            )


        st.markdown(f"""
        <div class="insight">

            <div class="insight-title">
                🤖 ResourceDNA Insight
            </div>

            <div class="insight-text">
                {insight}
            </div>

        </div>
        """, unsafe_allow_html=True)


        # ====================================================
        # RELATABLE COMPARISON
        # ====================================================

        st.markdown(f"""
        <div class="compare">

            📱 Your estimated energy footprint is about
            <strong>{phone_charges:.2f} phone charges</strong>.

            <br><br>

            💧 Your estimated water footprint is about
            <strong>{bottle_fraction:.3f} of a 500 mL bottle</strong>.

        </div>
        """, unsafe_allow_html=True)


        # ====================================================
        # WHY?
        # ====================================================

        with st.expander("🔎 Why am I seeing these numbers?"):

            st.write(
                "ResourceDNA estimates the footprint using "
                "model-level resource assumptions and an estimated "
                "token count."
            )

            st.write(
                f"Your prompt contains approximately "
                f"{input_tokens:,} input tokens."
            )

            st.write(
                f"ResourceDNA estimates approximately "
                f"{output_tokens:,} output tokens."
            )

            st.write(
                "Actual resource consumption varies depending on "
                "the AI provider, hardware, data-centre efficiency, "
                "cooling system, region and electricity grid mix."
            )


        # ====================================================
        # WHAT-IF
        # ====================================================

        st.divider()

        st.subheader("🔮 What if this becomes a habit?")

        daily_queries = st.slider(
            "How many times would you run this prompt per day?",
            min_value=1,
            max_value=10000,
            value=100
        )

        daily_energy = energy * daily_queries
        daily_water = water * daily_queries
        daily_carbon = carbon * daily_queries

        q1, q2, q3 = st.columns(3)

        with q1:
            st.metric(
                "Daily Energy",
                f"{daily_energy:.2f} Wh"
            )

        with q2:
            st.metric(
                "Daily Water",
                f"{daily_water:.2f} mL"
            )

        with q3:
            st.metric(
                "Daily Carbon",
                f"{daily_carbon:.2f} g"
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

ResourceDNA 🌱  
Making AI's hidden resource footprint visible.

<br><br>

Estimates are not direct measurements. Actual AI resource
consumption varies by model, provider, hardware, location,
cooling system and electricity grid mix.

</div>
""", unsafe_allow_html=True)
```
