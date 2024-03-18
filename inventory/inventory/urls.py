"""
URL configuration for inventory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from django.conf import settings
from django.contrib import admin
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.views.generic.base import RedirectView



urlpatterns = i18n_patterns(
  path('', RedirectView.as_view(url='/admin/login/'), name='home'),
  path("en/jsi18n/", JavaScriptCatalog.as_view(), name="javascript-catalog"),
  path("en/admin/", admin.site.urls),
  path("en/filer/", include("filer.urls")),
  path("en/", include("cms.urls")),
  path("en/media/", serve, {"document_root": settings.MEDIA_ROOT}),
  path("en/admin/logout/", admin.site.urls),
  path('admin/login/', admin.site.urls),
  path("", include("djangocms_page_sitemap.sitemap_urls")),
  path('en/admin/cms/placeholder/copy-plugins/', admin.site.urls, name='cms_placeholder_copy_plugins'),
  path('en/admin/cms/placeholder/add-plugin/', admin.site.urls, name='cms_placeholder_add_plugin'),
  path('en/admin/cms/placeholder/edit-plugin/([0-9]+)/', admin.site.urls, name='cms_placeholder_edit_plugin'),
  path('en/admin/cms/placeholder/delete-plugin/([0-9]+)/', admin.site.urls, name='cms_placeholder_delete_plugin'),
  path('en/admin/cms/placeholder/clear-placeholder/([0-9]+)/', admin.site.urls, name='cms_placeholder_clear_placeholder'),
  path('en/admin/cms/placeholder/move-plugin/', admin.site.urls, name='cms_placeholder_move_plugin'),
  path('en/admin/cms/placeholder/object/([0-9]+)/edit/([0-9]+)/', admin.site.urls, name='cms_placeholder_render_object_edit'),
  path('en/admin/cms/placeholder/object/([0-9]+)/structure/([0-9]+)/', admin.site.urls, name='cms_placeholder_render_object_structure'),
  path('en/admin/cms/placeholder/object/([0-9]+)/preview/([0-9]+)/', admin.site.urls, name='cms_placeholder_render_object_preview')
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('en/media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    ]