from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/",views.index, name = 'index'),
    path("signup/",views.signup, name = 'signup'),
    path("",views.home, name = 'home'),
    path("contact/",views.contact,name='contact'),
    path("logout/",views.logout,name='logout'),
    path("b_library/",views.b_library,name='b_library'),
    path("lib_policy/",views.lib_policy,name='lib_policy'),
    path("member/",views.member,name='member'),
    path("facility/",views.facility,name='facility'),
    path("lending/",views.lending,name='lending'),
    path("con/",views.con,name='con'),
    path('search/', views.search_books, name='search_books'),
    # Password reset URLs
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

