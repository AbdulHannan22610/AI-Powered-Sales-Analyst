import os

import streamlit as st
import pandas as pd
import joblib

from utils.preprocess import clean_data
from utils.charts import line_chart, bar_chart, pie_chart
from utils.ui_components import kpi_card
from utils.theme import (
    apply_theme,
    sidebar_brand,
    upload_section_label,
    page_header,
    section_label,
    insight_card,
    empty_state,
)
from services.allam import ask_allam

SAMPLE_PATH = "data/sample.csv"
MODEL_PATH = "models/sales_model.pkl"


@st.cache_resource
def load_model():
    if os.path.isfile(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None


st.set_page_config(page_title="AI Sales Analyst", layout="wide", page_icon="📊")
apply_theme()

sidebar_brand()

page = st.sidebar.radio("Menu", [
    "Dashboard",
    "Prediction",
    "AI Chat"
])

if st.sidebar.button("Load sample data", use_container_width=True):
    if os.path.isfile(SAMPLE_PATH):
        st.session_state["df"] = clean_data(pd.read_csv(SAMPLE_PATH))
        st.sidebar.success("Sample data loaded.")
    else:
        st.sidebar.error("Sample file not found at data/sample.csv")

upload_section_label()
uploaded_file = st.sidebar.file_uploader(
    "Choose your file",
    type="csv",
    label_visibility="collapsed",
)

model = load_model()
if model is None:
    st.sidebar.warning("ML model missing. Run: python ml/train_model.py")

df = None

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df = clean_data(df)

    st.session_state["df"] = df

df = st.session_state.get("df")

# ================= FILTER =================
if df is not None:

    categories = df["category"].unique()
    selected_category = st.sidebar.selectbox("Filter Category", categories)

    df = df[df["category"] == selected_category]

# ================= DASHBOARD =================
if page == "Dashboard":
    if df is None:
        page_header("Dashboard", "Upload a CSV in the sidebar to get started.")
        empty_state(
            "No data yet",
            "Use the sidebar uploader to load your sales CSV. Sample data lives in data/sample.csv.",
        )
    else:
        page_header("Dashboard", "Live overview of sales performance and trends.")

        c1, c2 = st.columns(2)
        with c1:
            kpi_card("Total Sales", round(df["total_sales"].sum(), 2), "#6a11cb, #2575fc")
        with c2:
            kpi_card(
                "Top Product",
                df.groupby("product")["total_sales"].sum().idxmax(),
                "#ff512f, #dd2476",
            )

        section_label("Analytics")
        st.pyplot(line_chart(df))
        col_a, col_b = st.columns(2)
        with col_a:
            st.pyplot(bar_chart(df))
        with col_b:
            st.pyplot(pie_chart(df))

        section_label("AI business insights")
        top_product = df.groupby("product")["total_sales"].sum().idxmax()
        best_category = df.groupby("category")["total_sales"].sum().idxmax()
        lowest_product = df.groupby("product")["total_sales"].sum().idxmin()

        insight_card(
            "success",
            "Revenue leader",
            f"{top_product} is generating the highest sales — consider extra marketing investment.",
        )
        insight_card(
            "info",
            "Growth opportunity",
            f"The {best_category} category shows strong performance — expand inventory and promotions.",
        )
        insight_card(
            "warning",
            "Needs attention",
            f"{lowest_product} is underperforming — review pricing, promotions, and demand.",
        )

# ================= PREDICTION =================
elif page == "Prediction":
    if df is None:
        page_header("Prediction Engine", "Load sales data first to enable predictions.")
        empty_state("Upload required", "Add a CSV in the sidebar before running the ML model.")
    else:
        page_header("Prediction Engine", "Forecast total sales from quantity, price, and discount.")

        q = st.number_input("Quantity", min_value=0)
        p = st.number_input("Unit Price", min_value=0.0)
        d = st.number_input("Discount (%)", min_value=0.0, max_value=100.0)

        if st.button("Predict", type="primary"):
            if model is None:
                st.error("Train the model first: `python ml/train_model.py`")
            else:
                result = model.predict([[q, p, d]])[0]
                st.success(f"Predicted sales: {round(result, 2)}")
                st.bar_chart(pd.DataFrame({"Predicted": [result]}))

# ================= AI CHAT =================
elif page == "AI Chat":
    page_header("ALLaM 2-7B Assistant", "Ask natural-language questions about your sales data.")

    if df is None:
        empty_state(
            "Chat needs data",
            "Upload a CSV in the sidebar, then ask things like “Which category grew fastest?”",
        )
    else:
        question = st.text_input("Ask a question about your sales", placeholder="e.g. What is our best-selling product?")
        if question:
            with st.spinner("Thinking..."):
                answer = ask_allam(question, df.to_string())
            st.markdown(
                f"""
                <div style="
                    background: white; border-radius: 14px; padding: 1.25rem 1.5rem;
                    border: 1px solid #e2e8f0; line-height: 1.6; color: #334155;
                ">{answer}</div>
                """,
                unsafe_allow_html=True,
            )
