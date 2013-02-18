
from django.conf.urls.defaults import url, patterns

from contact_form import views, forms

urlpatterns = patterns('',
    url(r'^$', views.ContactFormView.as_view(
        template_name="contact_form/contact.html",
        get_context_data=lambda form: {"form": form, "breadcrumbs": [("/", "Home"), ('/contact', "Contact Us")]},
        form_class=forms.BasicContactForm,
    ), name="contact"),
    url(r'^completed/$', views.CompletedPage.as_view(get_context_data=lambda: {"breadcrumbs": [("/", "Home"), ('/contact', "Contact Us")]}), name="completed"),
)
