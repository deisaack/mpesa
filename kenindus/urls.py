from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from evaluation import urls as evaluation_urls
from django.views.decorators.csrf import csrf_exempt
from evaluation.views.saf import SafView
from evaluation import views

from django.conf.urls import url, include
import oauth2_provider.views as oauth2_views
from django.conf import settings
from evaluation.views import ApiEndpoint
from evaluation.views import secret_page

from django.conf.urls import url, include
from django.contrib.auth.models import User, Group
from django.contrib import admin
admin.autodiscover()
from evaluation.models import MpesaPayment

from rest_framework import permissions, routers, serializers, viewsets

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class MpesaPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MpesaPayment
        fields= '__all__'

# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MpesaPaymentViewSet(viewsets.ModelViewSet):
    permission_classes = []
    queryset = MpesaPayment.objects.all()
    serializer_class = MpesaPaymentSerializer

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
# router.register(r'users'tt, UserViewSet)
# router.register(r'groups'tt, GroupViewSet)
router.register(r'mpesa', MpesaPaymentViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^f/', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # ...
]

# OAuth2 provider endpoints
oauth2_endpoint_views = [
    url(r'^authorize/$', oauth2_views.AuthorizationView.as_view(), name="authorize"),
    url(r'^token/$', oauth2_views.TokenView.as_view(), name="token"),
    url(r'^revoke-token/$', oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]

if settings.DEBUG:
    # OAuth2 Application Management endpoints
    oauth2_endpoint_views += [
        url(r'^applications/$', oauth2_views.ApplicationList.as_view(), name="list"),
        url(r'^applications/register/$', oauth2_views.ApplicationRegistration.as_view(), name="register"),
        url(r'^applications/(?P<pk>\d+)/$', oauth2_views.ApplicationDetail.as_view(), name="detail"),
        url(r'^applications/(?P<pk>\d+)/delete/$', oauth2_views.ApplicationDelete.as_view(), name="delete"),
        url(r'^applications/(?P<pk>\d+)/update/$', oauth2_views.ApplicationUpdate.as_view(), name="update"),
    ]

    # OAuth2 Token Management endpoints
    oauth2_endpoint_views += [
        url(r'^authorized-tokens/$', oauth2_views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
        url(r'^authorized-tokens/(?P<pk>\d+)/delete/$', oauth2_views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete"),
    ]

urlpatterns += [
    # OAuth 2 endpoints:
    url(r'^api/hello', ApiEndpoint.as_view()),  # an example resource endpoint
    url(r'^secret$', secret_page, name='secret'),

]

urlpatterns += [
    url(r"^ipn/mpesa/$", views.IPNReceiverView.as_view(), name="ipn-receiver"),
    url(r'^admin/', admin.site.urls),
    url(r'^saf/$', csrf_exempt(SafView.as_view())),
    url(r'^eval/', include(evaluation_urls, namespace='evaluation')),
]

if settings.DEBUG:
    pass
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
