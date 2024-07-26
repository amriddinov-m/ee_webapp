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


class QualificationTracking(models.Model):
    CHOICES = [
        ('status1', 'Status 1'),
        ('status2', 'Status 2'),
    ]

    test_date = models.DateTimeField()
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE)
    position = models.ForeignKey('Manpower', on_delete=models.CASCADE)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    passport_number = models.CharField(max_length=255)
    passport_expire = models.DateField()
    info_status = models.CharField(max_length=255, choices=CHOICES)
    test_city = models.CharField(max_length=255)
    residence_state = models.CharField(max_length=255)
    uniform_size = models.CharField(max_length=255)
    shoes_size = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    ref_number = models.CharField(max_length=255)
    agency = models.CharField(max_length=255)
    qualified_1 = models.CharField(max_length=255)
    qualified_2 = models.CharField(max_length=255)
    language_hindi = models.CharField(max_length=255)
    language_english = models.CharField(max_length=255)
    medical_status = models.CharField(max_length=255)
    demand = models.ForeignKey('Demand', on_delete=models.CASCADE)
    demand_detail = models.ForeignKey('DemandDetail', on_delete=models.CASCADE)
    issue_date = models.DateTimeField()
    submission_date = models.DateTimeField()
    telex_number = models.CharField(max_length=255)
    visa_number = models.CharField(max_length=255)
    visa_date = models.DateTimeField()
    mobilization_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255)
    creator = models.ForeignKey('user.User', on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
