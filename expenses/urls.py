from django.urls import path

from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.logout_view, name='logout.html'),
    
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('delete_transaction/<int:transaction_id>/', views.delete_transaction, name='delete_transaction'),
    path('set_savings_goal/', views.set_savings_goal, name='set_savings_goal'),
    
]
