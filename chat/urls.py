from django.urls import re_path
from .views import ChatView

app_name = "chat"

urlpatterns = [re_path("^$", ChatView.as_view(), name="chat_view")]