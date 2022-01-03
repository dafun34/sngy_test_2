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

# class OccupationMutation(graphene.Mutation):
#     class Arguments:
#         name = graphene.String(required=True),
#         company_name=graphene.String(required=True)
#         position_name=graphene.String(required=True)
#         hire_date=graphene.Date(required=True)
#         fire_date=graphene.Date()
#         salary=graphene.Int(required=True),
#         fraction=graphene.Int(required=True)
#         base=graphene.Int(required=True)
#         advance=graphene.Int(required=True)
#         by_hours=graphene.Boolean(required=True)
#         id = graphene.ID()
#     occupation = graphene.Field(OccupationType)
#
#     @classmethod
#     def mutate(cls, root, info, name, company_name, position_name,
#                hire_date, fire_date, salary, fraction, base, advance, by_hours,
#                id):
#         occupation = Occupation.objects.get(pk=id)
#         occupation.name = name
#         occupation.company_name = company_name
#         occupation.position_name = position_name
#         occupation.hire_date = hire_date
#         occupation.fire_date = fire_date
#         occupation.salary = salary
#         occupation.fraction = fraction
#         occupation.base = base
#         occupation.advance = advance
#         occupation.by_hours = by_hours
#         occupation.save()
#         return OccupationMutation(occupation=occupation)
#
# class Mutation(graphene.ObjectType):
#     updateOccupation = OccupationMutation.Field()

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
    removeOccupation = graphene.Field(graphene.String, obj_id=graphene.ID())

    def resolve_addOccupation(root, info, **kwargs):
        occupation, created = Occupation.objects.get_or_create(**kwargs)
        return occupation

    def resolve_removeOccupation(root, info, obj_id):
        try:
            Occupation.objects.get(id=obj_id).delete()
        except Occupation.DoesNotExist:
            return f'Объекта с ID:{obj_id} не существует'
        return f'Объект с ID:{obj_id} успешно удален'

schema = graphene.Schema(query=Query, mutation=Mutation)