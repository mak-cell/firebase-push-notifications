from django.http.request import HttpHeaders
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
import json
from django.http import JsonResponse

def send_notification(registration_ids , message_title , message_desc):
    fcm_api = "AAAAglgW_L0:APA91bGkK_9DRljN1F6dgsQuzE4ZAljfZPLTc1KiCLcEkZGI4Y0VGd8fpAR3fZXfyO7xCymyov5vjti7uDBpTuiFC7KeYUgaqXPbCw2UKO-jOyd9jqBe7hrpfgSOc_hKpVCW9XksCH7a"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}

    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            "image" : "https://i.ytimg.com/vi/m5WUPHRgdOA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDwz-yjKEdwxvKjwMANGk5BedCOXQ",
            "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result.json())





def index(request):
    return render(request , 'index.html')

def send(request):
    resgistration  = ['dmtsFW1_v3Bcs5jc6kH70A:APA91bFuFc0V2VQ-2qWSlxhUzzxnzp1_1JE9qzheEQJjril9AYbQgY8tNJT6Xb1ykoB3YZ2zKCvOZvKc9ADkVVpByZydo2t6-FhOIdsqylM5vptPQO5Eaq4YCQrffauSjiTIt9Hk_LIH']
    send_notification(resgistration , 'Code Keen added a new video' , 'Code Keen new video alert')
    return HttpResponse("sent")

@csrf_exempt
def send_device_id(request):
    if request.method == 'POST':
        token = validate_data(request, "token")
        print(token)
        return respond(status_code=200, message="Device id recieved from server")
    return respond(status_code=400, message="Bad token")

def validate_data(request, key):
    """
    This common helper function used to extract and return required field as per request type
    """
    if request.method == "GET":
        return request.GET.get(key, "")
    if request.method == "POST":
        return request.POST.get(key, "")
def respond(status_code, message, **kwargs):
    """
    This helper function used to provide json response as per success and failure status code
    """
    if status_code == 200:
        return JsonResponse({"success": True, "msg": message, **kwargs}, status=200)
    else:
        return JsonResponse({"success": False, "error": message}, status=status_code)


def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyBJeuQ3ZAjQlE77daP92qNVKgdt0EhQXmM",' \
         '        authDomain: "bazarside-mak.firebaseapp.com",' \
         '        databaseURL: "",' \
         '        projectId: "bazarside-mak",' \
         '        storageBucket: "bazarside-mak.appspot.com",' \
         '        messagingSenderId: "559823649981",' \
         '        appId: "1:559823649981:web:258ed7771ca85a3bdb4bd4",' \
         '        measurementId: "G-L7M9P9L1VS"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")
