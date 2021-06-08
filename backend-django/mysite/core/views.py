import os
import json

import logging
logger = logging.getLogger(__name__)
from django.http import HttpResponse

from django.http import Http404
from django.http import HttpResponseServerError
from django.core.exceptions import EmptyResultSet

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.http import JsonResponse
from django.utils import timezone


# from django.contrib.staticfiles import finders
import pandas as pd 

 #db
# from database.orm import DBRead

#s3
from aws.s3 import s3Bucket
from aws.ses import SES

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout

import time

from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url
from database.orm import Sensors, Heartbeats, Query

dataTime= {
    "time": timezone.localtime(),
}

# views
class Home(TemplateView):
    template_name = 'home.html'

#logout
def logout_view(request):
    logout(request)
    return render(request,'home.html')

# -----------------------------------------for api-------------------------------------
class Demo(): 

    #/version/
    def version(request):  
        print("\n\n*************************************version*************************************")

        dataJson= {
            "version": "1.0"
        }

        return JsonResponse(dataJson)

    #/test/s3/
    def s3(request):  
        print("\n\n************************************* s3 test*************************************")

        #bucket='thrivee-dev/audiotranscribe'
        bucket=  'thrivee-dev'

        key= 'audiotranscribe/test.wav'

        fileName= 'media/' + key.split('/')[1]
        print(fileName)
        res= s3Bucket(bucket, key, fileName).loadFile()

        data= {
            "s3": res,
        }
        
        return JsonResponse(data)
    
    #/test/db
    def db(request):  
        print("\n\n************************************* db test*************************************")
        

        data= {
            "db test": "data"
        }
        
        return JsonResponse(data)

    def ses(request):  
        print("\n\n************************************* ese test*************************************")

        SES().gmail()

        data= {
            "ses": "ses",
        }
        
        return JsonResponse(data)

    @csrf_exempt
    def sensorsUpdate(request):  
        print("\n\n************************************* sensorsUpdate *************************************")
       
        data = json.loads(request.body) 

        if request.method == 'POST':
            print("POST...")

            sensors_id= data['sensors_id']
            serialNumber= data['serialNumber']
            metadata= data['metadata']
       
            Sensors().update(sensors_id, serialNumber, metadata)

            data_res= {
                "sensors_id": sensors_id,
                "serialNumber": serialNumber,
                "metadata": metadata,
            }

            return JsonResponse(data_res, safe=False)

    @csrf_exempt
    def heartUpdate(request):  
        print("\n\n************************************* heart *************************************")
        data = json.loads(request.body) 

        if request.method == 'POST':
            print("POST...")

            serialNumber= data['serialNumber']
            message= data['message']

            Heartbeats().update(serialNumber, message);

            data= {
                "serialNumber": serialNumber,
                "message": message,
            }

            return JsonResponse(data, safe=False)

    @csrf_exempt
    def data(request):  
        print("\n\n************************************* data *************************************")
        
        query= Query()

        data= query.all()
        
        # data_ = []
        # for da in data:
        #     data_.append(da)

        # print(data_)

        return JsonResponse(data, safe=False)



        return HttpResponse(data, content_type="application/json")

        # data= {
        #     "data": "data",
        # }
        
        # return JsonResponse(data, safe=False)


    #/api/demo
    @csrf_exempt
    def demo(request, key):  #s3 key
        print("\n\n************************************* demo *************************************")
        print(key)

        data= {
            "e": "sonething wrong",
        }       

        if request.method == 'POST':
            print("POST...")

        if request.method == 'GET':
            print("GET...")

        data= {
            "demo": "demo",
        }
        
        return JsonResponse(data)

        # data = json.loads(request.body) 
        # print(data)

        # return JsonResponse(data)

        # df= pd.DataFrame(data, index=[0])
        # return HttpResponse( df.to_html() )
    

          
