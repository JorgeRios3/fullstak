import mariadb


def busqueda(nombre="falso"):
    conn = mariadb.connect(user="jorge.rios", password="Macros3", host="localhost", port=3306, database="proyectox")
    cur = conn.cursor()
    #cur.execute("select * from personas")
    cur.execute("select * from personas where nombre='{}'".format(nombre))
    for x in cur:
        print(x)



def main():
    print("entro en busqueda como primer fucnion")
    nombre = input("escribe el valor")
    print("este es tu valor {}".format(nombre))
    busqueda(nombre)


if __name__ == "__main__":
    main()
