import matplotlib
matplotlib.use('Agg')
import librosa
import librosa.display
import io
import matplotlib.pyplot as plt
import numpy as np
import soundfile
import sys
import os
import argparse



def harmonic_percussive_waveform(y, sr):
    """
    :y: numpy array
    :sr: sample rate
    :return: 
    """
    out = io.BytesIO()
    y_harm, y_perc = librosa.effects.hpss(y)
    plt.subplot(1, 1, 1)
    librosa.display.waveplot(y_harm, sr=sr, alpha=0.25)
    librosa.display.waveplot(y_perc, sr=sr, color='r', alpha=0.5)
    plt.title('Harmonic + Percussive')
    plt.tight_layout()
    plt.savefig(out, format="pdf")
    return out


# def make_spectrogram(y, sr):
#     librosa.display.specshow(librosa.amplitude_to_db(librosa.stft(y), ref=np.max), y_axis='log', x_axis='time')
#     plt.title('Power spectrogram')
#     plt.colorbar(format='%+2.0f dB')
#     plt.tight_layout()
#     out = io.BytesIO()
#     plt.savefig(out, format="pdf")
#     plt.close()
#     return out


def log_spec(y, sr):
    out = io.BytesIO()
    D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)
    plt.subplot(1, 1, 1)
    librosa.display.specshow(D, y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Log-frequency power spectrogram')
    plt.savefig(out, format="pdf")
    return out


def read_file(f):
    """
    :f: bytes like object probably referring to a wave file :)
    :return: numpy array and samplerate
    """
    y, sr = soundfile.read(f)
    return y, sr


def mono_waveform(y, sr):
    out = io.BytesIO()
    plt.figure()
    plt.subplot(3, 1, 1)
    librosa.display.waveplot(y, sr=sr)
    plt.title('Monophonic')
    plt.savefig(out, format="pdf")
    return out


def setup():
    parser = argparse.ArgumentParser(description='Make spectrograms')
    parser.add_argument('--mode', help='type of spectrogram to make')
    # harm
    # overlay the harmonic and percussive componenets to a waveform
    # mono
    # a basic waveform
    # logspec
    # show a spectrogram of the signal on the log scale
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = setup()
    print(args)
    f = io.BytesIO(sys.stdin.buffer.read().strip())

    y, sr = read_file(f)

    buf = io.BytesIO()
    if args.mode == "harm":    
        buf = harmonic_percussive_waveform(y, sr)
    elif args.mode == "mono":
        buf = mono_waveform(y, sr)
    elif args.mode == "logspec":
        buf = log_spec(y, sr)
    sys.stdout.buffer.write(buf.getvalue())
