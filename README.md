# Un Vistazo al Debate Biden-Trump

### Autor: Andrés González-Santa Cruz
### ORCID: [https://orcid.org/0000-0002-5166-9121](https://orcid.org/0000-0002-5166-9121)

## ¿Cómo me puedo hacer una idea respecto a lo que se habló ahí?

### Temario:

00. Se recomienda trabajar con R, version 4.4.0.

0. Al principio tenemos dos opciones: o bajar el audio y transcribir en Python o en R. Ambas opciones requieren que instalen [FFmpeg](https://ffmpeg.org/download.html), un reconocido codificador de audio para transformarlo desde formato video a .wav, y un programa para bajar video llamado [yt-dlp](https://github.com/yt-dlp/yt-dlp), que baja archivos de audio o video. Si no quiere arriesgarse a instalar archivos de terceros, puede saltar el video introductorio y el punto 1 a continuación.

1.a. **Un ejemplo transcribiendo audio mediante modelos de lenguaje en grandes volúmenes en Python ((taller_previo.py)[taller_previo.py])** 
   - Generamos el archivo  [https://raw.githubusercontent.com/AGSCL/taller_udp_2024/main/debate.txt](debate.txt)
   - Los paquetes utilizados fueron los siguientes:
   - **yt-dlp**: Permite descargar y extraer audio de videos de YouTube.
   - **moviepy**: Proporciona herramientas para manipular archivos de audio y video.
   - **pydub**: Facilita el procesamiento de audio, como dividir archivos de audio en chunks.
   - **SpeechRecognition**: Biblioteca para reconocer el habla y convertirla a texto.
   - **whisper**: Modelo de transcripción automática de OpenAI.
   - **setuptools-rust**: Requerido para la instalación de algunos paquetes basados en Rust.
   - **ffmpeg-python**: Enlace a FFmpeg para la manipulación de multimedia.
   - **openai-whisper**: Biblioteca específica para el modelo Whisper de OpenAI.

1.b. **Un ejemplo transcribiendo audio mediante modelos de lenguaje en grandes volúmenes en R ((taller_previo.R)[taller_previo.R])**
   - Generamos el archivo  [https://raw.githubusercontent.com/AGSCL/taller_udp_2024/main/debate.txt](debate.txt)
   - Los paquetes utilizados fueron los siguientes:
   - **yt-dlp**: Permite descargar y extraer audio de videos de YouTube.
   - **processx**: Para ejecutar el descargador de video y el conversor de audio.
   - **parallel**: Para detectar la cantidad de núcleos disponibles en la CPU del computador.
   - **whisper**: Para transcribir usando openAI. Biblioteca específica para el modelo Whisper de OpenAI.
   - **ffmpeg**: Enlace a FFmpeg para la manipulación de multimedia. [https://ffmpeg.org/download.html](FFmpeg)

2. **Procesar transcripciones a R**
   - Utilizando el archivo (si usted no quiere transcribir la entrevista por usted mismo, omita el paso 1 y limítese a bajar el siguiente archivo de texto) [https://raw.githubusercontent.com/AGSCL/taller_udp_2024/main/debate.txt](debate.txt)

3. **Algunos ejemplos de análisis descriptivos de texto en R**
   - Nube de palabras
   - Palabras más frecuentes
   - Trigrama

4. **Conceptos básicos**
   - Término
   - Vectores y matrices de texto
   - Stopwords

5. **Proyecciones de análisis inferenciales**
