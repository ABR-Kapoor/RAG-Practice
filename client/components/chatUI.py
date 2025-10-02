import streamlit as st
from utils.api import query_bot 

def render_chatui():
    st.subheader("chat with BabyBot :speech_balloon:")
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    # render existing messages history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # input and response
    user_input = st.chat_input("Ask me anything about the documents you uploaded")
    if user_input:
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        response = query_bot(user_input)
        if response and hasattr(response, 'status_code') and response.status_code == 200:
            try:
                data = response.json()
                answer = data["response"]
                sources = data.get("sources", [])
                st.chat_message("assistant").markdown(answer)
                if sources:
                    st.markdown("**Sources:**")
                    for src in sources:
                        st.markdown(f"- {src}")
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                error_msg = f"Error parsing response: {str(e)}"
                with st.chat_message("assistant"):
                    st.markdown(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
        else:
            error_msg = "Error: Unable to get response from the server."
            with st.chat_message("assistant"):
                st.markdown(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})