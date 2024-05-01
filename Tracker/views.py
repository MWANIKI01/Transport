from django.shortcuts import render

# Home
def home(request):
    return render(request, 'home/Home.html')

# Real-time Tracking
def realtime(request):
    return render(request, 'home/realtime.html')

# Closest Transport
def closest(request):
    return render(request, 'home/closest.html')


# Dashboard
def Dashboard(request):
    return render(request, 'home/Dashboard.html')

# User Authentication
def authentication(request):
    return render(request, 'home/authentication.html')

def login(request):
    return render(request, 'home/authentication/login.html')

def signup(request):
    return render(request, 'home/authentication/signup.html')

def profile(request):
    return render(request, 'home/authentication/profile.html')

# Farmer Dashboard
def farmer_dashboard(request):
    return render(request, 'farmer-dashboard/farmer-dashboard.html')

def post_request(request):
    return render(request, 'farmer-dashboard/postrequest.html')

def view_transport_history(request):
    return render(request, 'farmer-dashboard/history.html')

def market_analysis(request):
    return render(request, 'farmer-dashboard/marketanalysis.html')

def view_product_listings(request):
    return render(request, 'farmer-dashboard/productlistings.html')

# Product Listings
def product_details(request):
    return render(request, 'consumer-dashboard/productdetails.html')

def checkout(request):
    return render(request, 'consumer-dashboard/checkout.html')


# Consumer Dashboard
def consumer_dashboard(request):
    return render(request, 'consumer-dashboard/consumer-dashboard.html')

def browse_products(request):
    return render(request, 'consumer-dashboard/browseproducts.html')

def view_order_history(request):
    return render(request, 'consumer-dashboard/orderhistory.html')

def add_to_cart(request):
    return render(request, 'consumer-dashboard/addtocart.html')

def manage_profile(request):
    return render(request, 'consumer-dashboard/managerprofile.html')

# Admin Dashboard
def admin_dashboard(request):
    return render(request, 'admin-dashboard/admin-dashboard.html')

def manage_users(request):
    return render(request, 'admin-dashboard/manageusers.html')

def manage_products(request):
    return render(request, 'admin-dashboard/manageproducts.html')

def manage_requests(request):
    return render(request, 'admin-dashboard/managerequests.html')

def analytics(request):
    return render(request, 'admin-dashboard/analytics.html')

# Error Pages
def error_404(request):
    return render(request, 'error_pages/404.html')

def error_500(request):
    return render(request, 'error_pages/500.html')
