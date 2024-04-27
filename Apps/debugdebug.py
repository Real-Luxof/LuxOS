def scale_2dlist(data, extendby):
    result = []
    for row in data:
        for _ in range(extendby):
            new_row = [item for item in row for _ in range(extendby)]  # Duplicate each item in the row
            result.append(new_row)  # Duplicate each row
            # weird method of adding new lists cuz python stores it weird if i don't do this
    return result

# Test the function with your data
data = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

new = transform_list(data, 3)
new[5][5] = 100
for i in new: print(i)
