from django.urls import path, include
from .views import *
from .context_processors import result, html_to_pdf_view

urlpatterns = [
    path('', main, name='main'),
    path('page/<str:slug>/', page, name='page'),
    path('form/', form, name='accept'),
    path('labs', labs, name='labs'),
    path('news', all_news, name='news'),
    path('news/<str:slug>', news, name='news'),
    path('prices', prices, name='prices'),
    path('clinic', clinic, name='clinic'),
    path('specialists', specialists, name='specialists'),
    path('services', services, name='services'),
    path('services/<str:slug>/', service, name='services'),
    path('review/<int:id>/', review, name='review'),
    path('result', result, name='result'),
    path('api/v1/', include('api.urls')),
    path('download/<int:oder_number>/<int:pin>/', html_to_pdf_view, name='html_to_pdf_view'),
]