from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, render_to_response
from datetime import datetime
from .schedule import trains
import re

format = '%I%M%p'


def home(request):
    return render(request, 'home.html')


@csrf_exempt
def sms(request):
    body = request.GET.get('Body', '')
    nb = int('nb' in body.lower())
    train = re.findall('[EF]', body)[0]
    stop = re.findall('to (.*)$', body)[0]
    print(train, nb, stop)
    print(trains[train][nb][stop])
    sched = [datetime.strptime(t, format) for t in trains[train][nb][stop]]
    now = datetime.now()
    for time in sched:
        if (time.hour == now.hour and time.min - now.min > 15) or time.hour > now.hour:
            next_train = time.strftime('%H:%M')
            break
    else:
        next_train = sched[0].strftime('%H:%M')

    twiml = '<Response><Message>Next {} Train is coming to {} at {}</Message></Response>'.format(
        train, stop, next_train
    )
    return HttpResponse(twiml, content_type='text/xml')
