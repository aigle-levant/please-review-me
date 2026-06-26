# import
# from cli import print_res
# from review import review

# a = review()
# print_res(a)
from cli.userinput import read_input
from models.validate import read_code
from agent.prompt import agent_prompt
from agent.agent import agent_response
from cli.interface import interface
from github.wrapper import fetch_open_prs
from github.parse import choose_pr
from github.changed import fetch_changed_file
from config import console

def main():
    try:
        while True:
            person = input("Enter the github id: ")
            if (len(person.strip())==0):
                console.print("[red]Please enter again[/red]")
                continue
            repo = input("Enter the repository name: ")
            if (len(repo.strip())==0):
                console.print("[red]Please enter again[/red]")
                continue
        repo_name = f"{person}/{repo}"
            pr = choose_pr(fetch_open_prs(repo_name))
            console.print("[cyan]Choose your fighter:[/cyan]")
            d = {
                1: "Intern",
                2: "Senior dev",
                3: "Parent",
                4: "Cybersecurity",
                5: "Systems engineer"
            }
            for i in len(d):
                print(f"{i} - {d.get(i)}")
            

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()