import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt

# ---------------------
# Page Configuration
# ---------------------
st.set_page_config(page_title="Sentiment Analyzer", page_icon="😊", layout="centered")

# ---------------------
# Sidebar - About
# ---------------------
with st.sidebar:
    st.title("ℹ️ About")
    st.markdown("""
    This app uses **TextBlob** to perform **Sentiment Analysis**.
    Enter any sentence, review, or tweet to detect whether it's **Positive**, **Negative**, or **Neutral**.

    💡 Built using [Streamlit](https://streamlit.io/)
    """)

# ---------------------
# Main Title
# ---------------------
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>😊 Simple Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.markdown("### Enter text to analyze sentiment:")

# ---------------------
# Text Input
# ---------------------
user_input = st.text_area("✍️ Type your sentence here:")

# ---------------------
# Analyze Button
# ---------------------
if st.button("🔍 Analyze"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Sentiment logic
        if polarity > 0:
            sentiment = "Positive 😀"
            color = "green"
            emoji = "🟢"
        elif polarity < 0:
            sentiment = "Negative 😠"
            color = "red"
            emoji = "🔴"
        else:
            sentiment = "Neutral 😐"
            color = "gray"
            emoji = "🟡"

        # Display Results
        st.markdown("---")
        st.markdown(f"### Sentiment: {emoji} <span style='color:{color}'>{sentiment}</span>", unsafe_allow_html=True)
        st.markdown(f"- **Polarity Score:** `{polarity:.2f}`")
        st.markdown(f"- **Subjectivity Score:** `{subjectivity:.2f}`")
        st.markdown(f"- **Word Count:** `{len(user_input.split())}`")
        st.markdown("---")

        # Progress Bar for Sentiment Polarity
        st.markdown("#### 🔋 Sentiment Polarity (Progress Bar)")
        st.progress((polarity + 1) / 2)

        # Pie Chart for Polarity Distribution
        st.markdown("#### 📊 Polarity Visualization")
        labels = ['Positive', 'Neutral', 'Negative']
        values = [max(polarity, 0), 1 - abs(polarity), max(-polarity, 0)]
        colors = ['#4CAF50', '#FFC107', '#F44336']

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

        # Extra Suggestions
        st.info("💡 Tip: Try pasting a movie review, product review, or tweet!")

