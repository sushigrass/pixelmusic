import numpy as np
import random
from PIL import Image
from midiutil.MidiFile import MIDIFile

def create_image():
    pixels = []
    size = 10
    for i in range(size):
        x = []
        for q in range(size):
            r1 = random.randint(0,255)
            r2 = random.randint(0,255)
            r3 = random.randint(0,255)
            x.append((r1,r2,r3))
        pixels.append(x)
    array = np.array(pixels,dtype=np.uint8)
    new = Image.fromarray(array)
    new.save('new.png')

def rgb_to_midi(rgb):
    return 21 + (rgb%87)

def pixels_to_midi():
    pix = get_image_data("stripes.jpg")
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
    print "done"
    with open("stripes.mid", 'wb') as outf:
        mf.writeFile(outf)

def pixels_to_midi2():
    pix = get_image_data("small.jpg")
    mf = MIDIFile(1)
    track = 0
    time = 0
    channel = 0
    volume = 100
    mf.addTrackName(track,time,"Sample")
    mf.addTempo(track,time,1000)
    for i in xrange(len(pix)):
        if i >= len(pix)-4:
            break
        p1 = rgb_to_midi(pix[i])
        p2 = rgb_to_midi(pix[i+1])
        p3 = rgb_to_midi(pix[i+2])
        duration = 1
        if time % 4 == 0:
            mf.addNote(track, channel, p1, time, 4, 120)
            mf.addNote(track, channel, p2, time, 4, 120)
            mf.addNote(track, channel, p3, time, 4, 120)
        else:
            mf.addNote(track, channel, p1, time, duration, 50)
        time += 1
    with open("small.mid", 'wb') as outf:
        mf.writeFile(outf)

def get_image_data(img):
    im = Image.open(img)
    pix = list(im.getdata())
    return pix
