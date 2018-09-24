from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
import sys
from robot import ChatRobot

chatrobot = ChatRobot('Medius')


def index(request):
    question = chatrobot.get_first_question()
    context = {"question": question}

    return render(request, 'medius/chat.html', context)
    # return HttpResponse("This is index page")

# btc/message/xxxx

# def handle_first_message(re)


def handle_message(request, message):
    print("Input message: ", message)
    res_message = dict()
    res_message['message'] = chatrobot.get_response(message)

    return JsonResponse(res_message)
