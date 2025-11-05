age = 6
tree = 2
trees = 2
while trees <= 100:
    age += 1
    tree += 2
    trees += tree
print(f"小明{age}岁时,累计种树{trees}棵")
