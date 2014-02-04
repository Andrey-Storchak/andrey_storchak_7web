from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.template import Context


from libs.helpers import convert_context_to_json
from libs.helpers import render_to_json_response

from apps.pynote import models
from apps.pynote import forms


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
        context = {'request_result': _('success'),
                   'message': _('Note added successfuly.')}
        return render_to_json_response(context)

    def form_invalid(self, form):
        context = {'request_result': _('error'),
                  'message': _('Error occured.')}
        context['form_errors'] = form.errors
        return render_to_json_response(context)

