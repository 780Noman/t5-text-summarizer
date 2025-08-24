import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# The model repository name on Hugging Face Hub
MODEL_REPO = "Nomi78600/t5-text-summerizer"

st.set_page_config(page_title="Text Summarizer", layout="wide")

# Function to load model and tokenizer
# Using st.cache_resource to cache them for better performance
@st.cache_resource
def load_model():
    """Loads the T5 tokenizer and model from the Hugging Face Hub."""
    try:
        tokenizer = T5Tokenizer.from_pretrained(MODEL_REPO)
        model = T5ForConditionalGeneration.from_pretrained(MODEL_REPO)
        return tokenizer, model
    except Exception as e:
        # Return None if model loading fails
        st.error(f"Error loading model: {e}")
        return None, None

tokenizer, model = load_model()

st.title("Text Summarization with T5")
st.write("This app uses a fine-tuned T5 model to summarize long documents.")

if model is not None:
    # Text area for user input
    input_text = st.text_area("Enter the text you want to summarize:", height=250, placeholder="Paste your document here...")

    if st.button("Summarize", type="primary"):
        if input_text:
            with st.spinner("Generating summary..."):
                # Preprocess the input text
                prefixed_text = "summarize: " + input_text
                inputs = tokenizer.encode(prefixed_text, return_tensors="pt", max_length=512, truncation=True)

                # Move inputs to the appropriate device
                device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
                model.to(device)
                inputs = inputs.to(device)

                # Generate the summary
                summary_ids = model.generate(
                    inputs,
                    max_length=150,
                    min_length=40,
                    length_penalty=2.0,
                    num_beams=4,
                    early_stopping=True
                )

                # Decode the generated summary
                summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

                st.subheader("Generated Summary:")
                st.success(summary)
        else:
            st.warning("Please enter some text to summarize.")
else:
    st.error("Model could not be loaded. Please ensure the repository 'Nomi78600/t5-text-summarizer' is public on the Hugging Face Hub and that you have an internet connection.")
