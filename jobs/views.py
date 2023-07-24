from datetime import datetime
from django.shortcuts import render
from . models import Working
from django.db.models import Sum

def index(request):
    work=Working.objects.filter(name='Anu')
    thour=0
    otime=0
    for a in work:
        s1 = str(a.start)
        s2 = str(a.end)
        start_dt = datetime.strptime(s1, '%H:%M:%S')
        end_dt = datetime.strptime(s2, '%H:%M:%S')
        diff = (end_dt - start_dt)
        days = diff.days
        days_to_hours = days * 24
        diff_btw_two_times = (diff.seconds) / 3600
        overall_hours = days_to_hours + diff_btw_two_times
        thour=thour+overall_hours
        if a.lunch=='Yes' and a.holyday=='No' and overall_hours>7:
            overall_hours=overall_hours-1
            otime=overall_hours-7
        if a.lunch=='No' and a.holyday=='Yes':
            otime=overall_hours
        if a.lunch=='No' and a.holyday=='No':
            otime=overall_hours
        if a.lunch=='Yes' and a.holyday=='Yes':
            overall_hours=overall_hours-1
            otime=overall_hours
        print("WH",overall_hours)
    print("TT",thour)
    print("TOT",otime)
    context= {
        'work': work
    }
    return render(request, "index.html", context)
