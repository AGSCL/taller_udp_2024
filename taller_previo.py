# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:44:36 2024

@author: Andres Gonzalez-Santa Cruz
"""

# 0. importar audio ---------------------------------------------------

#_#_#_#_#_#_#_#_#_#_#_#_#_#_
#instalar paquete
!pip install yt-dlp

#_#_#_#_#_#_#_#_#_#_#_#_#_#_
#importar datos
import yt_dlp
from moviepy.editor import AudioFileClip
import os

# URL del video de YouTube
url = 'https://www.youtube.com/watch?v=qqG96G8YdcE'  # Ejemplo de URL de un video disponible

# Opciones para yt-dlp
# Opciones para yt-dlp
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'debate.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }],
}

try:
    # Descargar y convertir el audio usando yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print(f'Audio extraído y guardado como debate.wav')
except Exception as e:
    print(f"Se ha producido un error: {e}")

# 1. obtener grabación ---------------------------------------------------

#_#_#_#_#_#_#_#_#_#_#_#_#_#_
#_#_#_#_#_#_#_#_#_#_#_#_#_#_
#cerrar memoria y limpiar
import gc
gc.collect()
import sys
sys.modules[__name__].__dict__.clear()

#_#_#_#_#_#_#_#_#_#_#_#_#_#_
#instalar
!pip install pydub
!pip install SpeechRecognition
!pip install whisper
!pip3 install setuptools-rust
!pip install ffmpeg-python
!pip install openai-whisper

#Para cerciorarnos de que se encuentra instalado ffmpeg para codificar audio: https://ffmpeg.org/download.html.
os.system('ffmpeg')
os.system('ffmpeg -version')

os.system("import whisper")
os.system('ffmpeg')
os.system('python3 import ffmpeg')
os.system('python import ffmpeg')


#_#_#_#_#_#_#_#_#_#_#_#_#_#_
#_#_#_#_#_#_#_#_#_#_#_#_#_#_
# IMPORTAR

from pydub import AudioSegment
from pydub.silence import split_on_silence
import time
import os
from os import path
import speech_recognition as sr
import ffmpeg
import whisper

#_#_#_#_#_#_#_#_#_#_#_#_#_#_
# Procesar el archivo de audio
sound_file = AudioSegment.from_wav("debate.wav")
print(f'Duración del archivo de audio: {len(sound_file)} ms')

#_#_#_#_#_#_#_#_#_#_#_#_#_#_
#dividir por espacios de tiempo
start_time = time.time()
print(f"Start time: {start_time} seconds\n")
# cuando hay silencios
#audio_chunks = split_on_silence(sound_file, min_silence_len=500, silence_thresh=-40 )
# para exigir silencios más cortos, cosa de tener menos chunks 
def split_on_shorter_silence(sound_file, silence_thresh=-40, min_silence_len=200):
  """
  Splits an audio file into segments based on silence detection with a shorter silence threshold.

  Args:
      sound_file (AudioSegment): The audio file to split.
      silence_thresh (int, optional): The dBFS threshold below which a segment is considered silent. Defaults to -40.
      min_silence_len (int, optional): The minimum duration (in milliseconds) for a segment to be considered silence. Defaults to 200.

  Returns:
      list[AudioSegment]: A list of AudioSegment objects representing the split audio segments.
  """

  # Split the audio using the adjusted parameters
  chunks = split_on_silence(sound_file, min_silence_len=min_silence_len, silence_thresh=silence_thresh)

  return chunks

audio_chunks = split_on_shorter_silence(sound_file)

count = len(audio_chunks)
print("El audio se divide en " + str(count) + " chunks \n")
#El audio se divide en 1507 chunks 

# Cargar el modelo Whisper para transcribir
model = whisper.load_model("medium")
transcript = ""
for i, chunk in enumerate(audio_chunks):
    out_file = f"chunks/chunk{i}.wav"
    print(f"\r\nExportando >> {out_file} - {i + 1}/{len(audio_chunks)}")
    chunk.export(out_file, format="wav")
    result = model.transcribe(out_file, language="en")
    transcript_chunk = result["text"]
    print(transcript_chunk)

    transcript += " " + transcript_chunk

    # Elimina el chunk después de traducirlo
    os.remove(out_file)
  
print("Transcripción completa del audio:")
print(transcript)

#exportar texto
with open('debate.txt', 'w', encoding='utf-8') as f:
    f.write(transcript)