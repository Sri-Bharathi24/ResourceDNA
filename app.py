import streamlit as st
import math

st.set_page_config(
    page_title="ResourceDNA",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------
# Resource assumptions
# -----------------------------

PROFILES = {
    "Small Model": {
        "energy": 0.4,
        "water": 1.2,
        "quality": 82
    },
    "Mid-size Model": {
        "energy": 1.8,
        "water": 4.5,
        "quality": 91
    },
    "Large Frontier Model": {
        "energy": 4.5,
        "water": 11.0,
        "quality": 97
    },
    "Image Generation": {
        "energy": 25.0,
        "water": 60.0,
        "quality": 95
    }
}

CARBON_PER_WH = 0.42
PHONE_CHARGE_WH = 12
BOTTLE_ML = 500


# -----------------------------
# Styling
# -----------------------------

st.markdown(
    """
    <style>
    .stApp {
        background-color: #07110d;
        color: white;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
    }

    .brand {
        font-size: 28px;
        font-weight: 800;
        color: white;
    }

    .brand span {
        color: #4ade80;
    }

    .hero {
        text-align: center;
        padding: 50px 20px 35px;
    }

    .hero h1 {
        font-size: 48px;
        margin-bottom: 10px;
    }

    .hero h1 span {
        color: #4ade80;
    }

    .hero p {
        color: #94a3b8;
        font-size: 18px;
    }

    .agent {
        background-color: #0d1812;
        border: 1px solid #26372d;
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
    }

    .agent-title {
        font-size: 20px;
        font-weight: 700;
    }

    .agent-status {
        color: #4ade80;
        font-size: 13px;
    }

    .result-title {
        font-size: 28px;
        font-weight: 800;
        margin-top: 30px;
    }

    .result-sub {
        color: #94a3b8;
        margin-bottom: 20px;
    }

    .metric-card {
        background-color: #0d1812;
        border: 1px solid #26372d;
        border-radius: 18px;
        padding: 20px;
        text-align: center;
        min-height: 145px;
    }

    .metric-icon {
        font-size: 25px;
    }

    .metric-label {
        color: #94a3b8;
        font-size: 12px;
        margin-top: 8px;
    }

    .metric-value {
        font-size: 28px;
        font-weight: 800;
        margin-top: 5px;
    }

    .metric-note {
        color: #64748b;
        font-size: 11px;
    }

    .insight {
        background-color: #102218;
        border: 1px solid #245333;
        border-radius: 18px;
        padding: 20px;
        margin-top: 20px;
    }

    .insight-title {
        font-size: 17px;
        font-weight: 700;
        color: #86efac;
    }

    .insight-text {
        color: #cbd5e1;
        margin-top: 8px;
        line-height: 1.5;
    }

    .comparison {
        background-color: #0d1812;
        border: 1px solid #26372d;
        border-radius: 18px;
        padding: 20px;
        margin-top: 18px;
        color: #cbd5e1;
        font-size: 16px;
    }

    .footer {
        text-align: center;
        color: #64748b;
        padding: 35px;
        font-size: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    """
    <div class="brand">
        🌱 Resource<span>DNA</span>
    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Hero
# -----------------------------

st.markdown(
    """
    <div class="hero">

        <h1>
            Every AI answer has a <span>footprint.</span>
        </h1>

        <p>
            ResourceDNA turns the hidden environmental cost of AI
            into a simple nutrition label.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Agent
# -----------------------------

st.markdown(
    """
    <div class="agent">

        <div class="agent-title">
            🤖 ResourceDNA Agent
        </div>

        <div class="agent-status">
            ● Ready to analyse
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# User Input
# -----------------------------

col1, col2 = st.columns([1, 2])

with col1:

    st.subheader("Choose AI model")

    model = st.selectbox(
        "AI Model",
        list(PROFILES.keys())
    )


with col2:

    st.subheader("Enter your prompt")

    prompt = st.text_area(
        "Prompt",
        placeholder="Example: Explain climate change to a beginner...",
        height=120
    )


# -----------------------------
# Analyze button
# -----------------------------

analyze = st.button(
    "✨ Analyse my AI footprint",
    use_container_width=True
)


# -----------------------------
# Main calculation
# -----------------------------

if analyze:

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
        st.stop()

    profile = PROFILES[model]

    # Estimate tokens
    input_tokens = max(
        1,
        math.ceil(len(prompt) / 4)
    )

    # Assume output is approximately 3x input
    output_tokens = input_tokens * 3

    total_tokens = input_tokens + output_tokens

    # Energy
    energy = (
        total_tokens / 1000
    ) * profile["energy"]

    # Water
    water = (
        total_tokens / 1000
    ) * profile["water"]

    # Carbon
    carbon = energy * CARBON_PER_WH

    # Comparisons
    phone_charges = energy / PHONE_CHARGE_WH
    bottle_fraction = water / BOTTLE_ML


    # -----------------------------
    # Result
    # -----------------------------

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


    # -----------------------------
    # Metrics
    # -----------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">💧</div>
                <div class="metric-label">WATER</div>
                <div class="metric-value">{water:.2f} mL</div>
                <div class="metric-note">cooling estimate</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">⚡</div>
                <div class="metric-label">ENERGY</div>
                <div class="metric-value">{energy:.2f} Wh</div>
                <div class="metric-note">inference estimate</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">🌍</div>
                <div class="metric-label">CARBON</div>
                <div class="metric-value">{carbon:.2f} g</div>
                <div class="metric-note">CO₂e estimate</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-icon">🔤</div>
                <div class="metric-label">TOKENS</div>
                <div class="metric-value">{total_tokens:,}</div>
                <div class="metric-note">estimated processing</div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # -----------------------------
    # AI-style insight
    # -----------------------------

    if model == "Small Model":

        insight = (
            "This request is relatively lightweight. "
            "A small model can handle it with a lower estimated "
            "resource footprint."
        )

    elif model == "Mid-size Model":

        insight = (
            "This is a middle-ground configuration, balancing "
            "estimated capability with resource consumption."
        )

    elif model == "Large Frontier Model":

        insight = (
            "This model has a higher estimated capability, but "
            "also has a higher resource footprint."
        )

    else:

        insight = (
            "Image generation is estimated to require considerably "
            "more resources than a typical text-generation request."
        )


    st.markdown(
        f"""
        <div class="insight">

            <div class="insight-title">
                🤖 ResourceDNA Insight
            </div>

            <div class="insight-text">
                {insight}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------
    # Simple comparison
    # -----------------------------

    st.markdown(
        f"""
        <div class="comparison">

            📱 Estimated energy:
            <b>{phone_charges:.2f}</b> phone charges.

            <br><br>

            💧 Estimated water:
            <b>{bottle_fraction:.3f}</b> of a 500 mL bottle.

        </div>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------
    # Explanation
    # -----------------------------

    with st.expander("🔎 How did ResourceDNA estimate this?"):

        st.write(
            f"Your prompt contains approximately "
            f"{input_tokens:,} input tokens."
        )

        st.write(
            f"ResourceDNA estimates approximately "
            f"{output_tokens:,} output tokens."
        )

        st.write(
            "The resource values are calculated using the selected "
            "model category and its configured resource assumptions."
        )

        st.write(
            "Actual AI resource consumption varies by provider, "
            "hardware, data-centre efficiency, cooling technology, "
            "location and electricity grid mix."
        )


    # -----------------------------
    # What-if analysis
    # -----------------------------

    st.divider()

    st.subheader("🔮 What if you used this prompt repeatedly?")

    daily_queries = st.slider(
        "Queries per day",
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


# -----------------------------
# Footer
# -----------------------------

st.markdown(
    """
    <div class="footer">

        🌱 ResourceDNA — Making AI's hidden footprint visible.

        <br><br>

        Estimates are indicative, not direct measurements.
        Actual resource consumption varies by model, provider,
        hardware, location and infrastructure.

    </div>
    """,
    unsafe_allow_html=True
)
