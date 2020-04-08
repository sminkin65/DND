from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''
Requests are handled by this function.
Each request should provide a direction property {right, left} which
tells the robot which direction to move in
'''
def index(request):
    init()
    return HttpResponse("Hello World!")

'''
Sets up the pins on the raspberry pi and sets them initial values
'''
def init():
    # initialize the raspberry pi settings
    print('init')

'''
Moves the robot to the left for a specified time
@param      {tf}    The time to move
'''
def left(tf):
    print('moving left')

'''
Moves the robot to the right for a specified time
@param      {tf}    The time to move
'''
def right(tf):
    print('moving right')


