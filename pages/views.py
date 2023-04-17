from django.views.generic import TemplateView, DeleteView, UpdateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class ContentPageView(TemplateView):
    template_name = 'content.html'
