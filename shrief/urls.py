
# from .routers import router
from .views import home
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
# from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', home.index),
    # path('rent/', include('shop.urls')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('User/', include('Users.urls')),

    # path('Products/', include('Products.urls')),
    path('Records/', include('Records.urls')),
    # path('api/', include(router.urls)),
    # path('', home.index),
    # path('login/', login, name='login'),

    path('', include('Products.urls', namespace='Home')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'Products.views.error_404_view'
