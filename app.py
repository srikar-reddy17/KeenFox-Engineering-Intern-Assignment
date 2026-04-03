import streamlit as st
import json
from qa import ask_question

st.set_page_config(page_title="KeenFox Intelligence Dashboard", layout="wide")

st.title("KeenFox Competitive Intelligence Dashboard")

try:
    with open("outputs/report.json") as f:
        data = json.load(f)
except Exception as e:
    st.error(" No report found. Please run main.py first.")
    st.stop()

def safe_json_load(text):
    try:
        return json.loads(text)
    except:
        return None

st.header("What Changed")

diff = data.get("diff", {})

if isinstance(diff, dict):
    if "status" in diff:
        st.info(diff["status"])
    else:
        for comp, change in diff.items():
            st.write(f"**{comp}** → {change}")
else:
    st.info("No diff data available")

st.header("Competitor Insights")

competitors = data.get("competitor_insights", {})

for comp, insight in competitors.items():
    with st.expander(f"{comp}", expanded=False):

        parsed = safe_json_load(insight)

        if not parsed:
            st.warning("Could not parse structured data")
            st.text(insight)
            continue

        st.subheader("Key Insights")

        st.write("**Messaging:**", parsed.get("messaging", "N/A"))
        st.write("**Target Audience:**", parsed.get("target_audience", "N/A"))
        st.write("**Strategic Positioning:**", parsed.get("strategic_positioning", "N/A"))

        st.subheader("Strengths")
        for s in parsed.get("strengths", []):
            st.write("- ", s)

        st.subheader("Weaknesses")
        for w in parsed.get("weaknesses", []):
            st.write("- ", w)

        st.subheader("Customer Likes")
        for l in parsed.get("customer_sentiment", {}).get("likes", []):
            st.write("- ", l)

        st.subheader("Customer Complaints")
        for c in parsed.get("customer_sentiment", {}).get("complaints", []):
            st.write("- ", c)

        st.subheader("Pricing Insights")
        for p in parsed.get("pricing_insights", []):
            st.write("- ", p)

        st.subheader("Product Updates")
        for u in parsed.get("product_updates", []):
            st.write("- ", u)

        st.subheader("Messaging Trends")
        st.write(parsed.get("messaging_trends", "N/A"))

        st.subheader("Opportunities for KeenFox")
        for o in parsed.get("opportunities_for_keenfox", []):
            st.write("- ", o)

st.header("Strategic Recommendations")

recommendations = data.get("recommendations", "{}")
rec = safe_json_load(recommendations)

if not rec:
    st.warning("Could not parse recommendations")
    st.text(recommendations)

else:
    # Messaging
    st.subheader("Messaging Strategy")
    st.write("**Weaknesses in Market:**", rec["messaging"].get("weaknesses_in_market", "N/A"))
    st.write("**New Positioning:**", rec["messaging"].get("new_positioning", "N/A"))

    sample_copy = rec["messaging"].get("sample_copy", {})

    if isinstance(sample_copy, str):
        sample_copy = safe_json_load(sample_copy) or {}

    st.subheader("Sample Copy")

    st.write("**Tagline:**")
    st.success(sample_copy.get("tagline", "N/A"))

    st.write("**Body:**")
    st.info(sample_copy.get("body", "N/A"))

    # Channels
    st.subheader("Channel Strategy")
    st.write("**Underutilized Channels:**", rec["channels"].get("underutilized", []))
    st.write("**Overcrowded Channels:**", rec["channels"].get("overcrowded", []))

    st.write("**Recommendations:**")
    for r in rec["channels"].get("recommendations", []):
        st.write("- ", r)

    # GTM Strategy
    st.subheader("GTM Strategy")
    for g in rec.get("gtm_strategy", []):
        st.write(f"**Strategy:** {g.get('strategy', '')}")
        st.write(f"- Rationale: {g.get('rationale', '')}")
        st.write(f"- Impact: {g.get('impact', '')}")
        st.write("---")

st.header("Ask Questions")

question = st.text_input("Ask something about competitors...")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            answer = ask_question(question, data)
            st.success(answer)