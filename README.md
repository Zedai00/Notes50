# Notes50

A CS50 Notes And PSets Reader.

### Arguments
    -x : CS50X
    -p : CS50 Python
    -w : CS50 Web
    -g : CS50 Games
    -a : CS50 AI

### Syntax
    -argument Week: Week For Which Notes To Read 
    -argument Week/PSets: Week For Which PSets To Read

### Examples
    To Get CS50x Week 0 Notes
    - python notes50.py -x 0

    To Get CS50x Week 0 PSet Scratch
    - python notes50.py -x 0/scratch


## Programming
    Notes50 Is Written in Python
    With a mix of multiple pip libraries Which you can find in requirements.txt

    Some of the important libraries are:
        - Argparse: To Parse Arguments
        - Urllib: To Get The HTML File Of Websites
        - BeautifulSoup: To Make Usage Of HTML Easy
        - Markdownify: To Turn HTML To Markdown
        - Rich: To Print Markdown In Terminal

### Functions
    There Are Three Core Functions
    - Note: Get Notes Of The Course Week No
    - PSet: Get PSet OF The Course Week No And PSet Name
    - Get: Get HTML From The Course Website And Turn It To Markdown

### Caching
    I Used Joblib To Cache The Results As Getting The HTML Causes Some Delay
    So By Using Caching It Can Return Previously Used Results Without Any Wasted Time
    It Uses Appdirs To Get The User Cache Directory
    The First Time Maybe Slow As It Will Cache The First Results.
