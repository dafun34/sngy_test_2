import graphene
from django import forms
from graphene_django import DjangoObjectType, DjangoListField
from applicant.models import Occupation
from graphene_django.forms.mutation import DjangoModelFormMutation

class OccupationType(DjangoObjectType):
    class Meta:
        model = Occupation
        fields = ('__all__')

class Query(graphene.ObjectType):
    getOccupations = graphene.List(OccupationType)
    getOccupation = graphene.Field(OccupationType, id=graphene.Int())

    def resolve_getOccupations(root, info):
        return Occupation.objects.all()

    def resolve_getOccupation(root, info, id):
        return Occupation.objects.get(id=id)
# name: String!,
# companyName: String!,
# positionName: String!,
# hireDate: Date!,
# fireDate: Date,
# salary: Int!,
# fraction: Int!,
# base: Int!,
# advance: Int!,
# by_hours: Boolean!

class Mutation(graphene.ObjectType):
    addOccupation = graphene.Field(OccupationType,
                                   name=graphene.String(required=True),
                                   company_name=graphene.String(required=True),
                                   position_name=graphene.String(required=True),
                                   hire_date=graphene.Date(required=True),
                                   fire_date=graphene.Date(),
                                   salary=graphene.Int(required=True),
                                   fraction=graphene.Int(required=True),
                                   base=graphene.Int(required=True),
                                   advance=graphene.Int(required=True),
                                   by_hours=graphene.Boolean(required=True)
                                   )

    def resolve_addOccupation(root, info, **kwargs):
        occupation, created = Occupation.objects.get_or_create(**kwargs)
        return occupation

schema = graphene.Schema(query=Query, mutation=Mutation)