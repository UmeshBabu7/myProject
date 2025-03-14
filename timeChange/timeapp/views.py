from django.shortcuts import render
import datetime

# Create your views here.

def index(request):
    date=datetime.datetime.now()
    msg=" Hello guest ! , "

    h=int(date.strftime(" %H "))

    # logic
    if h<12:
        msg += " Good Morning "
    elif h<16:
        msg += " Good Afternoon "

    elif h<20:
        msg +=" Good Evening "
    
    else:
        msg +=" Good Night "
    
    context={
        "date": date,
        "msg": msg
    }

    return render(request,"timeapp/index.html",context)

