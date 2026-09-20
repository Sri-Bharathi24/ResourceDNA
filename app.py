import streamlit as st
import math
import time

# =========================================================
# RESOURCE DNA
# =========================================================

st.set_page_config(
    page_title="ResourceDNA",
    page_icon="🌱",
    layout="wide"
)

# =========================================================
# RESOURCE PROFILES
# =========================================================

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

# Insight copy, keyed by model — add a new model here and it's automatically
# picked up (no if/elif chain to maintain).
INSIGHTS = {
    "Small Model": (
        "This request is relatively lightweight. "
        "A small model has a lower estimated resource "
        "footprint for this type of workload."
    ),
    "Mid-size Model": (
        "This configuration provides a middle ground "
        "between estimated model capability and resource use."
    ),
    "Large Frontier Model": (
        "This model category has a higher estimated "
        "resource footprint than smaller model categories."
    ),
    "Image Generation": (
        "Image generation is estimated to require "
        "considerably more resources than typical text requests."
    ),
}

CARBON_PER_WH = 0.42
PHONE_CHARGE_WH = 12
BOTTLE_ML = 500


# =========================================================
# HTML RENDER HELPER
# =========================================================
#
# st.markdown() runs its input through a CommonMark parser before
# injecting the HTML. Any line indented 4+ spaces that follows a blank
# line is treated as an "indented code block" and gets rendered as
# literal text instead of parsed HTML. Our HTML strings below are
# indented for readability and have blank lines between nested <div>s,
# which triggers exactly that bug (tags show up as raw text on the
# page). Flattening to one line before handing it to st.markdown avoids
# the problem entirely, while keeping the source readable.

def render_html(html: str) -> None:
    flat = " ".join(
        line.strip()
        for line in html.strip().splitlines()
        if line.strip()
    )
    st.markdown(flat, unsafe_allow_html=True)


# =========================================================
# PAGE STYLE
# =========================================================

render_html(
    """
    <style>

    .stApp {
        background-color: #07110d;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 30px;
        padding-bottom: 40px;
    }

    /* Main title */

    .main-title {
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        margin-top: 40px;
        margin-bottom: 10px;
        color: white;
    }

    .green {
        color: #4ade80;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 18px;
        margin-bottom: 40px;
    }

    /* Agent */

    .agent-box {
        background-color: #0d1812;
        border: 1px solid #26372d;
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 20px;
    }

    .agent-name {
        color: white;
        font-size: 20px;
        font-weight: 700;
    }

    .agent-status {
        color: #4ade80;
        font-size: 13px;
        margin-top: 4px;
    }

    /* Result title */

    .result-title {
        color: white;
        font-size: 30px;
        font-weight: 800;
        margin-top: 35px;
    }

    .result-subtitle {
        color: #94a3b8;
        font-size: 14px;
        margin-bottom: 20px;
    }

    /* Metric */

    .metric-box {
        background-color: #0d1812;
        border: 1px solid #26372d;
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        min-height: 145px;
    }

    .metric-icon {
        font-size: 28px;
    }

    .metric-name {
        color: #94a3b8;
        font-size: 12px;
        margin-top: 8px;
    }

    .metric-value {
        color: white;
        font-size: 27px;
        font-weight: 800;
        margin-top: 5px;
    }

    .metric-description {
        color: #64748b;
        font-size: 11px;
        margin-top: 5px;
    }

    /* Insight */

    .insight-box {
        background-color: #102218;
        border: 1px solid #245333;
        border-radius: 18px;
        padding: 20px;
        margin-top: 20px;
    }

    .insight-heading {
        color: #86efac;
        font-size: 17px;
        font-weight: 700;
    }

    .insight-content {
        color: #cbd5e1;
        font-size: 15px;
        line-height: 1.6;
        margin-top: 8px;
    }

    /* Comparison */

    .comparison-box {
        background-color: #0d1812;
        border: 1px solid #26372d;
        border-radius: 18px;
        padding: 20px;
        margin-top: 18px;
        color: #cbd5e1;
        font-size: 16px;
    }

    /* Footer */

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 12px;
        margin-top: 40px;
    }

    </style>
    """
)


# =========================================================
# HEADER
# =========================================================

render_html(
    """
    <div style="
        font-size:28px;
        font-weight:800;
        color:white;
    ">
        🌱 Resource<span style="color:#4ade80;">DNA</span>
    </div>
    """
)


# =========================================================
# HERO
# =========================================================

render_html(
    """
    <div class="main-title">
        Every AI answer has a <span class="green">footprint.</span>
    </div>

    <div class="subtitle">
        See the hidden water, energy and carbon cost of AI.
    </div>
    """
)


# =========================================================
# AI AGENT
# =========================================================

render_html(
    """
    <div class="agent-box">

        <div class="agent-name">
            🤖 ResourceDNA Agent
        </div>

        <div class="agent-status">
            ● Ready to analyse your AI request
        </div>

    </div>
    """
)


# =========================================================
# INPUT
# =========================================================

left, right = st.columns([1, 2])

with left:

    st.markdown("### 🤖 Choose AI Model")

    model = st.selectbox(
        "Model",
        [
            "Small Model",
            "Mid-size Model",
            "Large Frontier Model",
            "Image Generation"
        ],
        label_visibility="collapsed"
    )


with right:

    st.markdown("### 💬 Your AI Prompt")

    prompt = st.text_area(
        "Prompt",
        placeholder="Example: Explain climate change to a beginner...",
        height=120,
        label_visibility="collapsed"
    )


# =========================================================
# BUTTON
# =========================================================

analyse = st.button(
    "✨ Analyse my AI footprint",
    use_container_width=True
)


