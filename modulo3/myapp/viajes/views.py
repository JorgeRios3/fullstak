from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from . import models
from .forms import NameForm
from django.views.generic import ListView




# Test if it works
engine = sqlalchemy.create_engine('mysql+mysqldb://jorge.rios:Macros3@localhost:3306/proyectox')
conn = engine.connect().connection
session= sessionmaker(bind =engine)()


def index(request):
    #personas = models.Persona.objects.all()
    #for x in personas:
    #    print(x.nombre)
    #persona = models.Persona(nombre="jajaja", apellido_paterno="jaja", apellido_materno="beltran", edad=1)
    #persona.save()
    #[persona] = models.Persona.objects.filter(nombre='nuevo nombre')
    #meter la informacion el postgres
    #persona.nombre="nuevo nombre"
    #persona.save()
    #persona.delete()
    [vals] = models.Pago.objects.all().select_related('viaje')
    print(vals.viaje.descripcion)
    return HttpResponse("pagina principal")

def bio(request, nombre="jorge"):
    usuarios = []
    for x in session.execute("select id as id, nombre as nombre, edad as edad, apellido_paterno as ap from personas"):
        usuarios.append(dict(id = x.id, nombre=x.nombre, edad=x.edad, apaterno=x.ap))
    print(request)
    template = loader.get_template('viajes/index.html')
    return HttpResponse(template.render({'nombre':nombre, 'apellido':'rios', 'usuarios':usuarios}, request))

def forma_viaje(request, id=0):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            nombre = request.POST.get("nombre"))
            #nombre = request.POST.get("apellido_paterno"))
            #p1 = Persona(nombre="jor")
            #p1.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/crear/')
    else:
        print("aca")
        form = NameForm()

    return render(request, 'persona.html', {'form': form})


class PersonaLista(ListView):
    model = models.Persona
