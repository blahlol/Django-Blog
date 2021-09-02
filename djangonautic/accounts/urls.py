from django.urls  import path
from . import views

app_name="accounts"

urlpatterns=[
    path('profile/<id>/',views.profile,name='profile'),
    # path('find/<value>/',views.find,name='find'),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('signup/',views.signup_view,name='signup'),
]
