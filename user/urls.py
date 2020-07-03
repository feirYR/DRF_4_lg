from django.urls import path
from user import views
urlpatterns=[
    # path('lg/',views.UserAPIView.as_view({'post':'register'})),
    # path('lg/<str:id>/',views.UserAPIView.as_view({'post':'login'})),
    path('lg/<str:username>/',views.UserAPIView.as_view({'post':'login'})),
    path('lg/',views.UserAPIView.as_view({'post':'login'})),
    # path('UserView/<str:id>/',views.UserView.as_view()),
    path('query/',views.QueryAPIView.as_view())
]