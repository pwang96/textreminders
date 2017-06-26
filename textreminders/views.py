import json

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt

from textreminders.util import ResponseHandler, add_verified_number
from textreminders.forms import NumberForm


def home(request):
    return render(request, 'home.html')


@csrf_exempt
def sms(request):
    body = request.GET.get('Body', '')
    if not body:
        return HttpResponse('<p> Hi! </p>', content_type='text/html')

    rh = ResponseHandler(body)
    twiml = rh.create_response()

    return HttpResponse(twiml, content_type='text/xml')


@csrf_exempt
def new_number(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NumberForm(request.POST)

        print(form)
        if form.is_valid():
            data = form.cleaned_data
            verification_code = add_verified_number.add_verified_number(data['your_number'], data['your_name'])
            return render(request,
                          'number.html', {'code': verification_code},
                          content_type='text/html')
        else:
            print("INVALID FORM")

    return render_to_response('home.html')
