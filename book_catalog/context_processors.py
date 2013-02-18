from book_catalog.models import Series, Page, Option

def populate_menus(request):
    return {"series_all": Series.objects.all(),
        "top_menu": Page.objects.filter(position=1),
        "side_menu": Page.objects.filter(position=0)}

def options(request):
    return {"options": dict([x.name, x.value] for x in Option.objects.all())}
