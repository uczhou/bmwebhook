from django.shortcuts import render
from plivo import plivoxml

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the sms index.")


def get_parameters(request, *args):

    if request.method == 'GET':
        # Sender's phone number
        from_number = request.GET.get('From')

        # Receiver's phone number - Plivo number
        to_number = request.GET.get('To')

        # The text which was received
        text = request.GET.get('Text')

        return from_number, to_number, text
    elif request.method == 'POST':
        # Sender's phone number
        from_number = request.POST.get('From')

        # Receiver's phone number - Plivo number
        to_number = request.POST.get('To')

        # The text which was received
        text = request.POST.get('Text')

        return from_number, to_number, text

    else:
        return None, None, None

def receive_sms(request):

    from_number, to_number, text = get_parameters(request)

    # Log the message
    message = 'From: {}, To: {}, Text: {}'.format(from_number, to_number, text)

    print(message)

    return HttpResponse("Message received", status=200)


def inbound_sms(request):

    from_number, to_number, text = get_parameters(request)

    # Log the message
    message = 'From: {}, To: {}, Text: {}'.format(from_number, to_number, text)


    print(message)
    # To reply to the SMS sender,
    # set the from number received in the request
    # as the dst number in the Message XML we return.
    #
    # To forward the message to another number,
    # set it as dst number in the Message XML.
    params = {
      "src": to_number,
      "dst": from_number,
    }

    body = "Thanks, we've received your message."

    # Generate a Message XML with the details of
    # the reply to be sent.
    r = plivoxml.Response()
    r.addMessage(body, **params)
    print(r.to_xml())

    return HttpResponse(str(r), content_type='text/xml')
    # return Response(str(r),mimetype='text/xml')


def report(request):
    # Sender's phone number
    from_number = request.values.get('From')

    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')

    # Status of the message
    status = request.values.get('Status')

    # Message UUID
    uuid = request.values.get('MessageUUID')

    # Log the message
    message = 'From: {}, To: {}, Status: {}, MessageUUID: {}'.format(from_number, to_number, status, uuid)
    # app.logger.info(message)

    print(message)

    return HttpResponse("Delivery status reported")