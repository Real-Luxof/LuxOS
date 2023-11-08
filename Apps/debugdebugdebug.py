foo = ["foo","foo","bar"]
for i in foo:
    print(i)
    del foo[foo.index(i)]
print(foo)