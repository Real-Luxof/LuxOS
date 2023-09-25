import api
foo = api.block("foo")
bar = api.block("bar",True)
fub = api.player("fub")
display = [
    [foo, foo, foo, foo, foo],
    [bar, bar, bar, bar, bar],
    [bar, bar, fub, bar, bar],
    [bar, bar, bar, bar, bar],
    [foo, foo, foo, foo, foo]
]
def finadisplay(display):
    for i in display:
        for j in i:
            print(j, end="")
        print()
finadisplay(display)
newdata = fub.move("a",display,bar)
display = newdata[0]
print("Now for moving")
finadisplay(display)