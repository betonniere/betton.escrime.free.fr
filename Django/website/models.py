from django.urls import reverse
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# ------------------------------------------------------------
class Article(models.Model):
    title    = models.CharField(max_length=50)
    vignette = models.CharField(max_length=50, default='')
    position = models.IntegerField(default=99)
    content  = RichTextField(default='')
    ref      = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        abstract = True

    # ----
    def get_vignette(self):
        vignettes = Vignette.objects.all()
        for vignette in vignettes:
            if self.vignette == vignette.name:
                return vignette.content
        return ''

    # ----
    def get_locale(self):
        return 'fr'

    # ----
    def get_slug(self):
        return slugify(self.title)

    # ----
    def get_absolute_url(self):
        return reverse('n_page', args=[self.get_locale(),  self.get_slug()])

    # ----
    def __unicode__(self):
        return self.title


# ------------------------------------------------------------
class ArticleEN(Article):
    def get_locale(self):
        return 'en'


class ArticleFR(Article):
    def get_locale(self):
        return 'fr'


class ArticleES(Article):
    def get_locale(self):
        return 'es'


class ArticleCA(Article):
    def get_locale(self):
        return 'ca'


class ArticleVA(Article):
    def get_locale(self):
        return 'va'


# ------------------------------------------------------------
class Vignette(models.Model):
    name    = models.CharField(max_length=50)
    content = RichTextField(default='')

    # ----
    def __unicode__(self):
        return self.name
