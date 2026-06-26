"""
what does this do: cleans up and sets up a nice CLI interface for your response
input: agent's response
flow: userinput -> validate -> prompt -> agent -> here
"""
from config import console
from rich.panel import Panel
from models.models import Response

def interface(res: Response):
    console.print(
        Panel(
            res.summary,
            title="Here's what I think of after going through your code:"
        )
    )
    console.print("\n🐛 Bugs")
    for bug in res.bugs:
        console.print(f" • {bug}")

    console.print("\n🛠 Maintainability")
    for item in res.maintainability:
        console.print(f" • {item}")

    console.print("\n⚡ Performance")
    for item in res.performance:
        console.print(f" • {item}")

    console.print("\n💡 Suggestions")
    for item in res.suggestions:
        console.print(f" • {item}")