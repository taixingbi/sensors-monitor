import requests
import time

serialNumbers= [1, 2]

circle= 5

def callApi(serialNumber, second):
    url= 'http://0.0.0.0:8090/api/heartUpdate/'
    data = {'serialNumber': serialNumber, "message": second}
    x = requests.post(url, json = data)

    print(x.text)

def getSeconds():
    Time= time.time()
    return int( Time ) % 10000

def timer():
    print("timer")
    seconds= 0
    while 1:
        now = getSeconds()
        if seconds == now:  continue
        seconds =now

        if seconds%5 == 0: 
            for serialNumber in serialNumbers:
                callApi(serialNumber, seconds)
                print( seconds )
 

if __name__ == '__main__':
    print("generate heart")

    # callApi(1, 300)
    timer()
