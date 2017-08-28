# Dockerized Spectrograms

# Installation

- Docker

# Usage

Cat a wave file into the docker container to retrieve the spectrogram as a pdf

`cat audio.wav | docker -i librosa --mode mono > out.pdf && open out.pdf`

