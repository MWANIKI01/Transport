

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
   
    # Real-time Tracking
    path('realtime/', views.realtime, name='realtime'),

    # Closest Transport
    path('closest/', views.closest, name='closest'),


    # Dashboard
     path('Dashboard/', views.Dashboard, name='Dashboard'),
     path('Dashboard/farmer-dashboard/', views.farmer_dashboard, name='farmer-dashboard'),
     path('Dashboard/consumer-dashboard/', views.farmer_dashboard, name='consumer-dashboard'),
     path('Dashboard/admin-dashboard/', views.farmer_dashboard, name='admin-dashboard'),
 
 

    # User Authentication
    path('authentication/', views.authentication, name='authentication'),
    path('authentication/login/', views.login, name='login'),
    path('authentication/signup/', views.signup, name='signup'),
    path('authentication/profile/', views.profile, name='profile'),

    #farmers Dashboard
    path('farmerdashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('farmerdashboard/postrequest/', views.post_request, name='post_request'),
    path('farmerdashboard/viewtransporthistory/', views.view_transport_history, name='view_transport_history'),
    path('farmerdashboard/viewproductlistings/', views.view_product_listings, name='view_product_listings'),
    path('farmerdashboard/marketanalysis/', views.market_analysis, name='market_analysis'),


    # Consumer Dashboard
    path('consumerdashboard/', views.consumer_dashboard, name='consumer_dashboard'),
    path('consumerdashboard/browseproducts/', views.browse_products, name='browse_products'),
    path('consumerdashboard/browseproducts/productdetails/', views.product_details, name='product_details_consumer'),
    path('consumerdashboard/browseproducts/addtocart/', views.add_to_cart, name='add_to_cart'),
    path('consumerdashboard/browseproducts/checkout/', views.checkout, name='checkout_consumer'),
    path('consumerdashboard/vieworderhistory/', views.view_order_history, name='view_order_history'),
    path('consumerdashboard/manageprofile/', views.manage_profile, name='manage_profile'),

  # Admin Dashboard
    path('admindashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admindashboard/manageusers/', views.manage_users, name='manage_users'),
    path('admindashboard/manageproducts/', views.manage_products, name='manage_products'),
    path('admindashboard/managerequests/', views.manage_requests, name='manage_requests'),
    path('admindashboard/analytics/', views.analytics, name='analytics'),

    # Error Pages
    path('404/', views.error_404, name='error_404'),
    path('500/', views.error_500, name='error_500'),
]
