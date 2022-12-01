import os
import requests

def get_input(day):
    if (not os.path.isfile("./cookie.txt")):
        open("cookie.txt", "x").write(input("What is your cookie? "))

    if (os.path.isfile(f"./inputs/{day}.txt")):
        return open(f"inputs/{day}.txt", "r")
    else:
        cookies = {'session': f"{open('cookie.txt', 'r').read()}"}
        url = f"https://adventofcode.com/2021/day/{day}/input"
        data = requests.post(url, cookies=cookies)

        file = open(f"inputs/{day}.txt", "x")
        file.write(str(data.content)[2:-3].replace("\\n", "\n"))

        return get_input(day)
