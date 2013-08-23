# Create your views here.

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.template.response import TemplateResponse

from models import DataDict

class DataDictList(ListView):
	model = DataDict
	queryset = DataDict.objects.order_by('order')
	context_object_name = 'data_dict_list'

class DataDictCreate(CreateView):
    model = DataDict
    fields = ['name']

class DataDictUpdate(UpdateView):
    model = DataDict
    fields = ['name']

class DataDictDelete(DeleteView):
    model = DataDict
    success_url = reverse_lazy('author-list')
