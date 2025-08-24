# T5 Text Summarizer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

A web application that summarizes long documents using a fine-tuned T5 (Text-to-Text Transfer Transformer) model. This project demonstrates an end-to-end workflow from model training on Google Colab to final deployment on Streamlit Cloud.

## 🚀 Live Demo

You can access the live application here: **[T5 Text Summarizer App](https://your-app-url.streamlit.app)**

*(Note: Please replace `https://your-app-url.streamlit.app` with your actual Streamlit app URL.)*

## ✨ Features

-   **Efficient Summarization:** Condenses long articles and documents into concise summaries.
-   **State-of-the-Art Model:** Powered by a fine-tuned version of Google's T5 model.
-   **Interactive UI:** A simple and user-friendly web interface built with Streamlit.

## 🛠️ Technology Stack

-   **Backend & Modeling:** Python
-   **Machine Learning Framework:** PyTorch
-   **NLP Library:** Hugging Face `transformers`
-   **Web Framework:** Streamlit
-   **Training Data:** Hugging Face `datasets`

## 🧠 Model Details

The summarization model is a `t5-small` checkpoint that has been fine-tuned on the `multi_news` dataset, which is a large-scale dataset for the summarization of news articles.

-   **Base Model:** `t5-small`
-   **Fine-tuned on:** `multi_news`
-   **Hugging Face Repository:** [Nomi78600/t5-text-summerizer](https://huggingface.co/Nomi78600/t5-text-summerizer)

## ⚙️ Setup and Local Installation

To run this application on your local machine, please follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/780Noman/t5-text-summarizer.git
    cd t5-text-summarizer
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    The application should now be running in your web browser.

## ☁️ Deployment

This application is deployed on **Streamlit Cloud**. The deployment is automated via GitHub. Any push to the `main` branch of the GitHub repository will trigger a redeployment of the application.

The application uses Streamlit's Secrets management to securely handle the Hugging Face API token required for downloading the model.

## 🙏 Acknowledgements

-   Thanks to the **Hugging Face** team for their incredible `transformers` library and for hosting the model.
-   Thanks to the **Streamlit** team for making it easy to build and deploy data applications.
