import sys
from re import *

md_header1 = r"^#[\s]+(.+)(?:\n)"
md_header2 = r"^##[\s]+(.+)(?:\n)"
md_header3 = r"^###[\s]+(.+)(?:\n)"
md_bold = r"\*\*(.+?)\*\*"
md_italic = r"\*(.+?)\*"
md_ordered_list = r"^(\d+\. .*(?:\n\d+\. .*)*)"
md_list_item = r"^\d+\. ([^\n]+)"
md_link = r"\[([\d\w]+)\]\((.+)\)"
md_image = r"\!\[([\d\w]+)\]\((.+)\)"

html_header1 = r"<h1>\1</h1>\n"
html_header2 = r"<h2>\1</h2>\n"
html_header3 = r"<h3>\1</h3>\n"
html_bold = r"<b>\1</b>"
html_italic = r"<i>\1</i>"
html_ordered_list = r"<ol>\n\1\n</ol>"
html_list_item = r'<li>\1</li>'
html_link = r'<a href="\2">\1</a>'
html_image = r'<img src="\2" alt="\1"/>'

def md_html(linha):
    res = linha

    res = sub(md_header1, html_header1, res, flags=M)
    res = sub(md_header2, html_header2, res, flags=M)
    res = sub(md_header3, html_header3, res, flags=M)
    res = sub(md_bold, html_bold, res, flags=M|U)
    res = sub(md_italic, html_italic, res, flags=M|U)
    res = sub(md_ordered_list, html_ordered_list, res, flags=M)
    res = sub(md_list_item, html_list_item, res, flags=M)
    res = sub(md_image, html_image, res)
    res = sub(md_link, html_link, res)

    return res

ficheiro_input = sys.argv[1]
ficheiro_output = sys.argv[2]

res = ""

with open(ficheiro_input, 'r') as f_in:
    res = md_html(f_in.read())

with open(ficheiro_output, 'w') as f_out:
    f_out.write(res)
