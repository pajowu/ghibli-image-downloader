import requests
from bs4 import BeautifulSoup
import re
import argparse
from pathlib import Path
from tqdm import tqdm
from tqdm.contrib import tenumerate


def download_works(out_dir):
    works_re = r"https://www.ghibli.jp/works/[-\w]*?/?#frame"
    start_url = "https://www.ghibli.jp/works/"
    start_req = requests.get(start_url)

    for work_url in tqdm(re.findall(works_re, start_req.text), desc="total"):
        download_work(out_dir, work_url)


def download_work(out_dir, work_url):
    work_req = requests.get(work_url)
    work_name = work_url.split("/")[4]
    work_dir = out_dir / work_name
    work_dir.mkdir(exist_ok=True)
    soup = BeautifulSoup(work_req.text, features="html.parser")
    image_tags = soup.find_all(class_="panelarea")
    for i, tag in tenumerate(image_tags, desc=f"{work_name}"):
        image_url = tag.get("href")
        output_name = image_url.split("/")[-1]
        output_filename = work_dir / f"{i:03}-{output_name}"

        image_req = requests.get(image_url)
        with open(output_filename, "wb") as f:
            f.write(image_req.content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--to", type=Path, required=True)
    args = parser.parse_args()

    args.to.mkdir(exist_ok=True)

    download_works(args.to)
