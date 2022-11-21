from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import CVE, NetworkDevice
from modules.base_parser import BaseParser
from modules.base_parser_settings import SETTINGS


def show_cve(request, cve_name):
    cve = CVE.objects.filter(name=cve_name)
    response = serializers.serialize('json', cve)
    return HttpResponse(response, content_type="text/json-comment-filtered")

def load_cve(request):
    bp = BaseParser(SETTINGS)
    cve_base = bp.start()
    for cve in cve_base:
        cve_obj = CVE.objects.create(
                    name = cve['name'],
                    severity =  cve['severity'],
                    url = cve['url'],
                    platforms = cve['platforms'],
                    affected_junos = cve['affected_junos'],  
                    tags = cve['tags']                    
                  )
        cve_obj.save()
    return HttpResponse('CVE base has been loaded!')

def show_networkdevice(request, networkdevice_name):
    networkdevice = NetworkDevice.objects.filter(name=networkdevice_name)
    response = serializers.serialize('json', networkdevice)
    return HttpResponse(response, content_type="text/json-comment-filtered")


def load_networkdevice(request):
    return HttpResponse('Network device base has been loaded!')


