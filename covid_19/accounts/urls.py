from django.urls import path ,reverse_lazy
from . import views
from django.conf.urls.static import static  
from django.contrib.auth.views import LogoutView
from .views import Sign_Up,Login
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.Sign_Up, name='signup'),
    path('Loggin_in/', views.Loggin_in, name='Loggin_in'),
    path('login/', views.Login, name='login'),
    path('logout/',LogoutView.as_view(next_page = reverse_lazy('accounts:login')) ,  name="logout"),
    #path('Profile/', views.Profile ,name= 'Profile' ),
    path('dashboard/', views.dashboard ,name= 'dashboard' ),
  
 
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)