# Arachnida

Arachnida is a python projetc separate in two script :

- Spider : scrap recursively image from a web URL
- Scorpion: display several informations on a given image (EXIF, shape ...)

## Spider

```bash
usage : /spider [-rlp] URL

Spider allow you to extract all the images form a website, recursively, by providing a url as a parameter.

-r        : recursively download the images in the URL
-rl [N]   : indicates the maximum depth level of the recursive download. If not indicated, it will be 5.
-p [PATH] :indicates the path where the downloaded files will be saved. If not specified, ./data/ will be used.

(folowing extension are managed: .jpg/jpeg | .png | .gif | .bmp)
```

Made with [Requests](https://pypi.org/project/requests/) and [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

## Scorpion

```bash
Scorpion display basic attributes such as the creation date, as well as EXIF data.

usage : ./scorpion FILE1 [FILE2 ...]
```

Made with [PIL](https://pypi.org/project/Pillow/)