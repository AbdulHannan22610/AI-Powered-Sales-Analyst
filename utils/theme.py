"""Global UI theme for AI Sales Analyst — inject once via apply_theme()."""

import streamlit as st

_CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', system-ui, sans-serif;
}

/* Main background */
.stApp {
    background: linear-gradient(160deg, #f8fafc 0%, #eef2ff 45%, #f1f5f9 100%);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
    border-right: 1px solid rgba(148, 163, 184, 0.15);
}
section[data-testid="stSidebar"] * {
    color: #e2e8f0 !important;
}
section[data-testid="stSidebar"] .stRadio label {
    background: rgba(255, 255, 255, 0.06);
    border-radius: 10px;
    padding: 0.35rem 0.75rem;
    margin: 0.15rem 0;
    border: 1px solid transparent;
    transition: all 0.2s ease;
}
section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(99, 102, 241, 0.2);
    border-color: rgba(129, 140, 248, 0.4);
}
section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] .stMarkdown h1 {
    font-weight: 700;
    letter-spacing: -0.02em;
}

/* Hide default Streamlit header/footer clutter */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header[data-testid="stHeader"] {
    background: transparent;
}

/* Primary buttons */
.stButton > button {
    background: linear-gradient(135deg, #6366f1, #4f46e5) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.55rem 1.5rem !important;
    font-weight: 600 !important;
    box-shadow: 0 4px 14px rgba(79, 70, 229, 0.35);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 6px 20px rgba(79, 70, 229, 0.45);
}

/* Inputs */
.stTextInput input, .stNumberInput input, .stSelectbox > div > div {
    border-radius: 10px !important;
    border: 1px solid #cbd5e1 !important;
}
.stTextInput input:focus, .stNumberInput input:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.15) !important;
}

/* Charts in soft panels */
div[data-testid="stPyplotGlobalUsage"] {
    background: white;
    border-radius: 16px;
    padding: 1rem;
    box-shadow: 0 4px 24px rgba(15, 23, 42, 0.06);
    border: 1px solid #e2e8f0;
}

/* Default alert boxes — softer */
.stAlert {
    border-radius: 12px !important;
    border: none !important;
}

/* Dashboard KPI cards — no heading tags, bold values */
.kpi-card .kpi-label {
    font-size: 0.9rem;
    font-weight: 500;
    letter-spacing: 0.02em;
    opacity: 0.92;
    margin: 0;
    line-height: 1.3;
}
.kpi-card .kpi-value {
    margin: 0.65rem 0 0;
    font-size: 2.1rem;
    line-height: 1.2;
}
.kpi-card .kpi-value strong {
    font-weight: 800;
    letter-spacing: -0.02em;
}

