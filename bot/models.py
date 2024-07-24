from django.db import models


# class User(models.Model):
#     tg_id = models.BigIntegerField(default=0)
#     phone_number = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.phone_number


class Project(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class SubProject(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    creator = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Manpower(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    creator = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Demand(models.Model):
    class Status(models.TextChoices):
        new = 'new', 'new',
        ready = 'ready', 'ready'
    creator = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sub_project = models.ForeignKey(SubProject, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.new)
    comment = models.TextField(null=True)

    def __str__(self):
        return f'{self.id}'


class DemandDetail(models.Model):
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE)
    creator = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    manpower = models.ForeignKey(Manpower, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'


class Certification(models.Model):
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE)
    creator = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255)
    comment = models.TextField(null=True)

    def __str__(self):
        return f'{self.id}'


class CertificationDetail(models.Model):
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    demand = models.ForeignKey(Demand, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    creator = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True)
    manpower = models.ForeignKey(Manpower, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'
