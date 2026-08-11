from prompt_toolkit import prompt
from rich.console import Console
from rich.markdown import Markdown

def inputs(message=None):
    lines = []
    if message:
        print(message,end="")
    while True:
        line = input("> ")
        if line == "/send":
            break

        lines.append(line)
    message = "\n".join(lines)

    return message
def print_md(s):
    if s:
        console = Console()
        console.print(Markdown(s))

def return_md():
    a = """
# head
```python
# print content
print("hello world")
print("hahaha")
```
this is a `cool` code.

study:
- do it
- do it
- do it

    """
    return a 
m = inputs()
print(f"you sends:{m}")
print(return_md())
print_md(return_md())
