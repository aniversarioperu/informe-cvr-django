import markdown
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse

from django.db import models


class Entry(models.Model):
    title = models.TextField()
    body = MarkdownField()
    body_html = models.TextField()
    slug = models.SlugField(max_length=125, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    def save(self):
        self.body_html = markdown.markdown(self.body, ['codehilite'])
        super(Entry, self).save()

    class Meta:
        verbose_name = "Sección del Informe CVR"
        verbose_name_plural = "Secciones del Informe CVR"
        ordering = ['-created']
