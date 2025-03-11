STR = input()
bomb = input()
output = []

for c in STR:
    output.append(c)
    if ''.join(output[-len(bomb):]) == bomb:
        del output[-len(bomb):]

print(''.join(output))