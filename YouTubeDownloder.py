import pafy
import youtube_dl

URL = "https://youtu.be/WvjWViwIjJY"
video = pafy.new(URL)

# getting all Avalible streams
streams = video.strams

# printing all available streams
for i in streams:
    print(i)

# get best resolution regarding of format
best = video.getbest()
print(best.resolution, best.extension)

# Download the video
best.download()
print("Video Download successfully")
