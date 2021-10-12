from moviepy.editor import *

mp4_file = "video.mp4" # source filename
mp3_file = "audio.mp3" # target filename

videoClip = VideoFileClip(mp4_file)
audioclip = videoClip.audio
audioclip.write_audiofile(mp3_file)
audioclip.close()
videoClip.close()