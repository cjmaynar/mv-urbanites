from django.db import models
'''There's two differnt types of things that can be featured, a Member or
a Restraunt. In either case they have an Interview attached to them'''

class Member(models.Model):
    SEXES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEXES)
    bio = models.TextField()
    interview = models.ManyToManyField('Interview')

    def __unicode__(self):
        return self.name

class Restraunt(models.Model):
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    cusine = models.ForeignKey('Cusine')
    about = models.TextField()
    interview = models.ManyToManyField('Interview')

    def __unicode__(self):
        return self.name

class Cusine(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Interview(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __unicode__(self):
        return self.question
