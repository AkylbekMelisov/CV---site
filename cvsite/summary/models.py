from django.db import models


class Resume(models.Model):
    photo = models.ImageField(blank=True, null=True, default='photo.jpg')
    full_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=40)
    github_account = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Experience(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    resume = models.ForeignKey(Resume, models.CASCADE, related_name='experiences')


class Education(models.Model):
    type_of_school = (
        ('kindergarten', 'kindergarten'),
        ('secondary_school', 'secondary_school'),
        ('university', 'university')
    )
    type_of_edu = (
        ('bachelor', 'bachelor'),
        ('master', 'master'),
        ('graduate_sertificate', 'graduate_sertificate')
    )
    type_of_univer = (
        ('offline', 'offline'),
        ('online', 'online')
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    type_of_school = models.CharField(choices=type_of_school, max_length=50, default='university')
    type_of_edu = models.CharField(choices=type_of_edu, max_length=50, default='bachelor')
    type_of_univer = models.CharField(choices=type_of_univer, max_length=50, default='online')
    name_of_school = models.CharField(max_length=50)
    faculty = models.CharField(max_length=50)
    spec = models.CharField(max_length=50)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')


class Skill(models.Model):
    name = models.CharField(max_length=50)
    star = models.PositiveIntegerField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')


class Language(models.Model):
    levels = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    )
    name = models.CharField(max_length=50)
    level = models.CharField(choices=levels, max_length=50, default='A1')
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='languages')
