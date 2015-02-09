from django.shortcuts import render
from django.template import RequestContext, loader, Context
from django.shortcuts import render_to_response


# Create your views here.

def login(requerst):
    # t = loader.get_template('login.html')
    # c = Context({ })

    return render_to_response('login.html')