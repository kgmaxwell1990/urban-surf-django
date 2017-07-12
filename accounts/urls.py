from django.conf.urls import url
from .views import logout, login, profile, register, cancel_subscription, subscribe, subscriptions_webhook
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete

urlpatterns = [
    url(r'^register', register, name='register'),
    url(r'^logout', logout, name='logout'),
    url(r'^login', login, name='login'),
    url(r'^profile', profile, name='profile'),
    url(r'^cancel_subscription/$', cancel_subscription, name='cancel_subscription'),
    url(r'^subscriptions_webhook/$', subscriptions_webhook, name='subscriptions_webhook'),
    url(r'^subscribe/$', subscribe, name='subscribe'),
    url(r'^password/reset/$', password_reset,
        {'post_reset_redirect': '/user/password/reset/done/'}, name='password_reset'),
    url(r'^password/reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
     password_reset_confirm, {'post_reset_redirect': '/user/password/done/'}, name='password_reset_confirm'),
    url(r'^password/done/$', password_reset_complete, name='password_reset_complete'),

]