from django.urls import path
from contact import views 
from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    
    # contact CRUD
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update', views.update, name='update'),
    path('contact/<int:contact_id>/delete', views.delete, name='delete'),

    # USER
    path('user/create/', views.register, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)