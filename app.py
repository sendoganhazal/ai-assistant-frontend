"""
    Fastapi endpointimize bağlanan basit bir chatbot arayüzü geliştir
"""

import streamlit as st
import requests

# canlı backend adresi
BACKEND_URL = "https://ai-assistant-backend-4usm.onrender.com"
# sayfa ayarları
st.set_page_config(
    page_title = "Akıllı Asistan",
    page_icon = "🤖",
    layout = "centered"
)

st.title("🤖 Akıllı Asistan")
st.write("Mesajınızı yazın, asistan size cevap versin.")

# sohbet geçmişi
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# backende den eski mesajları çekme
def load_messages_from_backend():
    try:
        response = requests.get(f"{BACKEND_URL}/messages")
        if response.status_code == 200:
            data = response.json()
            return data.get("messages", [])
        return []
    except:
        return []
    
# mesajımızı backende gönder
def send_message_to_backend(user_message):
    try:
        response = requests.post(f"{BACKEND_URL}/chat", json = {"user_message": user_message})
        if response.status_code == 200:
            return response.json()
        return {"assistant_response": "Bir hata oluştu."}   
    except:
        return {"assistant_response": "backend servisine bağlanamadı"}
    
# sayfa ilk açıldığında geçmiş mesajları yükle
if not st.session_state.chat_history:
    old_messages = load_messages_from_backend()

    for item in old_messages:
        st.session_state.chat_history.append(
            {
                "role": "user",
                "content": item["user_message"]
            }
        )
        st.session_state.chat_history.append(
            {
                "role": "assistant",
                "content": item["assistant_response"]
            }
        )

# eski mesajları göster
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# yeni mesaj girişi
user_input = st.chat_input("Mesajınızı yazın: ")

if user_input:
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    result = send_message_to_backend(user_input)
    assistant_response = result.get("assistant_response", "bir cevap alınamadı")

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )

    with st.chat_message("assistant"):
        st.write(assistant_response)