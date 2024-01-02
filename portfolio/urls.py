from django.urls import path, include
from .views import my_work, contact, about_me, shop

urlpatterns = [
    path('my_work/', my_work, name='my_work'),
    path('contact/', contact, name='contact'),
    path('about_me/', about_me, name='about_me'),
    path('shop/', shop, name='shop'),
    # path('admin/', admin.site.urls),
    # path('my_work/', include('portfolio.urls')),  # Include the portfolio app's URLs
]
