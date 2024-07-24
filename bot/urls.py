from django.urls import path
from rest_framework import routers

from bot.views import ProjectView, SubProjectView, DisciplineView, ManpowerView, DemandView, DemandDetailView, \
    CertificationView, CertificationDetailView, UserView, LoginView, LogoutView

router = routers.SimpleRouter()
router.register('user', UserView, basename='user')
router.register('project', ProjectView, basename='project')
router.register('sub_project', SubProjectView, basename='sub_project')
router.register('discipline', DisciplineView, basename='discipline')
router.register('manpower', ManpowerView, basename='manpower')
router.register('demand', DemandView, basename='demand')
router.register('demand_detail', DemandDetailView, basename='demand_detail')
router.register('certification', CertificationView, basename='certification')
router.register('certification_detail', CertificationDetailView, basename='certification_detail')

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]
