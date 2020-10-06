from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('register', views.register,name='registration'),  
    path('signin', views.signin,name='signin'),  
    path('emp', views.emp,name='emp'),  
    path('show',views.show,name='show')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)