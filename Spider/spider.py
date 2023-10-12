#!/usr/bin/env python3

import os
from argv_handle import *
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

global level
level = 0

def download_img(path, opt):
    url =  urljoin(opt.url, path)
    res = requests.get(url, stream=True)
    slash = path.rfind("/")
    path = path[slash + 1:]
    files_in_directory = os.listdir(opt.path)
    if path in files_in_directory:
        return 
    path = os.path.join(opt.path, path)
    if not(path.endswith(".jpg") or path.endswith(".jpeg") or path.endswith(".png") or path.endswith("gif") or path.endswith(".bmp")):
        return
    if res.status_code == 200:
        print(f"downloading {url}")
        with open(path, "wb") as file:
            file.write(res.content)

def down(data, opt):
    imgs = data.find_all('img')
    src_list = []
    for img in imgs:
        src = img.get('src')
        if src:
            src_list.append(src)
    for src in src_list:
        download_img(src, opt)
    return 


def scrap(opt, url: str, lst: list[str]):
    global level
    print(f"going to : {url}")
    try:
        res = requests.get(url, timeout=1, stream=True)
    except requests.exceptions.Timeout:
        return
    except Exception as e:
        error_arg(f"{e}")
    if res.status_code != 200:
        return 
    data = bs(res.text, 'html.parser')

    if not os.path.exists(opt.path):
        os.mkdir(opt.path)

    if opt.r == True: 
        a_tags = data.find_all("a")
        if len(a_tags) == 0:
            return
        for a in a_tags:
            href = a.get('href')
            new_url = urljoin(url, href)
            if not (href.startswith("http") or new_url == url or href.startswith("#")):
                if new_url in lst:
                    return
                level += 1
                lst.append(new_url)
                down(data, opt)
                if opt.l == True:
                    if opt.N < level:
                        return 
                scrap(opt, new_url, lst)

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
    scrap(option, option.url, [option.url])

if __name__ == "__main__":
    main()