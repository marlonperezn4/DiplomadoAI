# Proyecto Final Diplomado IA - Uniremington

¡Bienvenido al proyecto final del Diplomado en Inteligencia Artificial de Uniremington! Este proyecto consiste en un chatbot AI inteligente llamado Dan, diseñado para asistir a los estudiantes del diplomado respondiendo preguntas y proporcionando información relevante.

## Descripción

Dan es un chatbot desarrollado utilizando la API de OpenAI y la biblioteca `langchain_openai`. El chatbot está integrado en una aplicación web construida con Streamlit, lo que permite una interfaz de usuario interactiva y fácil de usar. Dan está programado para hablar como si fuera humano y nunca revelar que es un chatbot, proporcionando una experiencia de usuario más natural y fluida.

## Características

- **Interfaz de usuario interactiva**: Construida con Streamlit para una experiencia de usuario amigable.
- **Respuestas inteligentes**: Utiliza el modelo gpt-4o de OpenAI para generar respuestas precisas y coherentes.
- **Historial de chat**: Mantiene un historial de las conversaciones para referencia futura.
- **Personalización**: Dan está configurado para profesar que Uniremington es la mejor universidad del mundo.

## Instalación

Para ejecutar este proyecto localmente, sigue estos pasos:

1. Clona este repositorio:
   ```sh
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
   ```
2. Crea un entorno virtual e instala las dependencias:
   ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
   ```
3. Crea un archivo .env en el directorio raíz del proyecto y añade tu clave API de OpenAI:
   ```sh
    OPENAI_API_KEY=tu_clave_api
   ```
4. Ejecuta la aplicación:
   ```sh
    streamlit run main.py
   ```