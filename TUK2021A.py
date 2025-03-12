#======================================================
# STR = input()
# bomb = input()
# output = []
#
# for c in STR:
#     output.append(c)
#     if ''.join(output[-len(bomb):]) == bomb:
#         del output[-len(bomb):]
#
# print(''.join(output))
#======================================================
STR = input()
bomb = input()

while bomb in STR:
    STR = STR.replace(bomb,'')

print(''.join(STR))

#=============교수님 코드================
#s = input()
#e = input()
#while e in s:
#   s = s.replace(e,'')
#print(s)