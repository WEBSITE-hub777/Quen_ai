import os
import json

import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Quen AI", page_icon="🤖", layout="wide")
st.title("Quen AI")
st.caption("Multilingual AI assistant for English / Hindi / Hinglish")

SYSTEM_PROMPT = """Aap Quen AI ho. Aap multilingual ho. English, Hindi, aur Hinglish mein answer do. Agar user coding pooche to step-by-step explain karo. Agar vague ho to politely question poochho. Aap text-only assistant ho. Aapko factual, helpful aur clear rehna chahiye."""

@st.cache_resource
def load_model():
    model_name = os.getenv("MODEL_NAME", "microsoft/Phi-3-mini-4k-instruct")
    try:
        pipe = pipeline(
            "text-generation",
            model=model_name,
            tokenizer=model_name,
            device_map="auto",
        )
        return pipe
    except Exception as e:
        st.warning(f"Model load failed: {e}")
        return None

model = load_model()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Namaste! Main Quen AI hoon. Aap mujhse English, Hindi, ya Hinglish mein baat kar sakte ho. Coding, learning, ya general questions poochho."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Aapka sawaal likho...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    if model is None:
        response = "Model load nahi hua hai. Local environment mein MODEL_NAME ko valid Hugging Face model name se set karo, ya training complete karne ke baad is app ko connect karo."
    else:
        prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}\nAssistant:"
        result = model(
            prompt,
            max_new_tokens=300,
            do_sample=True,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.1,
        )
        generated = result[0]["generated_text"]
        response = generated.replace(prompt, "").strip() or "Mujhe samajh nahi aaya. Kya aap aur detail de sakte ho?"

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.write(response)
