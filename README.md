Streamlit ile Chatbot Arayüzü
    pip install streamlit requests
    streamlit run app.py
Frontend Uygulamasını Docker ile Test Et
    requirements.txt
    docker build -t ai-assistant-frontend .
    docker run -d -p 8501:8501 --name ai-assistant-frontend-container ai-assistant-frontend
    http://localhost:8501
Frontend Github'a Yükle ve Streamlit Cloud'da Yayınlama
