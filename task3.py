xmldoc = open("input.xml", 'r')
contentsxml = xmldoc.read().replace("<", ">").split(">")
pathval = []
isname = False
path = []
for i in contentsxml:
    if i.isspace() or i == "":
        isname = True
    elif i[0] == '/':
        path.pop()
    elif isname:
        path.append(i)
        isname = False
    else:
        pathval.append([list(path), i])
jsondict = {}
for i in range(len(pathval)):
    dictpath = ""
    for j in range(len(pathval[i][0])):
        dictpath = dictpath + f"""["{pathval[i][0][j]}"]"""
        exec(f"keyasgn = True if pathval[i][0][j] in jsondict else False")
        if keyasgn and j == len(pathval[i][0]) - 1:
            exec(f"jsondict{dictpath} += [pathval[i][1]]  if isinstance(jsondict{dictpath}, list) else [jsondict{dictpath}]")
        elif j == len(pathval[i][0]) - 1:
            exec(f"jsondict{dictpath} = pathval[i][1]")
        elif not keyasgn and j < len(pathval[i][0]) - 1:
            exec(f"jsondict{dictpath} = {{}}")

jsonoutputfile = open("output.json", 'w')
jsonoutputfile.write(str(jsondict).replace("'", '"'))
jsonoutputfile.close()
xmldoc.close()
print(str(jsondict))
