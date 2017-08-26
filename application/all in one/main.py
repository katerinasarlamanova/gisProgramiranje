#!/usr/bin/python
# -'''- coding: utf-8 -'''-

"""
/***************************************************************************
 Frames from video
 This is an application for extracting frames from video.
                              -------------------
        begin                : 2017-04-01
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Katerina Sharlamanova
        email                : kate_sarlamanova@hotmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   With this application can be extracted frames from video. It can be   *
 *   one frame in a current time, all frames that video contains or frames *
 *   from every second.                                                    *
 *                                                                         *
 ***************************************************************************/
"""

import sys
from GUI import *
import cv2
import Tkinter, tkFileDialog
import os
import math

class Frames(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.video)
        self.pushButton_3.clicked.connect(self.directory)
        self.pushButton_2.clicked.connect(self.odredjeno)
        self.pushButton_5.clicked.connect(self.svaka)
        self.pushButton_8.clicked.connect(self.sve)

    def video(self):     # loading video file
        root = Tkinter.Tk()
        root.withdraw()  # use to hide tkinter window

        self.file = tkFileDialog.askopenfile(parent=root, mode='rb', title='Choose a file')
        if self.file != None:
            data = self.file.read()
            print "You chose %s" % self.file.name
            print "I got %d bytes from this file." % len(data)
            print ""

        self.textEdit.setText(str(self.file.name))


    def directory(self):       # choose directory
        root = Tkinter.Tk()
        root.withdraw()  # use to hide tkinter window

        currdir = os.getcwd()
        self.tempdir = tkFileDialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
        if len(self.tempdir) > 0:
            print "You chose %s" % self.tempdir
            print ""

        self.textEdit_5.setText(str(self.tempdir))


    def odredjeno(self):                  # frame at a current time
        videoFile = self.file             # self.file is defined in function video()
        imagesFolder = self.tempdir       # self.tempdir is defined in function directory()

        x = float(self.textEdit_4.toPlainText())
        y = x * 1000

        vidcap = cv2.VideoCapture(str(videoFile.name))
        vidcap.set(cv2.CAP_PROP_POS_MSEC, y)  # just cue to x sec. position

        success, image = vidcap.read()

        if success:
            print 'Read a new frame: ', success
            cv2.imwrite(imagesFolder + "/image_%d.jpg" % x, image)

        vidcap.release()
        print ""
        print "Done!"


    def svaka(self):                          # frames at every second
        videoFile = self.file                 # self.file is defined in function video()
        imagesFolder = self.tempdir           # self.tempdir is defined in function directory()

        vidcap = cv2.VideoCapture(str(videoFile.name))

        frameRate = vidcap.get(5)  # frame rate

        while (vidcap.isOpened()):
            frameId = vidcap.get(1)  # current frame number
            success, image = vidcap.read()
            if (success != True):
                break
            if (frameId % math.floor(frameRate) == 0):
                filename = imagesFolder + "/image_" + str(int(frameId)) + ".jpg"
                print 'Read a new frame: ', success
                cv2.imwrite(filename, image)

        vidcap.release()
        print ""
        print "Done!"


    def sve(self):                      # all frames
        videoFile = self.file           # self.file is defined in function video()
        imagesFolder = self.tempdir     # self.tempdir is defined in function directory()

        vidcap = cv2.VideoCapture(str(videoFile.name))

        count = 0
        success = True

        while success:
            success, image = vidcap.read()
            print 'Read a new frame: ', success
            cv2.imwrite(imagesFolder + "/image_%d.jpg" % count, image)  # save frame as JPEG file
            count += 1

        vidcap.release()
        print ""
        print "Done!"


def main():
    app = QtGui.QApplication(sys.argv)
    form = Frames()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()