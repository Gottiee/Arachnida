from sys import argv
from spider import main

class option:
    def __init__(self, url: str) -> None:
        self.url = url
        self.r = False
        self.l = False
        self.N = 5
        self.path = "./data/"
        
    def __str__(self):
        return f"{self.__dict__}"
    
    def set_r(self):
        self.r = True
    def set_l(self):
        self.l = True
    def set_N(self, N: int):
        self.N = N
    def set_url(self, url:str):
        self.url = url
    def set_path(self, path:str):
        self.path = path

def error_arg(err: str) -> None:
    print(err)
    exit(1)

def managed_level(args, url: list):

    if len(args) != 1:
        try:
            integer = int(args[0])
        except ValueError:
            error_arg(ValueError.__doc__)
        url.pop(0)
        return integer
    return 5

def managed_path(args, url: list):

    if len(args) != 1:
        try:
            integer = int(args[0])
        except ValueError:
            error_arg(ValueError.__doc__)
        url.pop(0)
        return integer
    return 5

def managed_option() -> option:
    values = option(None)

    url = argv[1:]

    for i, args in enumerate(argv):
        if args.startswith('-'):
            url = url[i:]
            for char in args: 
                if char == 'r':
                    option.set_r(values)
                if char == 'l':
                    option.set_l(values)
                    if len(argv) - i > 1:
                        option.set_N(values, managed_level(argv[1 + 1:], url))
                        if len(argv) - 1 > 2:
                            argv.pop(i)
                if char == 'p':
                    if len(argv) - i > 2:
                        option.set_path(values, argv[1 + i])
                        url.pop(0)
                        argv.pop(i)
    if len(url) != 1:
        error_arg(f"No URL or several URL provided: {main.__doc__}")
    option.set_url(values, url[0])
    return values

def argv_handler() -> option:
    if len(argv) < 2:
        error_arg(f"{main.__doc__}")
    else: 
        return managed_option()