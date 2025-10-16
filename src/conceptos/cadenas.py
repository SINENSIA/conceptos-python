print("Hola mundo")

print("""Este texto
se representará 
en varias líneas
todo el texto que escriba
""")
# 
num_lineas = 3

print(f"""Este texto
se representará 
en {num_lineas} líneas
""")


def print_multilinea(texto, num_lineas):
    if(True):
        test = 7
    else:
        test = 8
        
    print(f"""{texto}
    se representará 
    en {num_lineas} líneas
    """)
    print(test)
    
print_multilinea("Este texto", 4)


str = "lorem ipsum doror sit amen"

print(str.capitalize())
print(str.upper())
print(str.casefold())

