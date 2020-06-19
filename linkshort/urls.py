from django.conf.urls import handler404
from django.urls import include, path

import links.urls
import bots.urls

urlpatterns = [
    path('', include(links.urls)),
    path('bots/', include(bots.urls))
]

handler404 = links.views.file_404
