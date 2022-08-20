from urllib.error import HTTPError
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from rich.markdown import Markdown
from rich.console import Console
import sys
import argparse


def main():
    args = parse_args()
    if f"{args.x}".isnumeric() or f"{args.p}".isnumeric():
        notes(args)
    elif args.x or args.p:
        psets(args)
    else:
        print("Unknown Error")
        sys.exit(1)


def notes(args):
    if args.x:
        url = f"https://cs50.harvard.edu/x/2022/notes/{args.x}"
    elif args.p:
        url = f"https://cs50.harvard.edu/python/2022/notes/{args.p}"
    else:
        print("Plese Check Your Argumnet")
        sys.exit(1)
    try:
        get(url)
    except HTTPError:
        print("Url Not Found Please Check Your Argumnet")
        sys.exit(1)


def psets(args):
    if args.x:
        url = f"https://cs50.harvard.edu/x/2022/psets/{args.x}"
    elif args.p:
        url = f"https://cs50.harvard.edu/python/2022/psets/{args.p}"
    else:
        print("Plese Check Your Argumnet")
        sys.exit(1)
    try:
        get(url)
    except HTTPError:
        print("Url Not Found Please Check Your Argumnet")
        sys.exit(1)


def get(url):
    con = Console()
    html = urlopen(Request(url)).read().decode()
    main = BeautifulSoup(html, "lxml")
    main = main.main
    markdown = md(main.prettify())
    ri = Markdown(markdown)
    con.print(ri)


def parse_args():
    parser = argparse.ArgumentParser(
        description="CS50 Notes And Problem Sets Reader In Terminal",
        epilog="Usage:\r\n  For Week Notes:\n    python notes50.py -x 0\n    python notes50.py -p 0\n  For Week Pset:\n    python notes50.py -x 0/scratch\n    python notes50.py -p 0/indoor\n",
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-x", metavar="Week, Week/PSet",
                        help="CS50x Week Notes or Week/PSet Name")
    parser.add_argument("-p", metavar="Week, Week/PSet",
                        help="CS50 Python Week Notes or Week/PSet Name")
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)
    else:
        return parser.parse_args()


if __name__ == "__main__":
    main()
