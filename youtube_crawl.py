import os
from youtube_dl import YoutubeDL


audio_list_file = './playlists.txt'
ydl_opts = {

    'noplaylist': True,
    'extract-audio': True,
    'ignoreerrors': True,
    'nooverwrites': True,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '256'
    }],
    'postprocessor_args': [
        '-ar', '22050', '-acodec', 'pcm_s16le'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': False,
    'outtmpl': 'audio/%(title)s.%(etx)s',
    'quiet': False
}


def normalize_audio_name(audio_name):
    audio_name = audio_name.lower()
    audio_name = audio_name.replace(' ','')
    return audio_name


def get_raw_audio(audio_list_file):
    print("Crawling raw audio from youtube")
    # Make audio_list
    audio_list=[]
    with open(audio_list_file) as f:
        lines = f.readlines()
        for line in lines:
            audio_url = line[:-1]
            audio_list.append(audio_url)
    # Make new directory if not exists
    audio_path = 'audio'
    if not os.path.exists(audio_path):
        os.makedirs(audio_path)
    # Download audio
    for audio in audio_list:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(audio, download=True)
            audio_title = info_dict.get('title', None)
    # Normalize audio name
    for fn in os.listdir(audio_path):
        new_fn = normalize_audio_name(fn)
        os.rename(os.path.join(audio_path, fn), os.path.join(audio_path, new_fn))


if __name__ == '__main__':
    get_raw_audio(audio_list_file)
