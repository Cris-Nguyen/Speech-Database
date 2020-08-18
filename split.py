import os
import pandas as pd
from sklearn.model_selection import train_test_split
import argparse


def split_data(csv_file_path, output_dir):
    # Read data
    data = pd.read_csv(csv_file_path)
    audio, sub = data['audio'], data['sub']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(audio, sub, test_size=0.2)

    # Write to correct format files
    with open(os.path.join(output_dir, 'training.txt'), 'w') as f:
        for audio, sub in zip(X_train, y_train):
            f.write(f'{os.path.join(os.getcwd(), audio)}|{sub}\n')

    with open(os.path.join(output_dir, 'testing.txt'), 'w') as f:
        for audio, sub in zip(X_test, y_test):
            f.write(f'{os.path.join(os.getcwd(), audio)}|{sub}\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', type=str, default='', help='Folder to save')
    parser.add_argument('--csv_file_path', type=str, default='', help='Path to save csv file')
    args = parser.parse_args()

    split_data(args.csv_file_path, args.output_dir)
