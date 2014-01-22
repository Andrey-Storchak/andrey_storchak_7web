from django.views.generic import TemplateView

from . import models


class HomeView(TemplateView):

    template_name= 'pynote/templates/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['notes'] = models.Note.objects.all()
        return context
