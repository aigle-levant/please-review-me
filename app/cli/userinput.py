"""
what does this do: asks user for input file path, confirms with user the file and all
input: file path
"""

# imports
from pathlib import Path
from config import console

def read_input() -> Path | None:
    print("Say 'stop' or 'quit' to exit process.")
    while True:
        filepath = console.input(f"Sigh...which file do you want me to review?: ").strip()
        path = Path(filepath)
        command = filepath.lower()
        li = ["stop", "quit"]
        if (command in li):
            print("Alright, alright, time's up. Let's wind down.")
            return
        if not path.exists():
            console.print("[red]File doesn't exist. What are you giving me, [i]air[/i]?[/red]\n")
            continue
        if not path.is_file():
            console.print("[red]Developers these days...that's [b]not[/b] a file![/red]\n")
            continue
        if path.suffix != ".py":
            console.print("[red]I read only Python, duh.[/red]")
            continue
        console.print("[green]Alright, sigh...let me review your code for any weird bugs you'd have caused...[/green]")
        return path

