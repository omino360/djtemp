import os
# write a html file
def write_html(html, title):
    with open(title, "w") as f:
        f.write(html)
# create a html file
def create_html(html, title):
    if os.path.exists(title):
        print("File already exists")
        overwrite = input("Overwrite? (y/n): ")
        if overwrite == "y":
            write_html(html, title)
    else:
        write_html(html, title)
#read a html file
def read_html(title):
    with open(title, "r") as f:
        return f.read()
# create a html class       
class html():
    def body(kwarg):
        return f"<body>{kwarg}</body>"
    def div(kwarg):
        return f"<div>{kwarg}</div>"
    def p(kwarg):
        return f"<p>{kwarg}</p>"
    def h1(kwarg):
        return f"<h1>{kwarg}</h1>"
    def h2(kwarg):
        return f"<h2>{kwarg}</h2>"
    def h3(kwarg):
        return f"<h3>{kwarg}</h3>"
    def h4(kwarg):
        return f"<h4>{kwarg}</h4>"
    def h5(kwarg):
        return f"<h5>{kwarg}</h5>"
    def h6(kwarg):
        return f"<h6>{kwarg}</h6>"
    def a(kwarg, href):
        return f"<a href='{href}'>{kwarg}</a>"
    def img(src, alt):
        return f"<img src='{src}' alt='{alt}'>"
    def br():
        return "<br>"
    def hr():
        return "<hr>"
    def head(kwarg):
        return f"<head>{kwarg}</head>"
    def title(kwarg):
        return f"<title>{kwarg}</title>"
    def meta(name, content):
        return f"<meta name='{name}' content='{content}'>"
    def link(rel, href):
        return f"<link rel='{rel}' href='{href}'>"
    def script(src):
        return f"<script src='{src}'></script>"
    def style(kwarg):
        return f"<style>{kwarg}</style>"
    def ul(kwarg):
        return f"<ul>{kwarg}</ul>"
    def ol(kwarg):
        return f"<ol>{kwarg}</ol>"
    def li(kwarg):
        li=""
        for item in kwarg:
            li += f"<li>{item}</li>"
        return li
    def table(kwarg):
        return f"<table>{kwarg}</table>"
    def tr(kwarg):
        return f"<tr>{kwarg}</tr>"
    def th(kwarg):
        return f"<th>{kwarg}</th>"
    def td(kwarg):
        return f"<td>{kwarg}</td>"
    def form(kwarg):
        return f"<form>{kwarg}</form>"
    def input(kwarg):
        return f"<input>{kwarg}</input>"
    def button(kwarg):
        return f"<button>{kwarg}</button>"
    
   

file = "index.html" 
text = "Hello World!"
list_1 = ["Hello", "World", "This", "Is", "A", "List"]
p = html.p(text)
div = html.div(p)
li = html.li(list_1)
index = html.body(div + li)
create_html(index, file)
print(read_html(file))



