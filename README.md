

#### task

Your task is to accomplish the following:

Use Django (or some similar Python web framework) to build a web application
Scaffold a database that includes **sensors** and **heartbeats**
A sensor is a device in the field. It generally includes a serial number and other metadata
A heartbeat is a periodic message used to tell the backend that the sensor is online and provide the current state of the sensor
It is left as an exercise to the candidate to define exactly what data is stored (as well as how it is stored) for a sensor and a heartbeat
Expose an endpoint that can receive "heartbeats" indicating that the sensor is alive and checking in
Deliver a webpage where a user can view live, updating heartbeats from the sensors
Deliver a script that can emulate one or many sensors by sending **emulated heartbeats** to the "heartbeats" endpoint.
Bonus Points: Build or tell us how you would include a way to alert users if a sensor hasn’t sent a heartbeat in the last 10 minutes.

#### database

![alt text](https://github.com/taixingbi/sensors-monitor/blob/main/backend-django/QuickDBD-export.png)

model is here https://github.com/taixingbi/sensors-monitor/blob/main/backend-django/database/models.py


#### emulated heartbeats
for serialNumbers= [1, 2] , generate heartbeats every 5 second

script is here https://github.com/taixingbi/sensors-monitor/blob/main/backend-django/generateHeart.py

#### alert 
if a sensor hasn’t sent a heartbeat in the last 10 minutes, will sent email to admin.     
email sent is here https://github.com/taixingbi/sensors-monitor/blob/main/backend-django/aws/ses.py



