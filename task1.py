from re import findall
                       
text = input()
print(len(findall(r"""=-\\""", text)))
