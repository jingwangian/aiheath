from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
import sys
from robot import ChatRobot

chatrobot = ChatRobot('Medius')


def index(request):
    context = {}

    chatrobot.reset()

    return render(request, 'medius/chat.html', context)


def handle_first_message(request):
    res_message = dict()
    res_message['message'] = chatrobot.get_first_question()
    return JsonResponse(res_message)


def handle_message(request, message):
    # print("Input message: ", message)
    res_message = dict()
    if chatrobot.chat_finished:
        res_message['message'] = "Chat has finished. Please refresh page to start again!"
    else:
        msg = chatrobot.get_response(message)
        if msg is None:
            res_message['message'] = "Thank you. Following is your result information:<br>{}".format(chatrobot.get_final_answer())
        else:
            res_message['message'] = msg

    return JsonResponse(res_message)
