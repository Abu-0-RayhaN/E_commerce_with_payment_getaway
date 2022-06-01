from unicodedata import name
from django.urls import path
from.import views
urlpatterns = [
    path('checkout/',views.checkout,name="checkout"),
    path('pay/',views.payment,name="payment"),
    path('status/',views.complete,name='complete'),
    path('purchased/<val_id>/<tran_id>/',views.purchased,name="purchased"),
    path('orders/',views.order_view,name="orders"),
]
