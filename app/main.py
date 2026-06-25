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
from config import li

def main():
    try:
        code = read_input()
        if code is None:
            return
        data = read_code(code)
        prompt = agent_prompt(data)
        print("Hmm, hmm...okay!")
        res = agent_response(prompt)
        print("Okay, I've gone through your file...")
        interface(res)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()