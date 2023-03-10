from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('boss/', include('boss.urls')),
    path('delivery/', include('delivery.urls')),
    path('order/', include('order.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/', include('user.urls'))    
]