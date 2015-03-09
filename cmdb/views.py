from django.shortcuts import render
from django.template import RequestContext, loader, Context
from django.shortcuts import render_to_response
from cmdb import models
import json
from django.http import HttpResponse, JsonResponse

# Create your views here.

def login(requerst):
    # t = loader.get_template('login.html')
    # c = Context({ })

    return render_to_response('login.html')


def IpList(request):
    Ips = models.Ip_address.objects.all()

    return render_to_response('iplist.html', {'Ips': Ips})


def HostList(request):
    # Hosts = models.Host.objects.all().values()
    Hosts = models.Host.objects.all().values()
    Hosts = list(Hosts)
    jsondata = {'code': 200, 'total': len(Hosts), 'result': Hosts}
    return JsonResponse(jsondata, safe=False)
    # return HttpResponse(json.dumps(list(Hosts)), content_type='application/json')


def VmList(request):
    Vms = models.VM.objects.all()
    Vms = json.loads(Vms)

    return render_to_response('vm.html', {'Vms': Vms})