/* Sidebar file uploader */
section[data-testid="stSidebar"] [data-testid="stFileUploader"] {
    background: linear-gradient(145deg, rgba(99, 102, 241, 0.18), rgba(79, 70, 229, 0.08));
    border: 2px dashed rgba(129, 140, 248, 0.55) !important;
    border-radius: 14px !important;
    padding: 1.1rem 1rem !important;
    margin-top: 0.25rem;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
section[data-testid="stSidebar"] [data-testid="stFileUploader"]:hover {
    border-color: rgba(167, 139, 250, 0.9) !important;
    box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15);
}
section[data-testid="stSidebar"] [data-testid="stFileUploader"] section {
    padding: 0 !important;
}
section[data-testid="stSidebar"] [data-testid="stFileUploader"] [data-testid="stFileUploaderDropzone"] {
    background: transparent !important;
    border: none !important;
}
section[data-testid="stSidebar"] [data-testid="stFileUploader"] small {
    color: #94a3b8 !important;
    font-size: 0.72rem !important;
}
section[data-testid="stSidebar"] [data-testid="stFileUploader"] button {
    background: linear-gradient(135deg, #818cf8, #6366f1) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.45rem 1.1rem !important;
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.35) !important;
}
section[data-testid="stSidebar"] [data-testid="stFileUploader"] button:hover {
    background: linear-gradient(135deg, #a5b4fc, #818cf8) !important;
    transform: translateY(-1px);
}
section[data-testid="stSidebar"] .upload-zone-label {
    display: flex;
    flex-direction: column;
    gap: 0.15rem;
    margin: 1rem 0 0.35rem;
    padding: 0 0.1rem;
}
section[data-testid="stSidebar"] .upload-icon {
    font-size: 1.35rem;
    line-height: 1;
}
section[data-testid="stSidebar"] .upload-title {
    color: #f1f5f9 !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
}
section[data-testid="stSidebar"] .upload-hint {
    color: #94a3b8 !important;
    font-size: 0.72rem !important;
}

/* Category filter — bold, bright selected value */
section[data-testid="stSidebar"] [data-testid="stSelectbox"] label {
    font-weight: 600 !important;
    color: #94a3b8 !important;
    font-size: 0.78rem !important;
    letter-spacing: 0.04em;
}
section[data-testid="stSidebar"] [data-testid="stSelectbox"] > div > div {
    background: rgba(255, 255, 255, 0.1) !important;
    border: 1px solid rgba(129, 140, 248, 0.5) !important;
    border-radius: 10px !important;
}
section[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"] > div,
section[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"] span,
section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[role="combobox"],
section[data-testid="stSidebar"] [data-testid="stSelectbox"] input {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    -webkit-text-fill-color: #ffffff !important;
}
section[data-testid="stSidebar"] [data-testid="stSelectbox"] svg {
    fill: #c7d2fe !important;
}
</style>
"""


def upload_section_label():
    """Label above the CSV uploader in the sidebar."""
    st.sidebar.markdown(
        """
        <div class="upload-zone-label">
            <span class="upload-icon">📤</span>
            <span class="upload-title">Upload sales data</span>
            <span class="upload-hint">CSV file · drag or browse</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def apply_theme():
    """Inject global CSS. Call once right after st.set_page_config()."""
    st.markdown(_CUSTOM_CSS, unsafe_allow_html=True)


def sidebar_brand():
    """Branded sidebar header."""
    st.sidebar.markdown(
        """
        <div style="text-align:center; padding: 0.5rem 0 1.25rem 0;">
            <div style="
                width: 52px; height: 52px; margin: 0 auto 0.75rem;
                background: linear-gradient(135deg, #818cf8, #6366f1);
                border-radius: 14px;
                display: flex; align-items: center; justify-content: center;
                font-size: 1.5rem; box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
            ">📊</div>
            <h2 style="margin:0; font-size:1.15rem; font-weight:700; color:#f8fafc !important;">
                AI Sales Analyst
            </h2>
            <p style="margin:0.35rem 0 0; font-size:0.75rem; color:#94a3b8 !important;">
                Insights · Predict · Chat
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = ""):
    """Hero-style page title."""
    sub = (
        f'<p style="margin:0.5rem 0 0; color:#64748b; font-size:1rem;">{subtitle}</p>'
        if subtitle
        else ""
    )
    st.markdown(
        f"""
        <div style="
            background: white;
            border-radius: 16px;
            padding: 1.5rem 1.75rem;
            margin-bottom: 1.5rem;
            border: 1px solid #e2e8f0;
            box-shadow: 0 4px 24px rgba(15, 23, 42, 0.05);
        ">
            <h1 style="
                margin:0; font-size:1.75rem; font-weight:700;
                color:#0f172a; letter-spacing:-0.03em;
            ">{title}</h1>
            {sub}
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_label(text: str):
    """Small uppercase section divider."""
    st.markdown(
        f"""
        <p style="
            margin: 1.5rem 0 0.75rem;
            font-size: 0.7rem;
            font-weight: 600;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #94a3b8;
        ">{text}</p>
        """,
        unsafe_allow_html=True,
    )


def insight_card(kind: str, title: str, message: str):
    """Styled insight row (success | info | warning)."""
    styles = {
        "success": ("#ecfdf5", "#059669", "#10b981", "✓"),
        "info": ("#eff6ff", "#2563eb", "#3b82f6", "◆"),
        "warning": ("#fffbeb", "#d97706", "#f59e0b", "!"),
    }
    bg, accent, border, icon = styles.get(kind, styles["info"])
    st.markdown(
        f"""
        <div style="
            background: {bg};
            border-left: 4px solid {border};
            border-radius: 12px;
            padding: 1rem 1.25rem;
            margin-bottom: 0.75rem;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
        ">
            <div style="display:flex; gap:0.75rem; align-items:flex-start;">
                <span style="
                    color:{accent}; font-weight:700; font-size:1rem;
                    width:1.5rem; text-align:center;
                ">{icon}</span>
                <div>
                    <strong style="color:#0f172a; display:block; margin-bottom:0.25rem;">
                        {title}
                    </strong>
                    <span style="color:#475569; font-size:0.9rem; line-height:1.5;">
                        {message}
                    </span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def empty_state(title: str, hint: str):
    """Friendly placeholder when no CSV is loaded."""
    st.markdown(
        f"""
        <div style="
            text-align: center;
            padding: 3rem 2rem;
            background: white;
            border-radius: 20px;
            border: 2px dashed #cbd5e1;
            margin: 2rem 0;
        ">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📁</div>
            <h3 style="color:#0f172a; margin:0 0 0.5rem;">{title}</h3>
            <p style="color:#64748b; margin:0; max-width: 420px; margin: 0 auto;">
                {hint}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

