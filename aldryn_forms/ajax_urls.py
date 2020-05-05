from django.urls import path

from .views import AjaxSubmit, csrf_token_view

urlpatterns = [
    path('', AjaxSubmit.as_view(), name='aldryn_forms_ajax_submit_form'),
    path('csrf_token/', csrf_token_view, name='aldryn_forms_csrf_token'),
]
