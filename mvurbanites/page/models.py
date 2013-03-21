from django.db import models
from django.template.defaultfilters import slugify


class Page(models.Model):
    slug = models.SlugField(blank=True, editable=False)
    title = models.CharField(max_length=255)
    template = models.ForeignKey('Template')
    parent = models.ForeignKey('self', blank=True, null=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Page, self).save(*args, **kwargs)

class Template(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
