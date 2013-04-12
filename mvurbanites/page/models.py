from glob import glob
from os.path import basename, splitext

from django.db import models
from django.template.defaultfilters import slugify

from settings import SITE_ROOT

class PageManager(models.Manager):
    def published(self):
        return self.get_query_set().filter(published=True)

class Page(models.Model):
    TEMPLATES = [(basename(t), basename(splitext(t)[0]).replace("_", " ").title()) for t in glob(SITE_ROOT + '/page/templates/page/*.html')]

    slug = models.SlugField(blank=True, editable=False)
    title = models.CharField(max_length=255)
    template = models.CharField(max_length=75, choices=TEMPLATES, default='basic.html', help_text="The template to be used to render this page. When unsure, leave as Basic")
    parent = models.ForeignKey('self', related_name="children", blank=True, null=True)
    in_navigation = models.BooleanField(default=False, help_text="Show this page in the navigation?")
    published = models.BooleanField(default=False)

    objects = PageManager()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Page, self).save(*args, **kwargs)


class Component(models.Model):
    class Meta:
        ordering = ['order']

    POSITIONS = (
        ('center', "Center"),
        ('left', "Left"),
        ('right', "Right"),
    )

    order = models.PositiveIntegerField(blank=True)
    page = models.ForeignKey('Page')
    text = models.TextField()
    image = models.ImageField(upload_to="component")
    link = models.CharField(max_length=255)
    alternate_text = models.CharField(max_length=255)
    side = models.CharField(max_length=50, choices=POSITIONS)
    span = models.SmallIntegerField(choices=[(s, s) for s in range(1, 8)], default=5)

    def __unicode__(self):
        if self.id:
            if self.text != "":
                return "Text Component"
            else:
                return "Image: %s" % (basename(self.image.path))

        return "Component %d" % (self.order)

    def save(self, *args, **kwargs):
        if not self.order:
            self.order = self.page.component_set.count() + 1

        super(Component, self).save(*args, **kwargs)
