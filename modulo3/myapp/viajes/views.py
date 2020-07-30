from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import sqlalchemy
from sqlalchemy.orm import sessionmaker


# Test if it works
engine = sqlalchemy.create_engine('mysql+mysqldb://jorge.rios:Macros3@localhost:3306/proyectox')
conn = engine.connect().connection
session= sessionmaker(bind =engine)()


def index(request):
    return HttpResponse("pagina principal")

def bio(request, nombre="jorge"):
    usuarios = []
    for x in session.execute("select id as id, nombre as nombre, edad as edad, apellido_paterno as ap from personas"):
        usuarios.append(dict(id = x.id, nombre=x.nombre, edad=x.edad, apaterno=x.ap))
    print(request)
    template = loader.get_template('viajes/index.html')
    return HttpResponse(template.render({'nombre':nombre, 'apellido':'rios', 'usuarios':usuarios}, request))
