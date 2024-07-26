from django.contrib.auth import authenticate
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from bot.models import Project, SubProject, Discipline, Manpower, Demand, DemandDetail, Certification, \
    CertificationDetail, QualificationTracking
from bot.serializers import ProjectSerializer, SubProjectSerializer, DisciplineSerializer, ManpowerSerializer, \
    DemandSerializer, DemandDetailSerializer, CertificationSerializer, CertificationDetailSerializer, UserSerializer, \
    LoginSerializer, QualificationTrackingSerializer
from user.models import User


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class SubProjectView(viewsets.ModelViewSet):
    queryset = SubProject.objects.all()
    serializer_class = SubProjectSerializer
    permission_classes = [AllowAny]


class DisciplineView(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [AllowAny]


class ManpowerView(viewsets.ModelViewSet):
    queryset = Manpower.objects.all()
    serializer_class = ManpowerSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = self.queryset
        discipline_id = self.request.query_params.get('discipline_id', None)
        filters = Q()
        if discipline_id:
            filters &= Q(discipline_id=discipline_id)

        return queryset.filter(filters)


class DemandView(viewsets.ModelViewSet):
    queryset = Demand.objects.all()
    serializer_class = DemandSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(creator_id=1)

    def get_queryset(self):
        queryset = self.queryset
        pk = self.request.query_params.get('id', None)
        filters = Q()
        if pk:
            filters &= Q(id__icontains=pk)

        return queryset.filter(filters)


class DemandDetailView(viewsets.ModelViewSet):
    queryset = DemandDetail.objects.all()
    serializer_class = DemandDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = self.queryset
        demand_id = self.request.query_params.get('demand_id', None)

        filters = Q()
        if demand_id:
            filters &= Q(demand_id=demand_id)

        return queryset.filter(filters)

    @action(detail=False, methods=['post'])
    def create_or_update(self, request, *args, **kwargs):
        print(request.data)
        demand_id = request.data.get('demand')
        discipline_id = request.data.get('discipline')
        manpower_id = request.data.get('manpower')
        count = request.data.get('count')
        creator_id = request.data.get('creator')

        instance = DemandDetail.objects.filter(demand_id=demand_id, discipline_id=discipline_id,
                                               manpower_id=manpower_id).first()
        if instance:
            instance.count += int(count)
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

        data = {
            'demand': demand_id,
            'discipline': discipline_id,
            'manpower': manpower_id,
            'count': count,
            'creator': creator_id,
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CertificationView(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [AllowAny]


class CertificationDetailView(viewsets.ModelViewSet):
    queryset = CertificationDetail.objects.all()
    serializer_class = CertificationDetailSerializer
    permission_classes = [AllowAny]


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.status != 'active':
                    return Response({'error': 'Awaiting confirmation'}, status=status.HTTP_403_FORBIDDEN)
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'is_admin': user.is_superuser
                })
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class QualificationTrackingView(viewsets.ModelViewSet):
    queryset = QualificationTracking.objects.all()
    serializer_class = QualificationTrackingSerializer
    permission_classes = [AllowAny]
