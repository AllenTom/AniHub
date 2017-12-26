from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView


class IndexView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
