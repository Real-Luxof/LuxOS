import api
block = api.block()
block2 = api.block()
list = [block, block2, block, block2]
print(list[1] == block2)