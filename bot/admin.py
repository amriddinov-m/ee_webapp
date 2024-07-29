from django.contrib import admin

from bot.models import Project, SubProject, Discipline, Manpower, Demand, DemandDetail, Certification, \
    CertificationDetail, QualificationTracking


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(SubProject)
class SubProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    pass


@admin.register(Manpower)
class ManpowerAdmin(admin.ModelAdmin):
    pass


@admin.register(Demand)
class DemandAdmin(admin.ModelAdmin):
    pass


@admin.register(DemandDetail)
class DemandDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    pass


@admin.register(CertificationDetail)
class CertificationDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(QualificationTracking)
class QualificationTrackingAdmin(admin.ModelAdmin):
    pass
