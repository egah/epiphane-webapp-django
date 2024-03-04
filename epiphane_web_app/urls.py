from django.urls import re_path, path, include
from django.contrib import admin

# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.static import serve
from portfolio_epiphane import views

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("^$", views.MyHomePage.as_view(), name="homepage"),
    re_path("^publications/$", views.Publications.as_view(), name="publications"),
    re_path("^nlp-task/$", views.nlptask, name="nlp-task"),
    re_path("^chat/", include("chat.urls")),
    # re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
