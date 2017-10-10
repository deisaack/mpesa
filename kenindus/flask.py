# import the Flask Framework
from flask import Flask,jsonify, make_response, request

app = Flask(__name__)

# Create the context (endpoint/URL) which will be triggered when the request
# hits the above specified port. This will resolve to a URL like
# 'http://address:port/context'. E.g. the context below would
# resolve to 'http://127.0.0.1:80/mpesa/b2c/v1' on the local computer. Then
# the Handler will handle the request received via the given URL.

# You may create a separate URL for every endpoint you need

@app.route('/wait/', methods = ["POST"])
def listenB2c():
    #save the data
    request_data = request.data

    #Perform your processing here e.g. print it out...
    print(request_data)

    # Prepare the response, assuming no errors have occurred. Any response
    # other than a 0 (zero) for the 'ResultCode' during Validation only means
    # an error occurred and the transaction is cancelled
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": "1234567890"
    };

    # Send the response back to the server
    return jsonify({'message': message}), 200

# Change this part to reflect the API you are testing
@app.route('/mpesa/b2b/v1')
def listenB2b():
    request_data = request.data
    print(request_data)
    message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": "1234567890"
    };

    return jsonify({'message': message}), 200

if __name__ == '__main__':
    app.run(debug=True)