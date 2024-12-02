from django.urls import path
from .views import HomeView, AboutView, ProductsView, BlogView, ContactView

app_name = 'sayt'

urlpatterns = [
    path('', HomeView.as_view(), name="home_page"),
    path('about/', AboutView.as_view(), name="about_page"),
    path('products/', ProductsView.as_view(), name="products_page"),
    path('blog/', BlogView.as_view(), name="blog_page"),
    path('contact/', ContactView.as_view(), name="contact_page"),
]