# Text Summarizer Assistant

Text Summarizer Assistant is a **Generative AI** tool built on powerful language models that helps users distill large blocks of text into short, meaningful summaries — enhancing comprehension, speed and clarity. This project highlights the efficiency and power of modern AI in enhancing content consumption.

## Features
- **Accurate Text Summarization**: Generate clear and coherent summaries from user-provided text.
- **User-Friendly Interface**: Simple and intuitive input area designed for quick summarization.
- **Generative AI in Action**: Utilizes LLaMA 3 LLM model running on high-performance.
- **Fast and Responsive**: Delivers summaries with minimal latency for a smooth user experience.


## Implementation Details

- The app takes user’s input and turns it into a prompt that tells the AI exactly what to do — in this case, to summarize text.
- If the input text is longer than the allowed limit, the app splits the text into smaller chunks to process each part separately.
- LangChain manages communication between the app and the AI, making the process smooth and reliable.
- Before sending the text or chunks, the app validates the input to ensure it’s neither empty nor too long.
- The app sends each chunk to the AI model, gets individual summaries, and then combines or presents the results.
- Once the AI generates a summary, the app shows it right away on the page.
- If something goes wrong (like missing API key or connection problems), the app shows helpful error messages.


## Tech Stack
- **Programming Language**
  - Python: Core language for backend and application logic.
- **Framework/Libraries**
  - LangChain: Framework to manage prompts, chains, interaction with language models.
  - langchain_groq: Groq-specific integration for calling Groq’s LLaMA models.
  - langchain_core: Core LangChain message types (e.g., `HumanMessage`).
- **APIs**:
  - Groq API for accessing LLaMA 3 summarization models.
- **Models**:
  - **Meta LLaMA 3**
- **Version Control & Deployment**
  - Git/GitHub: Source code versioning and remote repository.
  - Streamlit Community Cloud: Hosting and deployment platform.
