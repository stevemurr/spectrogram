build:
	docker build --rm -t librosa .
example:
	make build
	cat test.wav | docker run -i librosa