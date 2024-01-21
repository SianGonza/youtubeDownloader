from pytube import YouTube
from sys import argv

# Get the YouTube link from the command line arguments
link = argv[1]

# Create a YouTube object
yt = YouTube(link)

# Print video title and views
print('Title: ', yt.title)
print('Views: ', yt.views)

# Get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download the stream to the specified directory
stream.download("C:/Users/siana/Downloads")
