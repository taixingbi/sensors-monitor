
```
python3 -m venv my_env
source my_env/bin/activate
pip install -r requirements.txt
```

### run migrate
##### packaging up your model changes
```
python manage.py makemigrations 
```
##### applying those to your database.
```
python manage.py migrate 
Username: test
Password: test
```

### run local
```
python manage.py runserver 0.0.0.0:8083
python manage.py createsuperuser
```


### task
```
Your task is to accomplish the following:

Use Django (or some similar Python web framework) to build a web application
Scaffold a database that includes sensors and heartbeats
A sensor is a device in the field. It generally includes a serial number and other metadata
A heartbeat is a periodic message used to tell the backend that the sensor is online and provide the current state of the sensor
It is left as an exercise to the candidate to define exactly what data is stored (as well as how it is stored) for a sensor and a heartbeat
Expose an endpoint that can receive "heartbeats" indicating that the sensor is alive and checking in
Deliver a webpage where a user can view live, updating heartbeats from the sensors
Deliver a script that can emulate one or many sensors by sending emulated heartbeats to the "heartbeats" endpoint.
Bonus Points: Build or tell us how you would include a way to alert users if a sensor hasn’t sent a heartbeat in the last 10 minutes.

```