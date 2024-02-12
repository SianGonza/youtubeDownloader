from sys import argv

from pytube import YouTube

# Para pasar el argumento [LINK DE YOUTUBE]
link = argv[1]

yt = YouTube(link)

# Imprime  el titulo y visitas
print("Title: ", yt.title)
print("Views: ", yt.views)

# Obtiene el video con la resolucion mas alta y lo descarga en la carpeta descargas
stream = yt.streams.get_highest_resolution()

# Reemplazar directorio por el elegido
stream.download("C:/Users/siana/Downloads")
