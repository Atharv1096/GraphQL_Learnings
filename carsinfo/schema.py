# cookbook/schema.py
import graphene
from graphene_django import DjangoObjectType

from mycars.models import Car, Build, Company


class CarType(DjangoObjectType):
    class Meta:
        model = Car
        fields = ("id", "name", "colour", "country_of_origin", "mileage", "description", "build", "company")


class BuildType(DjangoObjectType):
    class Meta:
        model = Build
        fields = ("id", "name", "differentiating_factor")


class CompanyType(DjangoObjectType):
    class Meta:
        model = Company
        fields = ("id", "name", "country_name", "speciality")

class Query(graphene.ObjectType):
    all_cars = graphene.List(CarType)
    all_companies = graphene.List(CompanyType)
    all_builds = graphene.List(BuildType)

    build_by_name = graphene.Field(
        BuildType, name=graphene.String(required=True))

    company_by_name = graphene.Field(
        CompanyType, name=graphene.String(required=True))
    
    car_by_country_name = graphene.List(CarType, country_name=graphene.String())

    def resolve_all_cars(root, info):
        # We can easily optimize query count in the resolve method
        return Car.objects.select_related("company").all()
    
    def resolve_all_builds(root, info):
        # We can easily optimize query count in the resolve method
        return Build.objects.all()
    
    def resolve_all_companies(root, info):
        # We can easily optimize query count in the resolve method
        return Company.objects.all()
    
    def resolve_build_by_name(root, info, name):
        try:
            return Build.objects.get(name=name)
        except Build.DoesNotExist:
            return None
        
    def resolve_company_by_name(root, info, name):
        try:
            return Company.objects.get(name=name)
        except Company.DoesNotExist:
            return None
        
    def resolve_car_by_country_name(root, info, country_name):
        try:
            return Car.objects.filter(country_of_origin=country_name)
        except Car.DoesNotExist:
            return None

    


schema = graphene.Schema(query=Query)
