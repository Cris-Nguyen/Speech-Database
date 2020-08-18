import os
import pysrt
from pydub import AudioSegment
import pandas as pd
from normalize import normalize_text
import argparse


# Define lambda function convert time to miliseconds 
time_to_ms = lambda x: (x.hours*3600 + x.minutes *60 + x.seconds) * 1000 + x.milliseconds


def prepare_data(raw_audio_dir, audio_outdir, csv_output):
    data_df = pd.DataFrame(columns=['audio', 'sub'])
    audio_list, sub_list = [], []
    sub_file = os.listdir(raw_audio_dir)
    # Interative over files
    for fn in sub_file:
        if fn.endswith(".wav"):
            # Audio and sub dir
            audio_path = os.path.join(raw_audio_dir, fn)
            audio_name, audio_format = fn.split('.')
            audio_sub_name = f'{audio_name}.srt'
            audio_sub_path = os.path.join(raw_audio_dir, audio_sub_name)
            #Read data
            audio = AudioSegment.from_file(audio_path)
            subs = pysrt.open(audio_sub_path, encoding = 'utf-8')
            for sub in subs:
                # Extract time
                start_ms = time_to_ms(sub.start)
                end_ms = time_to_ms(sub.end)
                audio_extract_name = f'{audio_outdir}{audio_name}_{start_ms}_{end_ms}.wav'
                text = normalize_text(str(sub.text))
                # CSV Columns
                audio_list.append(audio_extract_name)
                sub_list.append(text)
                # Extract to file
                extract = audio[start_ms:end_ms]
                extract.export(audio_extract_name, format="wav")
    # To csv file
    data_df['audio'], data_df['sub'] = audio_list, sub_list
    data_df.to_csv(csv_output, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--raw_audio_dir', type=str, default='audio', help='Raw audio folder')
    parser.add_argument('--audio_outdir', type=str, default='', help='Folder to save postprocess audio')
    parser.add_argument('--csv_output', type=str, default='', help='Path to save csv file')
    args = parser.parse_args()

    prepare_data(args.raw_audio_dir, args.audio_outdir, args.csv_output)
