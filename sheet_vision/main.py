# all the imports used throughout the main file
from GUI import GUI
import GUI
import sys
<<<<<<< HEAD
=======
import subprocess
import cv2
import time
import numpy as np
from best_fit import fit
from rectangle import Rectangle
from note import Note   
from random import randint
from MidiFile3 import MIDIFile

sheet_music = [
        "playableMusic/fire.jpg",
        "playableMusic/lost.jpg",
        "playableMusic/zelda.jpg",
        "playableMusic/pirates.jpg",
        "playableMusic/delune.jpg",
    ]
IMAGE = sheet_music[4]

# getting the files form the musicImages folder and turning them into list sorted by the type of music image they represent
staff_files = [
    "musicImages/staff2.png", 
    "musicImages/staff.png"]
quarter_files = [
    "musicImages/quarter.png", 
    "musicImages/solid-note.png"]
sharp_files = [
    "musicImages/sharp.png"]
flat_files = [
    "musicImages/flat-line.png", 
    "musicImages/flat-space.png" ]
half_files = [
    "musicImages/half-space.png", 
    "musicImages/half-note-line.png",
    "musicImages/half-line.png", 
    "musicImages/half-note-space.png"]
whole_files = [
    "musicImages/whole-space.png", 
    "musicImages/whole-note-line.png",
    "musicImages/whole-line.png", 
    "musicImages/whole-note-space.png"]

staff_imgs = [cv2.imread(staff_file, 0) for staff_file in staff_files]
quarter_imgs = [cv2.imread(quarter_file, 0) for quarter_file in quarter_files]
sharp_imgs = [cv2.imread(sharp_files, 0) for sharp_files in sharp_files]
flat_imgs = [cv2.imread(flat_file, 0) for flat_file in flat_files]
half_imgs = [cv2.imread(half_file, 0) for half_file in half_files]
whole_imgs = [cv2.imread(whole_file, 0) for whole_file in whole_files]

staff_lower, staff_upper, staff_thresh = 50, 150, 0.77
sharp_lower, sharp_upper, sharp_thresh = 50, 150, 0.70
flat_lower, flat_upper, flat_thresh = 50, 150, 0.77
quarter_lower, quarter_upper, quarter_thresh = 50, 150, 0.70
half_lower, half_upper, half_thresh = 50, 150, 0.70
whole_lower, whole_upper, whole_thresh = 50, 150, 0.70

>>>>>>> 5cfe37597f484e0c37c49586bd660954495dfc54
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = GUI.GUI(app, MainWindow)
ui.setUp()
MainWindow.show()
sys.exit(app.exec_())

