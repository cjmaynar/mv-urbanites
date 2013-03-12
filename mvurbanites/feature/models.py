from django.db import models

from django.template.defaultfilters import slugify

'''There's two differnt types of things that can be featured, a Member or
a Restraunt. In either case they have an Interview attached to them'''

class Feature(models.Model):
    slug = models.SlugField(blank=True, editable=False)
    name = models.CharField(max_length=255)
    about = models.TextField()
    interview = models.ManyToManyField('Interview')

    member = models.OneToOneField('Member', null=True, blank=True)
    business = models.OneToOneField('Business', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Feature, self).save(*args, **kwargs)

class Member(models.Model):
    SEXES = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEXES)

class Business(models.Model):
    owner = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    cusine = models.ForeignKey('Cusine')

    def __unicode__(self):
        return self.owner

class Cusine(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Interview(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __unicode__(self):
        return self.question
