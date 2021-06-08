from django.conf import settings
from .models import Sensor, Heartbeat
from .serializers import SensorSerializer, HeartbeatSerializer
import json

from django.core import serializers

class Heartbeats():
    def __init__(self):
        self.print= None
     
    def all(self):
        print("all")
        e= Heartbeat.objects.all()
        serializer = HeartbeatSerializer( e, many=True)
        data= serializer.data

        return data        

    def getMessage(self, heartbeat_id):
        message= Heartbeat.objects.values_list('message', flat=True).get(pk__in= heartbeat_id )
        return message

    def update(self, serialNumber, message):
        print("update")

        heartbeat_id= str( Sensors().getHeartbeat_id(serialNumber) )
        message_old= self.getMessage(heartbeat_id)

        # update state
        state= 0 if int(message) < message_old or int(message) > message_old + 10 * 60 else 1
        print("old message", message_old)
        print("new message", message)
        print("new state", state)

        # update Heartbeat with new state and message
        e= Heartbeat.objects.filter(pk__in= heartbeat_id)
        e.update(message= message, state= state)

class Sensors():
    def __init__(self):
        self.print= None

    def getHeartbeat_id(self, serialNumber):
        Heartbeat_id= Sensor.objects.values_list('heartbeat', flat=True).get(serialNumber=serialNumber)
        return Heartbeat_id

    def update(self, sensors_id, serialNumber, metadata):
        e= Sensor.objects.filter( pk__in= str(sensors_id) )
        if metadata: e.update(metadata= metadata)
        if serialNumber: e.update(serialNumber= serialNumber)

    def all(self):
        print("all")
        e= Sensor.objects.all()
        serializer = SensorSerializer( e, many=True)
        data= serializer.data

        # for da in data:
        #     state= self.getState( int(da['state']) )
        #     da['state']=  state

        return data


class Query():
    def __init__(self):
        print("Query")
        self.print= None  

    def getHeartbeat(self, heartbeat_id):
        e = Heartbeat.objects.filter(pk__in= heartbeat_id)
        data= [x for x in e.values()]
        data= data[0]

        # print("111", data)
        # data['state']= 0
        return data

    def heartUpdate(self, serialNumber, message):
        print("heartUpdate")
        print(serialNumber, message)
        heartbeat_id= Sensors().getHeartbeat_id( serialNumber )
        print("heartbeat_id", heartbeat_id)


    def all(self):
        print("all")
        e = Sensor.objects.all().select_related('heartbeat')
        data = e.values()

        data_dic= []
        for row in data:
            heartbeat = self.getHeartbeat( str(row['heartbeat_id'] ) )
            row['heartbeat']=  heartbeat

            # row['heartbeat'].state= "offline"


            data_dic.append(row)

        print(data_dic)
        return data_dic

# class Query():
#     def __init__(self):
#         print("Query")
#         self.print= None  

#     def all(self):
#         print("all")

        # queryset= Sensor.objects.select_related('serialNumber')
        # print(str(queryset))

        # queryset= Sensor.objects.all().values_list()
        # print(str(queryset))

        # q1= Sensor.objects.select_related('serialNumber')
        # print(q1)


# books = Book.objects.all().select_related("author")
# for book in books:
#     print(book.author.name)  # Evaluates the query set, caches in memory results
# first_book = books[1]  # Does not hit db
# print(first_book.author.name)  # Does not hit db 

        # children_ids = ParentModel.objects.filter(name__startswith='A').values_list('child', flat=True)
        # children = ChildModel.objects.filter(pk__in=children_ids)
        
        # heartbeat_ids = Sensor.objects.all().values_list('heartbeat', flat=True)
        # heartbeat = Heartbeat.objects.filter(pk__in=heartbeat_ids)
        # print("aaaaaaaaaaaa", heartbeat_ids)
        # print("bbbbbbbbbbbb", heartbeat.values_list())

        # # Parent.objects.prefetch_related('child_set')
        # # sensors= Sensor.objects.prefetch_related('heartbeat')
        # # print("0000", sensors.values_list())

        # e = Sensor.objects.all().select_related('heartbeat')
        # print("0000", type(e), e.values_list())
        # serializer = SensorSerializer(e, many=True)
        # print("11111", type(serializer), serializer )


        # for sensor in e:
        #     print(sensor.heartbeat.message)  # Does not hit db 

        # data = serializers.serialize('json', e)

        # print("22222", data)
        # print("22222", serializer.data)



        # return serializer.data
        # q1= Sensor.objects.select_related('serialNumber')
        # print(q1)


        # for heartbeat in heartbeats.items():
        #     print( heartbeat['serialNumber'] )

        # serialNumbers= [ heartbeat['serialNumber'] for heartbeat in heartbeats]
        # print(serialNumbers)





    # def getState(self, state):
    #     print("getState")
    #     message= Heartbeats().filter(state)
    #     return message


# class DBRead():
#     def __init__(self):
#         self.print= None
     
#     def ml_test(self, name="hunter"):
#         try:
#             e= Ml_test.objects.filter( name= name )
#         except:
#             raise Http404("can not access to mysql")

#         serializer = Ml_testSerializer( e, many=True)
        
#         if not serializer.data:
#             raise Http404("filename can not found in table")

#         return serializer.data



    # def update(self, filename=None, transcription=None):
    #     try:
    #         e= Teleconference_transcribe.objects.filter( filename= filename )
    #     except:
    #         raise Http404("can not access to mysql")

    #     serializer = Teleconference_transcribeSerializer( e, many=True)
        
    #     if not serializer.data:
    #         raise Http404("filename can not found in table")

    #     row= e.update(transcription_baseline= transcription)
    #     print("successfully update db ")

    #     return serializer.data



     








         
 #print(timeslot)

        # today= datetime.date.today() 
        # TimeslotToday= Timeslot.objects.filter( start_date__range=(today, today + datetime.timedelta(days=1)) )
        # print("TimeslotToday:  ",TimeslotToday)

        # minute = datetime.timedelta(minutes=500)
        # today= datetime.date.today() 
        # now= datetime.datetime.now()
     

        # print("st    ", datetime.datetime(2019, 11, 15, 15, 30) )
        # x=              datetime.datetime.utcnow()
        # x=              datetime.datetime(2019, 11, 15, 16, 30) 
        # x= now
        # print("xx    ", x )
        # print("ed    ", datetime.datetime(2019, 11, 15, 17, 30))

     
        #inSlot_ = Timeslot.objects.filter(start_date__lt= x, end_date__gt= x)

        #inSlot= Timeslot.objects.filter( start_date__lt= now + minute ).filter( end_date__gt= now - minute )

        #inSlot= Timeslot.objects.filter( start_date__lt= now ).filter( end_date__gt= now ) # utc

        # TimeslotToday= Timeslot.objects.filter( start_date__range=(today, today + datetime.timedelta(days=1)) )
        # print("TimeslotToday:  ",TimeslotToday)
        #2019-11-15 15:30:00  -  2019-11-15 16:30:00