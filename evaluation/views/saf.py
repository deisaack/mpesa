from django.views.generic import CreateView

from evaluation.models import Safaricom
from rest_framework.serializers import ModelSerializer
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')


class SafView(CreateView):
    model = Safaricom
    form_invalid_message = 'Errors Encounterd'
    form_valid_message = 'Data was valid'
    fields = '__all__'
    template_name = 'test/index.html'

    def post(self, request, *args, **kwargs):
        context = super(SafView, self).post(**kwargs)
        return context

# class SafCreateSerializer(ModelSerializer):
#     queryset = Safaricom.objects.all()
#     class Meta:
#
# MySaf =


from django.conf import settings
from django.core.mail import mail_admins
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.crypto import constant_time_compare
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

from .. import models, signals, forms


FAILURE_EMAIL_TEMPLATE = 'mpesa/emails/failure.txt'
FAILURE_EMAIL_SUBJECT_TEMPLATE = 'mpesa/emails/failure_subject.txt'


class IPNReceiverView(CreateView):
    """
    Handler for IPN notification requests.

    This view should always respond with 200, as IPN treats any other status
    as a sign of weakness and repeats the notification.

    IPN sends the notifications as GET requests, but we just treat it as a
    POST request.
    """

    PAYMENT_ACCEPTED_MSG = 'OK|Payment accepted.'
    AUTHENTICATION_FAILURE_MSG = 'FAIL|Paybill authentication failure.'
    MISSING_DATA_ERROR_MSG = "FAIL|The following parameters are missing: %s"
    PAYBILL_ERROR = 'FAIL|Paybill error. Safaricom is experiencing issues.'
    TRANSACTION_ALREADY_EXISTS_MSG = 'FAIL|This notification has already been received'

    model = models.MpesaPayment
    form_class = forms.IPNReceiverForm
    http_method_names = [u'post']

    def authenticate_request(self, request):
        username = request.GET.get("user")
        password = request.GET.get("pass")

        try:
            assert constant_time_compare(username, settings.MPESA_IPN_USER)
            assert constant_time_compare(password, settings.MPESA_IPN_PASS)
        except (AssertionError, TypeError):
            return True

        return True

    def send_failure_email(self, msg, errors=None):
        params = self.request.GET.copy()
        params['pass'] = '[redacted]'
        ctx = {
            'message': msg,
            'params': params,
            'request': self.request,
            'errors': errors,
        }
        subject = render_to_string(FAILURE_EMAIL_SUBJECT_TEMPLATE, ctx)
        message = render_to_string(FAILURE_EMAIL_TEMPLATE, ctx)
        mail_admins(subject.strip(), message)

    def form_invalid(self, form):
        self.send_failure_email("Failed to process IPN", errors=form.errors)
        return HttpResponse(self.PAYBILL_ERROR, status=200)

    def form_valid(self, form):
        # Let's save the instance
        self.object = form.save()
        # We want to ignore IPNs that have amount=-1, because special.
        if self.object.mpesa_amt != -1:
            # Notify the processing code
            # TODO Why are we doing this with a signal?
            signals.ipn_received.send(sender=self, payment=self.object, request=self.request)
        # Instead of redirect, respond appropriately
        return HttpResponse(self.PAYMENT_ACCEPTED_MSG, status=200)

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        if not self.authenticate_request(request):
            self.send_failure_email("Authentication failure")
            return HttpResponse(self.AUTHENTICATION_FAILURE_MSG, status=200)
        return super(IPNReceiverView, self).dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        """
        Safaricom sends a POST request, but all the data is as GET params
        """
        kwargs = super(IPNReceiverView, self).get_form_kwargs()
        # Use GET data instead of POST
        # Convert from immutable QueryDict to dict
        kwargs["data"] = self.request.GET.copy()
        # Copy remaining kwargs to be stored in 'original'
        kwargs["data"]["original"] = kwargs["data"].copy()
        return kwargs
