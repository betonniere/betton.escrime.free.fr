from django.shortcuts import render
from django.urls import reverse
from .site_language import Language
from .models import ArticleEN
from .models import ArticleFR
from .models import ArticleES
from .models import ArticleCA
from .models import ArticleVA


# ------------------------------------------------------------
class Page:
    # --
    def __init__(self, locale, article):
        self.locale  = locale
        self.article = article

    # --
    def get_title(self):
        return self.article.title

    # --
    def get_vignette(self):
        return self.article.get_vignette()

    # --
    def get_content(self):
        return self.article.content

    # --
    def get_absolute_url(self):
        return reverse('n_page', args=[self.locale, self.article.get_slug()])


# ------------------------------------------------------------
class Book:
    # --
    def __init__(self, locale):
        self.locale = locale
        self.pages  = []

        if locale == 'en':
            objects = ArticleEN.objects.all()
        elif locale == 'fr':
            objects = ArticleFR.objects.all()
        elif locale == 'es':
            objects = ArticleES.objects.all()
        elif locale == 'ca':
            objects = ArticleCA.objects.all()
        elif locale == 'va':
            objects = ArticleVA.objects.all()

        objects = objects.order_by('position')

        for article in objects:
            page = Page(locale, article)
            if(page.article.ref != 'Download (V4)'):
                self.pages.append(page)

    # --
    def has_page(self, page):
        for p in self.pages:
            if p.article.ref == page.article.ref:
                return True

        return False

    # --
    def add_missing_pages_from(self, from_book):
        for page in from_book.pages:
            if self.has_page(page) is not True:
                page.locale = self.locale
                self.pages.append(page)


# ------------------------------------------------------------
def get_language(locale):
    for current_language in Language.pool:
        if current_language.code == locale:
            return current_language


# ------------------------------------------------------------
def display_page(request, locale='fr', pk=''):
    book         = Book(locale)
    default_book = Book('en')

    book.add_missing_pages_from(default_book)

    current_language = get_language(locale)
    current_page     = book.pages[0]

    for page in book.pages:
        if page.article.get_slug() == pk:
            current_page = page
            break

    return render(request, 'page.html', {'current_language': current_language,
                                         'languages':        Language.pool,
                                         'book':             book.pages,
                                         'page':             current_page})
