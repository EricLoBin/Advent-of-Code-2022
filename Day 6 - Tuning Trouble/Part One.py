from inputs.input import get_input

inp = get_input(6).read()

for i in range(3, len(inp)):
    if len(set(inp[i-3:i+1])) == 4:
        print(i+1)
        break
