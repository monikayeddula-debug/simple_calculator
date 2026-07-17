import streamlit as st
from openai import OpenAI

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 AI Calculator")
st.write("Simple Calculator using Streamlit and OpenAI")

# -----------------------------
# OpenAI API Key
# -----------------------------
api_key = st.sidebar.text_input(
    "Enter OpenAI API Key",
    type="password"
)

client = OpenAI(api_key=api_key) if api_key else None

# -----------------------------
# Calculator Inputs
# -----------------------------
num1 = st.number_input("Enter First Number", value=0.0)
num2 = st.number_input("Enter Second Number", value=0.0)

operation = st.selectbox(
    "Choose Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# -----------------------------
# Calculate
# -----------------------------
if st.button("Calculate"):

    if operation == "Addition":
        result = num1 + num2
        symbol = "+"

    elif operation == "Subtraction":
        result = num1 - num2
        symbol = "-"

    elif operation == "Multiplication":
        result = num1 * num2
        symbol = "*"

    else:
        if num2 == 0:
            st.error("Division by zero is not allowed.")
            st.stop()
        result = num1 / num2
        symbol = "/"

    st.success(f"Result = {result}")

    # -------------------------
    # AI Explanation
    # -------------------------
    if client:

        prompt = f"""
        Explain this calculation in simple words.

        {num1} {symbol} {num2} = {result}
        """

        response = client.responses.create(
            model="gpt-5-mini",
            input=prompt
        )

        st.subheader("🤖 AI Explanation")
        st.write(response.output_text)

    else:
        st.info("Enter your OpenAI API Key to get an AI explanation.")