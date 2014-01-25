from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy

from . import models
from . import forms


class HomeView(TemplateView):

    template_name = 'pynote/templates/index.html'

    def get_context_data(self, **kwargs):
        '''Add notes list to context'''
        context = super(HomeView, self).get_context_data(**kwargs)
        context['notes'] = models.Note.objects.all()
        return context


class AddNoteView(FormView):
    '''Add note view'''
    template_name = 'pynote/templates/add_note.html'
    form_class = forms.NoteForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return redirect(reverse_lazy('home'))
