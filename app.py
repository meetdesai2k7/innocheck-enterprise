import streamlit as st
import google.generativeai as genai

# 🔑 Paste your API key here
genai.configure(api_key= "ADD YOUR API KEY HERE")

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

st.title("InnoCheck Enterprise 🚀")
st.write("AI that evaluates innovation before you build it")

idea = st.text_area("Enter your idea:")

if st.button("Analyze Idea"):

    prompt = f"""
    You are an enterprise-grade multi-agent AI system called InnoCheck Enterprise.

    Simulate these agents:
    1. Idea Understanding Agent
    2. Market Research Agent
    3. Patent Analysis Agent
    4. Evaluation Agent
    5. Improvement Agent
    6. Decision Agent
    7. Audit Trail Agent

    Idea: {idea}

    Output format:

    --- AGENT LOGS ---

    [Idea Understanding]
    - Problem:
    - Solution:
    - Domain:

    [Market Research]
    - Similar ideas:

    [Patent Analysis]
    - Novelty insight:

    [Evaluation]
    - Novelty Score (0-100):
    - Feasibility:
    - Market Potential:

    [Improvement Suggestions]
    - Improved idea:

    [Final Decision]
    - Decision:
    - Reason:

    [Audit Trail]
    - Step-by-step reasoning summary
    """

    response = model.generate_content(prompt)

    st.subheader("Analysis Result")
    st.write(response.text)
