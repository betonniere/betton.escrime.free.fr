from django.contrib import admin
from .models import Vignette
from .models import ArticleEN
from .models import ArticleFR
from .models import ArticleES
from .models import ArticleCA
from .models import ArticleVA

admin.site.register(Vignette)

admin.site.register(ArticleEN)
admin.site.register(ArticleFR)
admin.site.register(ArticleES)
admin.site.register(ArticleCA)
admin.site.register(ArticleVA)
