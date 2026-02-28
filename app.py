import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Interview Voice Bot", page_icon="🎙️")

st.title("🎙️ AI Interview Voice Bot – Revathi Krishna")
st.markdown("### Stage 1 – 100x AI Agent Assessment")
st.divider()

st.write("Ask me anything about my life story, strengths, growth areas, or mindset.")

# 🔑 Use Streamlit Secrets (for deployment)
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = """
You are Revathi Krishna.

You are a BCA student from India and a strong tech enthusiast.
Your primary interests are Artificial Intelligence, Machine Learning, Web Development, and Data Analysis.
You enjoy building practical AI applications and solving real-world problems using technology.
Creativity like filmmaking and design is your hobby, not your main identity.
You are analytical, disciplined, resilient, and continuously learning.
You push yourself through challenges and believe in growth through consistency.

Answer confidently, clearly, and naturally in 4-6 sentences.
Avoid sounding generic or robotic.
Be authentic and grounded.
"""

user_input = st.text_input("Type your question here:")

if st.button("Ask"):
    if user_input:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ],
            )

            answer = response.choices[0].message.content

        st.subheader("Response:")
        st.write(answer)

        # Browser-based speech
        st.components.v1.html(f"""
            <script>
                var msg = new SpeechSynthesisUtterance({repr(answer)});
                msg.rate = 1;
                msg.pitch = 1;
                msg.volume = 1;
                window.speechSynthesis.speak(msg);
            </script>
        """)