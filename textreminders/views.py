from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from textreminders.util import ResponseHandler
from textreminders.util.schedule import TRAINS

format = '%I%M%p'


def home(request):
    return render(request, 'home.html')


@csrf_exempt
def sms(request):
    body = request.GET.get('Body', '')
    if not body:
        return HttpResponse('<p> Hi! </p>', content_type='text/html')

    rh = ResponseHandler(body)
    twiml = rh.create_response()
    # move this somewhere else

    # now = datetime.now()
    # for time in sched:
    #     if (time.hour == now.hour and time.minute - now.minute > 15) or time.hour > now.hour:
    #         next_train = time.strftime('%H:%M')
    #         break
    # else:
    #     next_train = sched[0].strftime('%H:%M')

    return HttpResponse(twiml, content_type='text/xml')
