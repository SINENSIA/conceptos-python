import copy

empleados = [
    ["Pedro", ["Python", "SQL"]],
    ["Manolo", ["Java", "C++", "JavaScript"]],
    ["Alejandro", ["HTML", "CSS", "JavaScript"]]
]

empleados_shallow = empleados.copy()
# añado test a Pêdro
empleados_shallow[0][1].append('Testing')

empleados_deep = copy.deepcopy(empleados)

# en la lista original añado bash
empleados[0][1].append("Bash")
# aañdo Java en la ultima lista
empleados_deep[-1][-1].append('Java')
empleados_deep.append(["Juan",["Node.js", "redis"]])
# Quita a poder de deep
empleados_deep.remove(empleados_deep[0])

print("----- empleados original ------")
print(empleados)
print()
print("------empleados shallow--------")
print(empleados_shallow)
print()
print("------empleados deep--------")
print(empleados_deep)











