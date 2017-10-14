def generateDataStructure(comp):
    original = comp
    ds = []
    while (True):
        obt = comp.find('[');
        if(obt == -1):
            break
        else:
            cbt = comp[obt:].find(']')
            if(cbt == -1):
                break
        times = ""
        i = 1
        while (True):
            if(i <= obt and (comp[obt-i] != "[" and comp[obt-i] != "]")):
                times = comp[obt-i] + times[0:]
                i += 1
            else:
                break
        string = comp[obt+1:cbt+1]
        ds.append([int(times),string])
        comp = comp[cbt+2:]
    return ds

def readDataStructure(ds):
    op = ""
    for i in ds:
        for j in range(0, i[0]):
            op += i[1]
    return op

print(readDataStructure(generateDataStructure("3[abc]2[ab]")))

