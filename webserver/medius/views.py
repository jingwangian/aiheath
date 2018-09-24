from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
import sys
from robot import ChatRobot

chatrobot = ChatRobot('Medius')


def index(request):
    context = {}

    return render(request, 'medius/chat.html', context)
    # return HttpResponse("This is index page")

# btc/message/xxxx


def handle_first_message(request):
    res_message = dict()
    res_message['message'] = chatrobot.get_first_question()
    return JsonResponse(res_message)


def handle_message(request, message):
    print("Input message: ", message)
    res_message = dict()
    msg = chatrobot.get_response(message)
    if msg is None:
        res_message['message'] = "Thank you. Following is your result:<br>{}".format(chatrobot.get_final_answer())
    else:
        res_message['message'] = msg

    return JsonResponse(res_message)
