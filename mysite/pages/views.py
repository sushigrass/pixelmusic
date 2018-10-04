# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import random
from PIL import Image
from midiutil.MidiFile import MIDIFile
from django.views.generic import View
from django.shortcuts import render
import time as t

class FrontEndRenderView(View):
    @csrf_exempt
    def get(self, request, *args, **kwargs):
        return render(request, "index.html",{})

@csrf_exempt
def index(request):
    print "IN HERE"
    if request.method == "POST":
        img = request.FILES['fileToUpload']
        pix = get_image_data(img)
        img_string = str(t.time())[:10]+".mid"
        pixels_to_midi(pix,img_string)
        return HttpResponse(img_string)

def get_image_data(img):
    im = Image.open(img)
    pix = list(im.getdata())
    return pix

def rgb_to_midi(rgb):
    return 21 + (rgb%87)

def pixels_to_midi(pix,img_string):
    mf = MIDIFile(1)
    track = 0
    time = 0
    channel = 0
    volume = 100
    mf.addTrackName(track,time,"Sample")
    mf.addTempo(track,time,1000)
    for i in pix:
        p2 = rgb_to_midi(i[1])
        p3 = rgb_to_midi(i[2])
        duration = 1
        if time % 4 == 0:
            mf.addNote(track, channel, p2, time, 4, volume)
            mf.addNote(track, channel, p3, time, 4, volume)
        else:
            mf.addNote(track, channel, p3, time, duration, volume)
        time += 1
    with open(img_string, 'wb') as outf:
        mf.writeFile(outf)
