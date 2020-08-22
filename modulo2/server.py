from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import mariadb
conn = mariadb.connect(user="jorge.rios", password="Macros3", host="localhost", port=3306, database="proyectox")
cur = conn.cursor()

import sqlalchemy
from sqlalchemy.orm import sessionmaker

#class UsuarioMSQL(model):
#    id, nombre
#    pass

#class UsuarioPostgres(model):
#    id, nombre, fecha
#    pass


# Test if it works
engine = sqlalchemy.create_engine('mysql+mysqldb://jorge.rios:Macros3@localhost:3306/proyectox')
conn = engine.connect().connection
session= sessionmaker(bind =engine)()
#engine2 = sqlalchemy.create_engine('postgres+mysqldb://jorge.rios:Macros3@localhost:3306/proyectox')
#conn2 = engine.connect().connection
#session2= sessionmaker(bind =engine)()
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
#cors = CORS(app, resources={r"/auth": {"origins": "*"}})
#cors = CORS(app, resources={r"/*": {"origins": "*"}})
app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def main():
    with open("query.txt", "r") as f:
        [val] = f.readlines()
        for x in session.execute(val):
            print("viendo usuario ", x)
    #select * from usuarios(mysql)
    #for x in usuarios:
    #  postgres(insert into usuarios  x)
    # if el usuario es id >20
      #guardalo en postgres y agregale el campo nuevo que necesito
    # else
    # guardalo en la base de datos mysql tal cual
    #mariadbdriver
    #cur.execute("select nombre, edad from personas")
    #headers = cur.description
    #print("viendo headers ",headers[0][0], headers[1][0])
    #vals = cur.fetchall()
    #for x in vals:
    #    print(x.edad)

    #sqlalchemy
    print("sqlalchemy")
    usuarios = []
    valores = {}
    for x in session.execute("select id as id, nombre as nombre, edad as edad, apellido_paterno as ap from personas"):
        usuarios.append(dict(id = x.id, nombre=x.nombre, edad=x.edad, apaterno=x.ap))


    #return jsonify({"usuarios": usuarios}), 200
    valores["usuarios"]= usuarios
    valores["titulo"] = "todos los usuarios"
    return render_template('index.html', valores=valores)


@app.route('/usuario', methods=['GET', 'POST', 'PUT'])
def usuario():
    is_update = False
    val = request.query_string.decode('utf-8')
    if request.query_string:
        is_update = val[-1]
    if request.method == "POST":
        if is_update:
            ombre = request.form.get("nombre")
            edad = request.form.get("edad")
            #session.execute("update personas set nombre, edad) values ('{}', '{}')".format(nombre, edad))
            session.commit()
        else:
            print(request.form)
            nombre = request.form.get("nombre")
            edad = request.form.get("edad")
            session.execute("insert into personas (nombre, edad) values ('{}', '{}')".format(nombre, edad))
            session.commit()
    if request.method == "PUT":
        print("llego al put")

    return render_template('forma.html', valores=is_update)




if __name__ == '__main__':
    app.run()

