from django.shortcuts import render
from django.views.generic import (
    TemplateView,
)
from .forms import Message


class MyHomePage(TemplateView):
    template_name = "portfolio_epiphane/resume.html"


class Publications(TemplateView):
    template_name = "portfolio_epiphane/publications.html"


class Chat(TemplateView):
    template_name = "chat/chat.html"


def nlptask(request):

    if request.method == "POST":
        form = Message(request.POST)
        if form.is_valid():
            print("Validation success!")
            print("Name: " + form.cleaned_data["text"])
    else:
        form = Message()

    return render(request, "portfolio_epiphane/nlp-task.html", {"form": form})
