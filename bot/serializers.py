from rest_framework import serializers

from bot.models import Project, SubProject, Discipline, Manpower, Demand, DemandDetail, Certification, \
    CertificationDetail, QualificationTracking
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'phone_number', 'status']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class SubProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProject
        fields = '__all__'


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = '__all__'


class ManpowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manpower
        fields = '__all__'


class DemandSerializer(serializers.ModelSerializer):
    project_name = serializers.SerializerMethodField()
    sub_project_name = serializers.SerializerMethodField()
    creator_phone_number = serializers.SerializerMethodField()
    creator_name = serializers.SerializerMethodField()

    # Поля для записи
    # project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), write_only=True)
    # sub_project = serializers.PrimaryKeyRelatedField(queryset=SubProject.objects.all(), write_only=True)
    # creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    def get_project_name(self, obj):
        try:
            return obj.project.name
        except Exception as err:
            return None

    def get_sub_project_name(self, obj):
        try:
            return obj.sub_project.name
        except Exception as err:
            return None

    def get_creator_phone_number(self, obj):
        return obj.creator.phone_number

    def get_creator_name(self, obj):
        return obj.creator.get_full_name()

    class Meta:
        model = Demand
        fields = '__all__'
        read_only_fields = ('project_name', 'sub_project_name', 'creator_phone_number')


class DemandDetailSerializer(serializers.ModelSerializer):
    discipline_name = serializers.SerializerMethodField()
    manpower_name = serializers.SerializerMethodField()
    creator_phone_number = serializers.SerializerMethodField()

    # Поля для записи
    discipline = serializers.PrimaryKeyRelatedField(queryset=Discipline.objects.all(), write_only=True)
    manpower = serializers.PrimaryKeyRelatedField(queryset=Manpower.objects.all(), write_only=True)
    creator = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)

    def get_discipline_name(self, obj):
        try:
            return obj.discipline.name
        except Exception as err:
            return None

    def get_manpower_name(self, obj):
        try:
            return obj.manpower.name
        except Exception as err:
            return None

    def get_creator_phone_number(self, obj):
        return obj.creator.phone_number

    class Meta:
        model = DemandDetail
        fields = '__all__'


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'


class QualificationTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualificationTracking
        fields = '__all__'


class CertificationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationDetail
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)
