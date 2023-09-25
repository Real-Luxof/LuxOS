foo = [
    ["foo","foo","foo","foo","foo","foo","foo","foo","foo","foo",],
    ["foo","foo","foo","foo","foo","foo","foo","foo","foo","foo",],
    ["foo","foo","foo","foo","foo","foo","foo","foo","foo","foo",],
    ["foo","foo","foo","baa","foo","baa","foo","foo","foo","foo",],
    ["foo","foo","foo","foo","bar","foo","foo","foo","foo","foo",],
    ["foo","foo","foo","foo","foo","foo","foo","foo","foo","foo",],
    ["foo","foo","foo","foo","foo","foo","foo","foo","foo","foo",],
    ["foo","foo","foo","foo","foo","foo","foo","foo","foo","foo",],
    ["foo","foo","foo","foo","foo","foo","foo","foo","foo","foo",],
    ["foo","foo","foo","foo","foo","foo","foo","foo","foo","foo",]
]
foobar = [
    [[],[],[]],
    [[],[],[]],
    [[],[],[]]
]
bary = 4
barx = 4
ycoord = 3
xcoord = 3
for i in range(len(foobar)):
    for j in range(len(i)):
        if foo[i][j] == "bar":
            for n in (foo[i - 1], foo[i + 1])