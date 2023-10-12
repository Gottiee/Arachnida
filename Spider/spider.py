from sys import argv
from argv import *
import argparse

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

if __name__ == "__main__":
    main()