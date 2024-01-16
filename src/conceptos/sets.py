zoo = { 'mono', 'águila', 'tigre', 'elefante', 'serpiente' }
print('mono' in zoo) 
zoo.add("rinoceronte")
print(zoo) 

zoo.update(["cebra", "cocodrilo"])
print(zoo)# 'cocodrilo', 'cebra', 'serpiente', 'rinoceronte', 'elefante', 'águila', 'tigre', 'mono'}

zoo.discard("rinoceronte")
print('------')
print(zoo) #  { 'cocodrilo', 'cebra', 'serpiente', 'elefante', 'águila', 'tigre', 'mono'}
zoo2 = zoo.copy()
print(zoo2)
for _ in range(len(zoo)):
    animal = zoo.pop()
    print(animal) # 'cebra' # …o cualquier otro. Cada vez que ejecutamos, un animal azar.

print(id(zoo))
print(id(zoo2))

zoo1 = { 'mono', 'tigre', 'panda', 'elefante', 'loro' }
zoo2 = { 'loro', 'lince', 'pitón', 'emú'}

zoo3 = zoo1 | zoo2
print("|" + str(zoo3))
zoo3 = zoo1 & zoo2
print("&" + str(zoo3))
zoo3 = zoo1 - zoo2
print("-" + str(zoo3))
zoo3 = zoo1 ^ zoo2
print("^" + str(zoo3))

print(zoo3)