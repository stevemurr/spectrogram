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


def make_spectrogram(stft):
    librosa.display.specshow(librosa.amplitude_to_db(stft, ref=np.max), y_axis='log', x_axis='time')
    plt.title('Power spectrogram')
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    out = io.BytesIO()
    plt.savefig(out, format="pdf")
    plt.close()
    return out


def read_file(f):
    y, sr = soundfile.read(f)
    D = librosa.cqt(y)
    return D, None


if __name__ == '__main__':

    f = io.BytesIO(sys.stdin.buffer.read().strip())

    stft, err = read_file(f)
    if err != None:
        print(err)
        sys.exit()
    buf = make_spectrogram(stft)
    sys.stdout.buffer.write(buf.getvalue())
