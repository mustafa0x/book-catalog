#from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from book_catalog.models import Series, Book, News, Page, files_dir
from book_catalog.settings import MEDIA_URL
#import pdb; pdb.set_trace()

home = ("/", "Home")
catalog_breadcrumb = ("/catalog", "Book Catalog")

def index(request):
    return render_to_response("index.html",
        {"breadcrumbs": [home], "news": News.objects.filter(visible=1)},
        context_instance=RequestContext(request))

def page(request, page):
    page_item = get_object_or_404(Page, slug=page)
    return render_to_response("page.html",
        {"page": page_item, "breadcrumbs": [home, (page_item.slug, page_item.title)]},
        context_instance=RequestContext(request))

def catalog(request):
    return render_to_response("catalog.html",
        {"breadcrumbs": [home, catalog_breadcrumb], "pdf_catalog_dir": MEDIA_URL + files_dir},
        context_instance=RequestContext(request))

def series(request, series):
    series_item = get_object_or_404(Series, slug=series)
    return render_to_response("series.html", {"series_item": series_item,
            "breadcrumbs": [home, catalog_breadcrumb, ('', series_item.title)]},
        context_instance=RequestContext(request))

def book(request, series, book):
    book_item = get_object_or_404(Book, slug=book)
    
    return render_to_response("book.html", {"book_item": book_item,
            "breadcrumbs": [home, catalog_breadcrumb, (catalog_breadcrumb[0] + "/" + series, book_item.series), ('', book_item.title)]},
        context_instance=RequestContext(request))
