from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'test_img'

urlpatterns = [
  #  path('test/', views.test_img ,name= 'test_img' ),
    path('total_cases/', views.total_cases ,name= 'total_cases' ),
    path('image_upload/', views.image_upload ,name= 'image_upload' ),
    
 
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)