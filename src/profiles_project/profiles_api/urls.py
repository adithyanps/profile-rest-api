from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewset, base_name='hello-viewset')
router.register('profile',views.UserProfileViewset)
router.register('login',views.LoginViewset,base_name='login')
router.register('feed',views.UserProfileFeedViewset)


urlpatterns = [
    url(r'^hello-view/',views.HelloApiView.as_view()),
    url(r'',include(router.urls)),

]
