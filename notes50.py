from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from rich.markdown import Markdown
from rich.console import Console

def main():
    con = Console()
    url = "https://cs50.harvard.edu/python/2022/psets/0/indoor/"
    httpsrequest = Request(url, headers={"Accept": "application/json"})
    html = urlopen(httpsrequest).read().decode()
    html = html.replace('“','"').replace('”','"')
    main = BeautifulSoup(html, "lxml")
    main = main.main
    with open("test.md", "w") as t:
        t.write(main.prettify())
    markdown = md(main.prettify())
    ri = Markdown(markdown)
    con.print(ri)
if __name__ == "__main__":
    main()
