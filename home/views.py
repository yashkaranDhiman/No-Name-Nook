import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404,render
from django.utils.timezone import now
from django.utils.timesince import timesince
from .models import Room, message

def index(request):
    allRooms = Room.objects.all()
    if(request.method == "POST"):
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        new_room = Room(title=title,description=desc)
        new_room.save()
    context = {
        "allRooms": allRooms
    }
    return render(request, "home/index.html", context)

def enter_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    the_message = room.message_set.all()
    context = {
        "the_room": room,
        "all_messages": the_message
    }
    return render(request, "home/room_detail.html", context)

def addMessage(request, room_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_chat = data.get('msg')
        room = get_object_or_404(Room, pk=room_id)
        new_chat_message = message.objects.create(content=new_chat, room=room)
        time_since = timesince(new_chat_message.time, now())
        json_res = {
            "content": new_chat_message.content,
            "time": time_since
        }
        return JsonResponse(json_res)
    else:
        return JsonResponse({"error": "cannot get the thing"}, status=400)
