from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import mariadb
conn = mariadb.connect(user="jorge.rios", password="Macros3", host="localhost", port=3306, database="proyectox")
cur = conn.cursor()

import sqlalchemy
from sqlalchemy.orm import sessionmaker


# Test if it works
engine = sqlalchemy.create_engine('mysql+mysqldb://jorge.rios:Macros3@localhost:3306/proyectox')
conn = engine.connect().connection
session= sessionmaker(bind =engine)()
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
#cors = CORS(app, resources={r"/auth": {"origins": "*"}})
#cors = CORS(app, resources={r"/*": {"origins": "*"}})
app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def main():
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
    if request.method == "POST":
        #print("entro en metodo post")
        print(request.form)
        nombre = request.form.get("nombre")
        edad = request.form.get("edad")
        session.execute("insert into personas (nombre, edad) values ('{}', '{}')".format(nombre, edad))
        session.commit()
    if request.method == "PUT":
        pass

    return render_template('forma.html')




if __name__ == '__main__':
    app.run()

