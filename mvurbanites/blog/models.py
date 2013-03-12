from django.db import models
from django.template.defaultfilters import slugify

class Blog(models.Model):
    slug = models.SlugField(blank=True, editable=False)
    title = models.CharField(max_length=255)
    post = models.TextField()

    class Meta():
        get_latest_by = 'id'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Blog, self).save(*args, **kwargs)