if __name__ == "__main__":
    #creating a list to hold all the playable sheetmusic
    img_file =  IMAGE
    img = cv2.imread(img_file, 0)
    img_gray = img
    img = cv2.cvtColor(img_gray,cv2.COLOR_GRAY2RGB)
    ret,img_gray = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
    img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
    img_width, img_height = img_gray.shape[::-1]

    print("Matching staff image...")
    staff_recs = locate_images(img_gray, staff_imgs, staff_lower, staff_upper, staff_thresh)

    print("Filtering weak staff matches...")
    staff_recs = [j for i in staff_recs for j in i]
    heights = [r.y for r in staff_recs] + [0]
    histo = [heights.count(i) for i in range(0, max(heights) + 1)]
    avg = np.mean(list(set(histo)))
    staff_recs = [r for r in staff_recs if histo[r.y] > avg]

    print("Merging staff image results...")
    staff_recs = merge_recs(staff_recs, 0.01)
    staff_recs_img = img.copy()
    for r in staff_recs:
        r.draw(staff_recs_img, (0, 0, 255), 2)
    cv2.imwrite('staff_recs_img.png', staff_recs_img)
    open_file('staff_recs_img.png')

    print("Discovering staff locations...")
    staff_boxes = merge_recs([Rectangle(0, r.y, img_width, r.h) for r in staff_recs], 0.01)
    staff_boxes_img = img.copy()
    for r in staff_boxes:
        r.draw(staff_boxes_img, (0, 0, 255), 2)
    cv2.imwrite('staff_boxes_img.png', staff_boxes_img)
    open_file('staff_boxes_img.png')
    
    print("Matching sharp image...")
    sharp_recs = locate_images(img_gray, sharp_imgs, sharp_lower, sharp_upper, sharp_thresh)

    print("Merging sharp image results...")
    sharp_recs = merge_recs([j for i in sharp_recs for j in i], 0.5)
    sharp_recs_img = img.copy()
    for r in sharp_recs:
        r.draw(sharp_recs_img, (0, 0, 255), 2)
    cv2.imwrite('sharp_recs_img.png', sharp_recs_img)
    open_file('sharp_recs_img.png')

    print("Matching flat image...")
    flat_recs = locate_images(img_gray, flat_imgs, flat_lower, flat_upper, flat_thresh)

    print("Merging flat image results...")
    flat_recs = merge_recs([j for i in flat_recs for j in i], 0.5)
    flat_recs_img = img.copy()
    for r in flat_recs:
        r.draw(flat_recs_img, (0, 0, 255), 2)
    cv2.imwrite('flat_recs_img.png', flat_recs_img)
    open_file('flat_recs_img.png')

    print("Matching quarter image...")
    quarter_recs = locate_images(img_gray, quarter_imgs, quarter_lower, quarter_upper, quarter_thresh)

    print("Merging quarter image results...")
    quarter_recs = merge_recs([j for i in quarter_recs for j in i], 0.5)
    quarter_recs_img = img.copy()
    for r in quarter_recs:
        r.draw(quarter_recs_img, (0, 0, 255), 2)
    cv2.imwrite('quarter_recs_img.png', quarter_recs_img)
    open_file('quarter_recs_img.png')

    print("Matching half image...")
    half_recs = locate_images(img_gray, half_imgs, half_lower, half_upper, half_thresh)

    print("Merging half image results...")
    half_recs = merge_recs([j for i in half_recs for j in i], 0.5)
    half_recs_img = img.copy()
    for r in half_recs:
        r.draw(half_recs_img, (0, 0, 255), 2)
    cv2.imwrite('half_recs_img.png', half_recs_img)
    open_file('half_recs_img.png')

    print("Matching whole image...")
    whole_recs = locate_images(img_gray, whole_imgs, whole_lower, whole_upper, whole_thresh)

    print("Merging whole image results...")
    whole_recs = merge_recs([j for i in whole_recs for j in i], 0.5)
    whole_recs_img = img.copy()
    for r in whole_recs:
        r.draw(whole_recs_img, (0, 0, 255), 2)
    cv2.imwrite('whole_recs_img.png', whole_recs_img)
    open_file('whole_recs_img.png')

    note_groups = []
    for box in staff_boxes:
        staff_sharps = [Note(r, "sharp", box) 
            for r in sharp_recs if abs(r.middle[1] - box.middle[1]) < box.h*5.0/8.0]
        staff_flats = [Note(r, "flat", box) 
            for r in flat_recs if abs(r.middle[1] - box.middle[1]) < box.h*5.0/8.0]
        quarter_notes = [Note(r, "4,8", box, staff_sharps, staff_flats) 
            for r in quarter_recs if abs(r.middle[1] - box.middle[1]) < box.h*5.0/8.0]
        half_notes = [Note(r, "2", box, staff_sharps, staff_flats) 
            for r in half_recs if abs(r.middle[1] - box.middle[1]) < box.h*5.0/8.0]
        whole_notes = [Note(r, "1", box, staff_sharps, staff_flats) 
            for r in whole_recs if abs(r.middle[1] - box.middle[1]) < box.h*5.0/8.0]
        staff_notes = quarter_notes + half_notes + whole_notes
        staff_notes.sort(key=lambda n: n.rec.x)
        staffs = [r for r in staff_recs if r.overlap(box) > 0]
        staffs.sort(key=lambda r: r.x)
        note_color = (randint(0, 255), randint(0, 255), randint(0, 255))
        note_group = []
        i = 0; j = 0;
        while(i < len(staff_notes)):
            if (staff_notes[i].rec.x > staffs[j].x and j < len(staffs)):
                r = staffs[j]
                j += 1;
                if len(note_group) > 0:
                    note_groups.append(note_group)
                    note_group = []
                note_color = (randint(0, 255), randint(0, 255), randint(0, 255))
            else:
                note_group.append(staff_notes[i])
                staff_notes[i].rec.draw(img, note_color, 2)
                i += 1
        note_groups.append(note_group)

    for r in staff_boxes:
        r.draw(img, (0, 0, 255), 2)
    for r in sharp_recs:
        r.draw(img, (0, 0, 255), 2)
    flat_recs_img = img.copy()
    for r in flat_recs:
        r.draw(img, (0, 0, 255), 2)
        
    cv2.imwrite('res.png', img)
    open_file('res.png')
   
    for note_group in note_groups:
        print([ note.note + " " + note.sym for note in note_group])

    midi = MIDIFile(1)
     
    track = 0   
    time = 0
    channel = 0
    volume = 100
    
    midi.addTrackName(track, time, "Track")
    midi.addTempo(track, time, 140)
    
    for note_group in note_groups:
        duration = None
        for note in note_group:
            note_type = note.sym
            if note_type == "1":
                duration = 4
            elif note_type == "2":
                duration = 2
            elif note_type == "4,8":
                duration = 1 if len(note_group) == 1 else 0.5
            pitch = note.pitch
            midi.addNote(track,channel,pitch,time,duration,volume)
            time += duration

    midi.addNote(track,channel,pitch,time,4,0)
    # And write it to disk.
    binfile = open("output.mid", 'wb')
    midi.writeFile(binfile)
    binfile.close()
    open_file('output.mid')
