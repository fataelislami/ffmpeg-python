import ffmpeg

def convert(fileName,resolution='1080p'):
    stream = ffmpeg.input(path+'/'+fileName+'.mp4')
    audio = stream.audio
    stream = ffmpeg.filter(stream, 'fps', fps=25, round='up')
    resolutionName=resolution
    if resolution=='1080p':
        resolution='hd1080'
    elif resolution=='720p':
        resolution='hd720'
    elif resolution=='480p':
        resolution='854x480'
    elif resolution=='360p':
        resolution='640x360'
    elif resolution=='240p':
        resolution='436x250'
    resize = ffmpeg.filter(stream,'scale', size=resolution)
    # resize = ffmpeg.filter(stream,'scale', size=resolution, force_original_aspect_ratio='increase')
    out = ffmpeg.output(audio, resize, 'output/'+fileName+resolutionName+'.mp4')
    out = ffmpeg.overwrite_output(out)
    ffmpeg.run(out)

path='./xfile'
pathOutput='./output'
import os

for filename in os.listdir(path):
    if filename.endswith(".mp4"):
        filename=os.path.splitext(filename)[0]
        file240p=os.path.isfile(pathOutput+'/'+filename+'240p.mp4')
        file360p=os.path.isfile(pathOutput+'/'+filename+'360p.mp4')
        file480p=os.path.isfile(pathOutput+'/'+filename+'480p.mp4')
        file720p=os.path.isfile(pathOutput+'/'+filename+'720p.mp4')
        file1080p=os.path.isfile(pathOutput+'/'+filename+'1080p.mp4')
        if not file240p:
            print("Mulai Convert File "+filename+" ke 240")
            convert(filename,'240p')
        else:
            print(filename+" 240p Sudah Ada")
        if not file360p:
            print("Mulai Convert File "+filename+" ke 360")
            convert(filename,'360p')
        else:
            print(filename+" 360p Sudah Ada")
        if not file480p:
            print("Mulai Convert File "+filename+" ke 480")
            convert(filename,'480p')
        else:
            print(filename+" 480p Sudah Ada")
        if not file720p:
            print("Mulai Convert File "+filename+" ke 720")
            convert(filename,'720p')
        else:
            print(filename+" 720p Sudah Ada")
        # if not file1080p:
        #     print("Mulai Convert File "+filename+" ke 1080")
        #     convert(filename,'1080p')
        # else:
        #     print(filename+" 1080p Sudah Ada")

