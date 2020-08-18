import os


audio_path = 'audio'


def get_transcript(audio_path):
    files = os.listdir(audio_path)
    for fn in files:
        file_path = os.path.join(audio_path, fn)
        os.system(f'autosub -S vi -D vi {file_path}')


if __name__ == '__main__':
    get_transcript(audio_path)
