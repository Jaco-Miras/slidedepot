from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
<<<<<<< HEAD
    RegisterViewSet,
    CommentView,
=======
    ArticleViewSet,
    CommentView,
    UserViewSet,
    CategoryView,
    PresentationView,
>>>>>>> 0e4b74dbfe5c43681675f4b7d7a9973061847952
)

router = DefaultRouter()
router.register('users', RegisterViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
<<<<<<< HEAD
=======
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:id>/', ArticleDetails.as_view()),
    # path('articles/<int:pk>', article_details),
    path('upload-presentation/', PresentationView.as_view(),name='upload-presentation'),
    path('category/', CategoryView.as_view(), name='category'),
>>>>>>> 0e4b74dbfe5c43681675f4b7d7a9973061847952
    path('comment/', CommentView.as_view(), name='comment')
]
