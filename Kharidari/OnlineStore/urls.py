from OnlineStore.views import home,cart,checkout,contact,shop,shopGrid,blog,blogSide,service,product,page
from django.urls import path

urlpatterns = [
    path('',home,name='home'),
    path('cart/',cart,name='cart'),
    path('checkout/',checkout,name='checkout'),
    path('contact/',contact,name='contact'),
    path('shop_grid/',shopGrid,name='shopGrid'),
    path('blogside/',blogSide,name='blogSide'),
    path('product/',product,name='product'),
    path('service/',service,name='service'),
    path('shop/',shop,name='shop'),
    path('blog/',blog,name='blog'),
    path('page/',page,name='page'),
]
