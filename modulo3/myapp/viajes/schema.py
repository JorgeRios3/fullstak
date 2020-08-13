import graphene
from .models import Persona, Pago
from graphene_django import DjangoObjectType
from graphene import relay, Schema
from graphene_django.filter import DjangoFilterConnectionField


class PersonaType(DjangoObjectType):
    class Meta:
        model = Persona
        fields = ("id", "nombre", "edad")

class PagoType(DjangoObjectType):
    class Meta:
        model = Pago
        fields = ("id", "total", "persona")

class Query(graphene.ObjectType):
    all_personas = graphene.List(PersonaType)
    todos_pagos = graphene.List(PagoType)
    persona_by_nombre = graphene.Field(PersonaType, nombre=graphene.String(required=True))

    def resolve_all_personas(root, info):
        return Persona.objects.all()
    
    def resolve_todos_pagos(root, info):
        return Pago.objects.select_related("persona").all()

    def resolve_persona_by_nombre(root, info, nombre):
        try:
            return Persona.objects.get(nombre=nombre)
        except Persona.DoesNotExist:
            return None

class PersonaNode(DjangoObjectType):
    class Meta:
        model = Persona
        #exclude_fields = ('apellido_paterno', )
        filter_fields = ['nombre', 'edad']
        interfaces = (relay.Node, )


class PagoNode(DjangoObjectType):
    class Meta:
        model = Pago
        filter_fields = {
            'total': ['exact', 'icontains', 'istartswith'],
            'fecha': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )


class Query2(graphene.ObjectType):
    persona = relay.Node.Field(PersonaNode)
    all_personas = DjangoFilterConnectionField(PersonaNode)

    all_pagos = DjangoFilterConnectionField(PagoNode)
    pago = relay.Node.Field(PagoNode)


from graphene_django.types import ObjectType
from graphene import relay, Schema
from graphene_django.rest_framework.mutation import SerializerMutation
from .serializers import PersonaSerializer
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


class PersonaType(SerializerMutation):
    class Meta:
        serializer_class = PersonaSerializer

class PersonaConnection(relay.Connection):
    class Meta:
        node = PersonaType



class Query3(graphene.ObjectType):
    all_personas = relay.ConnectionField(PersonaConnection)
    all_personas_sql = relay.ConnectionField(PersonaConnection)

    persona = graphene.Field(PersonaType,
                                id=graphene.Int(),
                                nombre=graphene.String(),
                                apellido_paterno=graphene.String(),
                                )
    
    def resolve_all_personas(self, info):
        return Persona.objects.all()

    def resolve_all_personas_sql(self, info, **kwargs):
        uri = 'mysql+mysqldb://jorge.rios:Macros3@localhost:3306/proyectox'
        engine = create_engine(uri)
        conn = engine.connect().connection
        session = sessionmaker(bind=engine)()
        query = "select * from personas"
        my_vals = []
        for x in session.execute(query):

            my_vals.append(dict(id=x.id, nombre=x.nombre, apellido_paterno=x.apellido_paterno))
            
        #return Client.objects.all()
        return my_vals

    
    def resolve_persona(self, info, **kwargs):
        id = kwargs.get('id')
        nombre = kwargs.get('nombre')
        apellidop = kwargs.get('apellido_paterno')
        if id is not None:
            return Persona.objects.get(pk=id)
        if nombre is not None:
            return Persona.objects.get(nombre=nombre)
        if apellidop is not None:
            return Persona.objects.get(apellido_paterno=apellidop)
        
        return None

class UpdatePersona(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        #si queremos mas campos a actualizar agregarlos
        id = graphene.ID()

    persona = graphene.Field(PersonaType)

    def mutate(self, info, nombre, id):
        persona = Persona.objects.get(pk=id)
        persona.nombre = nombre
        persona.save()
        return UpdatePersona(persona=persona)

class CreatePersona(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        nombre = graphene.String()
        edad = graphene.Int()

    # The class attributes define the response of the mutation
    persona = graphene.Field(PersonaType)

    def mutate(self, info, nombre, edad):
        persona = Persona.objects.create(nombre=nombre, edad=edad)
        persona.save()
        # Notice we return an instance of this mutation
        return CreatePersona(persona=persona)


class DeletePersona(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        obj = Persona.objects.get(pk=kwargs["id"])
        obj.delete()
        return cls(ok=True)

class Mutations(graphene.ObjectType):
    update_persona = UpdatePersona.Field()
    create_persona = CreatePersona.Field()
    delete_persona = DeletePersona.Field()



#schema = graphene.Schema(query=Query3)
schema = graphene.Schema(query=Query3, mutation=Mutations)






