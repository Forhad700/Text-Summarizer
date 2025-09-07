import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.documents import Document
from dotenv import load_dotenv
import os

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

MAX_CHARACTERS = 4000 
MODEL_NAME = "llama-3.3-70b-versatile"

def summarize_text(input_text: str) -> str:
    chat = ChatGroq(
        temperature=0.2,
        model_name=MODEL_NAME,
        groq_api_key=groq_api_key
    )

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(input_text)
    docs = [Document(page_content=chunk) for chunk in chunks]

    summaries = []
    for i, doc in enumerate(docs):
        prompt = HumanMessage(content=f"Summarize this part:\n\n{doc.page_content}")
        response = chat.invoke([prompt])
        summaries.append(response.content.strip())

    combined_summary = "\n".join(summaries)

    final_prompt = HumanMessage(content=f"Summarize the following overall summary:\n\n{combined_summary}")
    final_response = chat.invoke([final_prompt])

    return final_response.content.strip()

st.set_page_config(page_title="Text Summarizer Assistant")
st.title("🧠 Text Summarizer Assistant")

st.markdown("""
Where AI Meets Artistry 🎭 — Crafting Summaries with Elegance ✨ and Sharp Insight 💡
""")

txt_input = st.text_area("✍️ Enter Your Text to Summarize", height=300)

if st.button("Summarize"):
    if not groq_api_key:
        st.error("❌ GROQ_API_KEY not Found!")
    elif not txt_input.strip():
        st.warning("⚠️ Please Input Some Text First")
    elif len(txt_input) > MAX_CHARACTERS:
        st.warning(f"⚠️ Input Too Long!!! Limit to {MAX_CHARACTERS} Characters.")
    else:
        with st.spinner("⏳ Generating Summary....."):
            try:
                summary = summarize_text(txt_input)
                st.success("✅ Summary: ")
                st.info(summary)
            except Exception as e:
                st.error(f"❌ An Error Occurred: {e}")