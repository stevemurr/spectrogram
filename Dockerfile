FROM nutzio/librosa-env
RUN apk update --no-cache
RUN apk add build-base python3-dev libffi-dev freetype-dev libpng-dev libsndfile-dev
RUN pip install soundfile matplotlib 
ADD spectrogram.py spectrogram.py
ENTRYPOINT ["python", "-u", "spectrogram.py"]
