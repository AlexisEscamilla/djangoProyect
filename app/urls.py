from . import views
from django.urls import path
from .views import EmisionesAPIView
app_name = 'app'

urlpatterns = [
    path('', views.vector_maps, name='index'),
    path('vector-maps', views.vector_maps, name='vector-maps'),
    path('canada', views.canada, name='canada'),
    path('russia', views.russia, name='russia'),
    path('spain', views.spain, name='spain'),
    path('mexico', views.mexico, name='mexico'),
    path('italy', views.italy, name='italy'),
    path('usa', views.usa, name='usa'),
    path('countries', views.countries, name='countries'),
    path('widgets', views.widgets, name='widgets'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('get-answer/', views.get_gemini_answer, name='get_gemini_answer'),
    #Mi api
    path('api/emisiones/', EmisionesAPIView.as_view(), name='emisiones-api'),  # Assuming you have a view called `country_page`
]