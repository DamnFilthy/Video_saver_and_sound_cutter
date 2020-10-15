#Add the required libraries
import youtube_dl
import os
import moviepy.editor

# Download video loop
flag = True
while flag == True:
    video_link = input('input link to vk video witch you want download:  ')

    # youtube_dl logic
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
         ydl.download([video_link])

    # Restart loop
    restart = input('\nDownload one more video?(y/n) :  ')
    if restart.lower() == 'y':
        continue
    else:
        flag = False

# Audio Cutter
cut_audio = input('\nCut audio from your videos?(y/n)  :  ')
# Choice fork
if cut_audio.lower() == 'y':
    # Our catalog
    directory = 'C:\\Users\\User\\Desktop\\python_pet\\video_saver_and_cutter'

    # all files to list
    files = os.listdir(directory)

    # Filter list
    videos = filter(lambda x: x.endswith('.mp4'), files)

    # Create usable names
    clean_names = []
    for video in videos:
        name = video.replace(".mp4", "")
        clean_names.append(name)

    # Cut audio from video
    for name in clean_names:
        # Programm logic
        video = moviepy.editor.VideoFileClip(name+'.mp4')
        audio = video.audio
        audio.write_audiofile(name+'.mp3')
elif cut_audio.lower() == 'n':
    print('Thanks for using this programm. Bye.')
