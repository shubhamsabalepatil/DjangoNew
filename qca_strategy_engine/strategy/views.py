from rest_framework.decorators import api_view
import subprocess
from django.http import HttpResponse
import sys

# Create your views here.


@api_view(['GET'])
def script1(r):

    obj = subprocess.Popen([sys.executable,'strategy//scripts//script1.py'])
    PID = obj.pid
    print('PID for process', PID)



    return HttpResponse('Script excecuted')


def script2(r):

    obj = subprocess.Popen([sys.executable,'strategy//scripts//script2.py'])
    PID = obj.pid
    print('PID for process', PID)

    return HttpResponse('Script excecuted')


def script3(r):

    obj = subprocess.Popen([sys.executable,'strategy//scripts//script3.py'])
    PID = obj.pid
    print('PID for process', PID)


    return HttpResponse('Script excecuted')



