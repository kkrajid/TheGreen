from django.urls import path,include
from . import views
urlpatterns = [
    path('GroceryAdmin', views.GroceryAdmin,name='GeoceryAdmin'),

    path('dashboard', views.dashboard,name='dashboard'),

    path('customer', views.customer,name='customer'),
    path('createuser', views.createuser,name='createuser'),
    path('user_unblock/<int:u_id>',views.user_unblock,name='user_unblock'),
    path('user_blocked/<int:u_id>',views.user_blocked,name='user_blocked'),

    path('category', views.category,name='category'),
    path('categorycreate', views.categorycreate,name='categorycreate'),
    path('categorydelete/<str:userid>', views.categorydelete,name='categorydelete'), 
    path('categoryUpdate/<int:u_id>', views.categoryUpdate,name='categoryUpdate'),

    path('product', views.product,name='product'),
    path('pcreate', views.pcreate,name='pcreate'),
    path('pdelete/<int:userid>', views.pdelete,name='pdelete'),
    path('productUpdate/<int:u_id>', views.productUpdate,name='productUpdate'),
    
    path('add_banner', views.add_banner,name='add_banner'),
    path('bannercreate', views.bannercreate,name='bannercreate'),
    path('bannerdelete/<int:userid>', views.bannerdelete,name='bannerdelete'),

    path('Trending/<int:p_id>', views.Trending,name='Trending'),
    path('not_trending/<int:p_id>', views.not_trending,name='not_trending'),

    
    path('order_view', views.order_view,name='order_view'),
    path('product_view_detail/<int:ord_id>', views.product_view_detail,name='product_view_detail'),

    path('manage_order/<int:order_id>', views.manage_order, name='manage_order'),

 
    
    path('coupon_managment',views.coupon_managment,name='coupon_managment'),


    
    path('order_pdf',views.order_pdf,name='order_pdf'),

    path('add_coupon',views.add_coupon,name='add_coupon'),
    path('logout_view', views.logout_view,name='logout_view'),

    path('product/<int:product_id>/image/<int:image_id>/delete/', views.delete_image, name='delete_image'),
]
