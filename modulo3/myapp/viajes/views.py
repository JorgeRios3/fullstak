from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from . import models
from .forms import NameForm
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.shortcuts import redirect


from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import permission_required, login_required

from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt







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
    #[vals] = models.Pago.objects.all().select_related('viaje')
    #print(vals.viaje.descripcion)
    #return HttpResponse("pagina principal")
    if request.user.is_authenticated:
        return render(request, "viajes/index.html")
    return redirect('/login')

#@login_required
@login_required(login_url='/login')
@permission_required(['viajes.view_viaje'])
def bio(request, nombre="jorge"):
    #usuarios = []
    #for x in session.execute("select id as id, nombre as nombre, edad as edad, apellido_paterno as ap from personas"):
        #usuarios.append(dict(id = x.id, nombre=x.nombre, edad=x.edad, apaterno=x.ap))
    #print(request)
    if request.user.is_authenticated:
        #template = loader.get_template('viajes/index.html')
        #return HttpResponse(template.render({'nombre':nombre, 'apellido':'rios', 'usuarios':usuarios}, request))
        return HttpResponse("estas en ruta viaje/....")
    else:
        return HttpResponse("no estas logeado")

def forma_viaje(request, id=0):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            nombre = request.POST.get("nombre")
            #nombre = request.POST.get("apellido_paterno"))
            #p1 = Persona(nombre="jor")
            #p1.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/crear/')
    else:
        is_superuser = request.user.is_superuser
        form = NameForm()
        if is_superuser == False:
            form.base_fields['nombre'].disabled = True
        return render(request, 'persona.html', {'form': form})


class PersonaLista(ListView):
    model = models.Persona


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_django(request, user)
            usuarios = []
            template = loader.get_template('viajes/index.html')
            return HttpResponse(template.render({'nombre':'jorge', 'apellido':'rios', 'usuarios':usuarios}, request))
        else:
            return render(request, 'viajes/login.html', {})
    else:
        return render(request, 'viajes/login.html', {})


def logout(request):
    try:
        logout_django(request)
        return HttpResponseRedirect('/')
    except:
        return HttpResponse("error en logout")


#@method_decorator(login_required, name='dispatch')
#@method_decorator(permission_required("viajes.view_viaje"), name="dispatch")
#@method_decorator(permission_required('is_staff'), name="dispatch")
@method_decorator(csrf_exempt, name='dispatch')
class Vista(View):
    def get(self, request):
        print("por el get")
        is_superuser = request.user.is_superuser
        form = NameForm()
        if is_superuser == False:
            form.base_fields['nombre'].disabled = True
        return render(request, 'persona.html', {'form': form})

    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            nombre = request.POST.get("nombre")
            #nombre = request.POST.get("apellido_paterno"))
            #p1 = Persona(nombre="jor")
            #p1.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/crear/')

    def put(self, request):
        print("entro al put")
        return HttpResponse("regreso metodo put")
    
    def delete(self, request):
        print("entro en metodo delete")
        return HttpResponse("regreso metodo delete")

