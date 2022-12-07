from inputs.input import get_input

inp = get_input(6).read()

for i in range(13, len(inp)):
    if len(set(inp[i-13:i+1])) == 14:
        print(i+1)
        break
