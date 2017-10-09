from django.dispatch import Signal


# This is sent out when the Instant Payment Notification is received and recorded
ipn_received = Signal(providing_args=["payment", "request"])

# This is sent out when a we know what the payment is for. 'Acception'
# a payment means that we were able to match it against an order.
payment_accepted = Signal(providing_args=["mpesa_payment", "transaction"])

# This is sent out when a payment is sent but you can't tell 
# what the payment is for. In most cases you won't need to do anything when this
# happens as it could possibly mean that an IPN has been received before a corresponding
# order has been created, e.g paying for an order before pressing the PlaceOrder button.
unknown_payment_received = Signal(providing_args=["payment", "request"])
