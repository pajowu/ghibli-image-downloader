# Studio Ghibli Image Downloader

[Studio Ghibli recently released over a thousand images from their beautiful films](https://www.ghibli.jp/info/013409/).
Since there is no download button for all of them, this repo contains a small script to download them.

## Installation

You need python3.
Install the dependencies in `requirements.txt`, for example like this:

```
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage

You just need to provide the script with a directory to download to images to.

```
python download.py --to OUTPUT_DIR
```

Downloading all images might take a moment.
A progress bar will be shown.

## License

This code is under a GPL 3.0, see the `LICENSE` file.
