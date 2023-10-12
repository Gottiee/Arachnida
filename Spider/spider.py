import os
from argv import *
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

def download_img(path, opt):
    url =  urljoin(opt.url, path)
    res = requests.get(url, stream=True)
    slash = path.rfind("/")
    path = path[slash + 1:]
    path = urljoin(opt.path, path)
    if res.status_code == 200:
        with open(path, "wb") as file:
            file.write(res.content)

def scrap(opt):
    res = requests.get(opt.url)
    print(f"Request status code: {res.status_code}")
    data = bs(res.text, 'html.parser')
    imgs = data.find_all('img')

    if not os.path.exists(opt.path):
        os.mkdir(opt.path)

    src_list = []
    for img in imgs:
        src = img.get('src')
        if src:
            src_list.append(src)
    print(f"Soure list : {src_list}")
    for src in src_list:
        download_img(src, opt)

def main():
    """
usage : /spider [-rlp] URL

Spider allow you to extract all the images form a website, recursively, by providing a url as a parameter.

-r        : recursively download the images in the URL
-rl [N]   : indicates the maximum depth level of the recursive download. If not indicated, it will be 5.
-p [PATH] :indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used.

(folowing extension are managed: .jpg/jpeg | .png | .gif | .bmp)
    """
    option = argv_handler()
    print("Option seleted : ", option)
    scrap(option)

if __name__ == "__main__":
    main()