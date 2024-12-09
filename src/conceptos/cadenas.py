print("""Este texto
se representará 
en varias líneas
""")

num_lineas = 3

print(f"""Este texto
se representará 
en {num_lineas} líneas
""")


def print_multilinea(texto, num_lineas):
    print(f"""{texto}
    se representará 
    en {num_lineas} líneas
    """)


print_multilinea("Este texto", 4)


str = "lorem ipsum doror sit amen"

print(str.capitalize())