# =========================================================
# ANALYSIS
# =========================================================

if analyse:

    if not prompt.strip():

        st.warning("Please enter a prompt first.")

    else:

        # -----------------------------------------
        # AI-style analysis
        # -----------------------------------------

        with st.spinner("🤖 ResourceDNA is analysing your request..."):

            time.sleep(1)


        profile = PROFILES[model]

        # -----------------------------------------
        # Token estimation
        # -----------------------------------------

        input_tokens = max(
            1,
            math.ceil(len(prompt) / 4)
        )

        output_tokens = input_tokens * 3

        total_tokens = input_tokens + output_tokens

        # -----------------------------------------
        # Resource calculation
        # -----------------------------------------

        energy = (
            total_tokens / 1000
        ) * profile["energy"]

        water = (
            total_tokens / 1000
        ) * profile["water"]

        carbon = (
            energy * CARBON_PER_WH
        )

        phone_charges = (
            energy / PHONE_CHARGE_WH
        )

        bottle_fraction = (
            water / BOTTLE_ML
        )

        quality = profile["quality"]


        # =================================================
        # RESULT
        # =================================================

        st.markdown(
            '<div class="result-title">🏷️ Your AI Nutrition Label</div>',
            unsafe_allow_html=True
        )

        render_html(
            f"""
            <div class="result-subtitle">
                {model} • Estimated {total_tokens:,} tokens
            </div>
            """
        )


        # =================================================
        # METRICS
        # =================================================

        c1, c2, c3, c4, c5 = st.columns(5)


        with c1:

            render_html(
                f"""
                <div class="metric-box">

                    <div class="metric-icon">💧</div>

                    <div class="metric-name">
                        WATER
                    </div>

                    <div class="metric-value">
                        {water:.2f} mL
                    </div>

                    <div class="metric-description">
                        cooling estimate
                    </div>

                </div>
                """
            )


        with c2:

            render_html(
                f"""
                <div class="metric-box">

                    <div class="metric-icon">⚡</div>

                    <div class="metric-name">
                        ENERGY
                    </div>

                    <div class="metric-value">
                        {energy:.2f} Wh
                    </div>

                    <div class="metric-description">
                        inference estimate
                    </div>

                </div>
                """
            )


        with c3:

            render_html(
                f"""
                <div class="metric-box">

                    <div class="metric-icon">🌍</div>

                    <div class="metric-name">
                        CARBON
                    </div>

                    <div class="metric-value">
                        {carbon:.2f} g
                    </div>

                    <div class="metric-description">
                        CO₂e estimate
                    </div>

                </div>
                """
            )


        with c4:

            render_html(
                f"""
                <div class="metric-box">

                    <div class="metric-icon">🔤</div>

                    <div class="metric-name">
                        TOKENS
                    </div>

                    <div class="metric-value">
                        {total_tokens:,}
                    </div>

                    <div class="metric-description">
                        estimated processing
                    </div>

                </div>
                """
            )


        with c5:

            render_html(
                f"""
                <div class="metric-box">

                    <div class="metric-icon">🎯</div>

                    <div class="metric-name">
                        QUALITY
                    </div>

                    <div class="metric-value">
                        {quality}/100
                    </div>

                    <div class="metric-description">
                        model benchmark score
                    </div>

                </div>
                """
            )


        # =================================================
        # AI INSIGHT
        # =================================================

        insight = INSIGHTS[model]

        render_html(
            f"""
            <div class="insight-box">

                <div class="insight-heading">
                    🤖 ResourceDNA Insight
                </div>

                <div class="insight-content">
                    {insight}
                </div>

            </div>
            """
        )


        # =================================================
        # RELATABLE COMPARISON
        # =================================================

        render_html(
            f"""
            <div class="comparison-box">

                📱 Estimated energy is about
                <b>{phone_charges:.2f}</b> phone charges.

                <br><br>

                💧 Estimated water is about
                <b>{bottle_fraction:.3f}</b> of a 500 mL bottle.

            </div>
            """
        )


        # =================================================
        # EXPLANATION
        # =================================================

        with st.expander("🔎 How did ResourceDNA calculate this?"):

            st.write(
                f"Estimated input tokens: {input_tokens:,}"
            )

            st.write(
                f"Estimated output tokens: {output_tokens:,}"
            )

            st.write(
                "Token counts are approximated as roughly 1 token per "
                "4 characters, with output assumed to be 3x the input "
                "length. This is a rough heuristic, not an exact tokenizer "
                "count — real usage will vary by model and prompt."
            )

            st.write(
                "The resource calculation uses the selected model category "
                "and its configured resource assumptions."
            )

            st.write(
                "These are estimates, not direct measurements. "
                "Actual resource consumption can vary by provider, "
                "hardware, data-centre efficiency, cooling technology, "
                "location and electricity grid mix."
            )


        # =================================================
        # WHAT-IF
        # =================================================

        st.divider()

        st.markdown("### 🔮 What if you used this prompt repeatedly?")

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
                f"{daily_energy:,.2f} Wh"
            )


        with q2:

            st.metric(
                "Daily Water",
                f"{daily_water:,.2f} mL"
            )


        with q3:

            st.metric(
                "Daily Carbon",
                f"{daily_carbon:,.2f} g"
            )


# =========================================================
# FOOTER
# =========================================================

render_html(
    """
    <div class="footer">

        🌱 ResourceDNA — Making AI's hidden footprint visible.

        <br><br>

        Estimates are indicative, not direct measurements.
        Actual resource consumption varies by model, provider,
        hardware, location and infrastructure.

    </div>
    """
)
