from django.db import models

covers_dir = 'covers'
files_dir = 'files'

def dynamic_upload(instance, filename):
    return covers_dir + "/" + instance.slug + "/" + filename;

class Page(models.Model):
    title = models.CharField(max_length=100)

    slug = models.SlugField(blank=True)
    slug.help_text = "If a normal page, what URL to use? This is automatically derived from the title, but can and should be tweaked."

    content = models.TextField(blank=True)
    content.help_text = "For pages only, ignored if an external link or attachment. HTML is allowed."

    link = models.CharField(max_length=250, blank=True)
    link.help_text = "If you want this to simple be an external link."

    attachment = models.FileField(upload_to=files_dir, blank=True)
    attachment.help_text = "If you want this to be a file."

    display_order = models.IntegerField(max_length=2)
    position = models.BooleanField(choices=((1, "Top Menu"), (0, "Side Menu")))


    class Meta:
        ordering = ['display_order']
 
    def __unicode__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date = models.DateField()
    visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "News"
        ordering = ['-date']

    def __unicode__(self):
        return self.title

class Option(models.Model):
    name = models.CharField(max_length=200)
    value = models.TextField(blank=True)
    meta = models.CharField(max_length=300, blank=True)

    def __unicode__(self):
        return self.name

class Series(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    slug.help_text = "What URL to use for this series? This is automatically derived from the title, but can and should be tweaked."
    description = models.TextField()
    image = models.ImageField(upload_to=covers_dir, blank=True)
    display_order = models.IntegerField(max_length=2)

    class Meta:
        verbose_name_plural = " Series"
        ordering = ['display_order']

    def __unicode__(self):
        return self.title

# print details e.g. 2 colors
# cover thumb, full, both sides
class Book(models.Model):
    series = models.ForeignKey(Series)
    title = models.CharField(max_length=100)

    slug = models.SlugField()
    slug.help_text = "What URL to use for this book? This is automatically derived from the title, but can and should be tweaked."

    sub_title = models.CharField(max_length=100, blank=True)

    series_item = models.IntegerField(max_length=2)
    series_item.help_text = "What part of the series is this?"

    price = models.DecimalField(max_digits=5, decimal_places=2)
    price.help_text = "Numbers only"

    purchase_link = models.CharField(max_length=250, blank=True)
    purchase_link.help_text = "If you wish to provide the visitor with an external place of purchase."

    published = models.DateField()
    description = models.TextField()
    pages = models.IntegerField(max_length=4)
    isbn = models.CharField(max_length=15)
    edition = models.CharField(max_length=30)
    binding = models.CharField(max_length=40, blank=True)
    dimensions = models.CharField(max_length=50, blank=True)
    cover = models.ImageField(upload_to=covers_dir, blank=True)
    toc = models.FileField(upload_to=files_dir, blank=True)
    extract = models.FileField(upload_to=files_dir, blank=True)

    class Meta:
        ordering = ['series_item']

    def __unicode__(self):
        return self.title
