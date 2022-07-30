from django .urls import path
from mobileuser import views


urlpatterns=[
    path('index',views.IndexView.as_view()),
    path('p_add',views.ProductAddView.as_view(),name='pro_add'),
    path('p_list',views.ProductListView.as_view(),name='pro-list'),
    path('singleview/<str:p_id>',views.SingleProductView.as_view(),name='single_product'),
    path('p_edit/<str:p_id>',views.ProductEditView.as_view(),name='pro_edit'),
    path('p_del/<str:p_id>',views.remove,name='pro-del'),
    path('accounts/signup',views.SignUpView.as_view(),name='sign-up'),
    path('accounts/login',views.LoginView.as_view(),name='mob-user'),
    path('accounts/signout',views.SignOut,name='signout'),
]