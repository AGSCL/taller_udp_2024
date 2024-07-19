
# 0. Cosas a saber --------------------------------------------------------


#Necesitaremos tener instalado FFMPEG que es un códec de audio, para convertir los videos a audio
#
#MAC: primero instalas Homebrew, disponible en https://brew.sh/
#Luego en la terminal, ingresas (instala brew): /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
#Luego en la terminal, ingresas (instala ffmpeg): brew install ffmpeg
#Windows: 
#si tiene
#winget install "FFmpeg (Essentials Build)"

# 1. Instalación de paquetes --------------------------------------------------------


# Comprueba si tiene los paquetes externos instalados; si no, los instala y luego los "activa"
# Para ejecutar el descargador de video y el conversor de audio
if(!require(processx)){install.packages("processx")}; library(processx)
# Para detectar la cantidad de núcleos disponibles
if(!require(parallel)){install.packages("parallel")}; library(parallel)
#para transcribir usando openAI
if(!require(audio.whisper)){remotes::install_github("bnosac/audio.whisper")}; library(audio.whisper)

## 1.a. Definición de variables de entorno --------------------------------------------------------

# Defina el nombre de los archivos
youtube_url <- "https://www.youtube.com/watch?v=qqG96G8YdcE"  # Replace with your URL
output_video <- "debate.mp4"
output_audio <- "audio.wav"

## 1.b. Bajar el audio desde youtube --------------------------------------------------------

# Bajo el video usando un programa llamado youtube a DLP 
#(https://github.com/yt-dlp/yt-dlp/releases , bajar el .exe y llamarlo desde la ubicación donde lo guarde)
processx::run("C:/Users/andre/Downloads/yt-dlp.exe", args = c("-o", output_video, youtube_url))

# Usa ffmpeg para convertir el video a audio en formato WAV de 16 bits (sample_rate). Si el audio ya existe, sobreescribir
if(file.exists(output_audio)){
  processx::run("C:/Users/andre/Desktop/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe", args = c("-i", paste0(output_video, ".webm"), "-acodec", "pcm_s16le", "-ar", "16000", "-y", output_audio))
} else {
  processx::run("C:/Users/andre/Desktop/ffmpeg-master-latest-win64-gpl-shared/bin/ffmpeg.exe", args = c("-i", paste0(output_video, ".webm"), "-acodec", "pcm_s16le", "-ar", "16000", output_audio))
}

# Eliminar el archivo de video
file.remove(paste0(output_video,".webm"))

# 2. Transcribir --------------------------------------------------------

# Cuántos núcleos tiene nuestro procesador?, esto nos permite hacerlo más rápido. Borramos unopara que no colapse nuestro computador
num_cores <- detectCores() -1

# Elegimos el modelo de whisper más simple. Conste que hay otros que detectan mejor el lenguaje, como nivel pequeño (small), medio (medium) o grande (large)
model <- whisper("tiny")
trans <- predict(model, #modelo utilizado. En este caso, tiny
                 # Datos usados para predecir (el archivo de audio en 16-bit y formato .wav)
                 newdata = output_audio, 
                 # Idioma de lenguaje ("en" de Inglés [english])
                 language = "en", 
                 # duración en que el audio es dividido en partes para poder procesarlo por OPENAI  (en milisegundos)
                 # duration = 30 * 1000, #en este caso, cada 60 segundos
                 # desde cuanto parte (en milisegundos)
                 # offset = (93*60*1000)+(21*1000), 
                 # número de núcleos de CPU
                 # trim 
                 trim =T,
                 n_threads = num_cores,
                 #Obtener los puntos de tiempo de cada división
                 token_timestamps= T) # cuánto CPU utilizar para la predicción

# 3. Exportar texto --------------------------------------------------------

texto_combinado <- paste(trans$data$text, collapse = " ")

writeLines(texto_combinado, con = "debate.txt")

