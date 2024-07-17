# Un Vistazo al Debate Biden-Trump

### Autor: Andrés González-Santa Cruz
### ORCID: [https://orcid.org/0000-0002-5166-9121](https://orcid.org/0000-0002-5166-9121)

## ¿Cómo me puedo hacer una idea respecto a lo que se habló ahí?

### Temario:

1. **Un ejemplo transcribiendo audio mediante modelos de lenguaje en grandes volúmenes en Python**
   - Generamos el archivo  [https://raw.githubusercontent.com/AGSCL/taller_udp_2024/main/debate.txt](debate.txt)
   - Los paquetes utilizados fueron los siguientes:
   - **yt-dlp**: Permite descargar y extraer audio de videos de YouTube.
   - **moviepy**: Proporciona herramientas para manipular archivos de audio y video.
   - **pydub**: Facilita el procesamiento de audio, como dividir archivos de audio en chunks.
   - **SpeechRecognition**: Biblioteca para reconocer el habla y convertirla a texto.
   - **whisper**: Modelo de transcripción automática de OpenAI.
   - **setuptools-rust**: Requerido para la instalación de algunos paquetes basados en Rust.
   - **ffmpeg-python**: Enlace a FFmpeg para la manipulación de multimedia. [https://ffmpeg.org/download.html](FFmpeg)
   - **openai-whisper**: Biblioteca específica para el modelo Whisper de OpenAI.

2. **Procesar transcripciones a R**
   - Utilizando el archivo [https://raw.githubusercontent.com/AGSCL/taller_udp_2024/main/debate.txt](debate.txt)

3. **Algunos ejemplos de análisis descriptivos de texto en R**
   - Nube de palabras
   - Palabras más frecuentes
   - Trigrama

4. **Conceptos básicos**
   - Término
   - Vectores y matrices de texto
   - Stopwords

5. **Proyecciones de análisis inferenciales**
