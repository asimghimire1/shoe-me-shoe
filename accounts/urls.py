
from django.urls import path
from .views import (
    signup,
    login_view,
    home,
    logout_view,
    men_view,        
    women_view,
    kids_view,
    personalize_view,
    sales_view,
    trending_view,
    brands_view,
    product1,
    product2,
    shop,
    brands,

)
app_name = 'accounts'

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),  
    path('logout/', logout_view, name='logout'),
    path('men/', men_view, name='men'),  
    path('women/', women_view, name='women'),  
    path('kids/', kids_view, name='kids'),  
    path('personalize/', personalize_view, name='personalize'),  # Personalize page
    path('sales/', sales_view, name='sales'),  # Sales page
    path('trending/', trending_view, name='trending'),  # Trending page
    path('brands/', brands_view, name='brands'),
    path('product1/', product1, name='product1'),
    path('shop/', shop, name='shop'),
    path('brands/', brands, name='brands'),

]
