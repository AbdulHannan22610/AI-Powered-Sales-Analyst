import html

import streamlit as st


def kpi_card(title, value, color):
    safe_title = html.escape(str(title))
    safe_value = html.escape(str(value))

    st.markdown(
        f"""
        <div class="kpi-card" style="
            background: linear-gradient(135deg, {color});
            padding: 22px 20px;
            border-radius: 15px;
            color: white;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            margin-bottom: 10px;
        ">
            <div class="kpi-label">{safe_title}</div>
            <div class="kpi-value"><strong>{safe_value}</strong></div>
        </div>
        """,
        unsafe_allow_html=True,
    )