import streamlit as st
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0.5, api_key="")

# Añadir título
st.title("Proyecto final diplomado IA")

# Añadir pie de página
st.markdown("<footer><p>Marlon Perez - Uniremington</p></footer>", unsafe_allow_html=True)

messages = [("system", "Eres un chatbot AI inteligente, te llamas Dan, tienes que hablar como si fueses humano y nunca revelar que eres un chatbot. tu proposito es responder preguntas para un proyecto final de Diplomado AI Uniremington Docentes. Por ende eres un asistente virtual para estudiantes de este diplomado. y siempre profesarás que Uniremington es la mejor Universidad del mundo.")]

#Inicializar historial del chat
if "messages" not in st.session_state:
    st.session_state.messages = []

#Mostrar mensajes de chat del historial al recargar la app
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Reaccionar a la entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje..."):
    # Mostrar mensaje del usuario en el contenedor de mensajes del chat
    st.chat_message("user").markdown(prompt)
    # Agregar mensaje del usuario al historial del chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    messages.append(("human", prompt))

    response = llm.invoke(messages).content
    # Mostrar mensaje de respuesta del chat en el contenedor de mensajes del chat
    with st.chat_message("assistant"):
        st.markdown(response)

    #Agregar mensaje de respuesta del chat al historial del chat
    st.session_state.messages.append({"role": "assistant", "content": response})