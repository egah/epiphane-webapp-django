from django.shortcuts import render
from django.views.generic import (
    TemplateView,
)


class MyHomePage(TemplateView):
    template_name = "portfolio_epiphane/resume.html"
