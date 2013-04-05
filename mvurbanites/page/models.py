from django.db import models
from django.template.defaultfilters import slugify

class Page(models.Model):
    slug = models.SlugField(blank=True, editable=False)
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', related_name="children", blank=True, null=True)
    in_navigation = models.BooleanField(default=False)

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
    '''
    image = models.ImageField(upload_to="component")
    link = models.CharField(max_length=255)
    alternate_text = models.CharField(max_length=255)
    side = models.CharField(max_length=50, choices=POSITIONS)
    '''

    def __unicode__(self):
        return "Component %d" % (self.order)

    def save(self, *args, **kwargs):
        if not self.order:
            self.order = self.page.component_set.count() + 1

        super(Component, self).save(*args, **kwargs)
