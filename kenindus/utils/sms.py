from .AfricasTalkingGateway import (AfricasTalkingGateway,
                                    AfricasTalkingGatewayException)

try:
	# Thats it, hit send and we'll take care of the rest.

	results = gateway.sendMessage(to, message)

	for recipient in results:
		# status is either "Success" or "error message"
		print (
		'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
		                                              recipient['status'],
		                                              recipient['messageId'],
		                                              recipient['cost']))

except AfricasTalkingGatewayException as e:
	print (
	'Encountered an error while sending: %s' % str(e))
