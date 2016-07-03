# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import time, socket, json

from main import Ui_MainWindow

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
PORT = 8000
IP = "192.168.1.10"

locatoin1_lat = "33.548057"
locatoin1_lon = "73.132359"
angle1 = 306

locatoin2_lat = "33.546603"
locatoin2_lon = "73.133479"
angle2 = 316

locatoin3_lat = "33.546603"
locatoin3_lon = "73.133479"
angle3 = 180

class main_menu(QtGui.QMainWindow):

    def __init__(self):
        super(main_menu, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        
        self.ui.location1.clicked.connect(self.send_location1)
        self.ui.location2.clicked.connect(self.send_location2)
        
        self.ui.location3.clicked.connect(self.send_location3)

        self.ui.Start.clicked.connect(self.start)
        self.ui.Stop.clicked.connect(self.stop)
        
    def start(self):
        go = {"action":"start"}
        json_data=json.dumps(go)
        s.sendto((json_data), (IP, PORT))
        print "action sent ", go

    def stop(self):
        go = {"action":"stop"}
        json_data=json.dumps(go)
        s.sendto((json_data), (IP, PORT))
        print "action sent ", go
        
    def send_location1(self):
        location = {"lat":locatoin1_lat, "lon":locatoin1_lon, "angle" : angle1}
        json_data=json.dumps(location)
        s.sendto((json_data), (IP, PORT))
        print "location 1 sent"

    def send_location2(self):
        location = {"lat":locatoin2_lat, "lon":locatoin2_lon, "angle" : angle2}
        json_data=json.dumps(location)
        s.sendto((json_data), (IP, PORT))         
        print "location 2 sent" 
        
    def send_location3(self):
        location = {"lat":locatoin3_lat, "lon":locatoin3_lon, "angle" : angle3}
        json_data=json.dumps(location)
        s.sendto((json_data), (IP, PORT))         
        print "location 3 sent"         
        
    def keyPressEvent(self, event1):
      verbose = {"FB":"", "LR":""}
      if event1.key() == QtCore.Qt.Key_W: 
        #print "Up pressed"
        verbose["FB"] = "F"
      if event1.key() == QtCore.Qt.Key_S:
        #print "D pressed"
        verbose["FB"] = "B"
      
      if event1.key() == QtCore.Qt.Key_A:
        #print "L pressed"
        verbose["LR"] = "L"
      if event1.key() == QtCore.Qt.Key_D:
        #print "R pressed"
        verbose["LR"] = "R"
        
      print verbose
      json_data=json.dumps(verbose)
      s.sendto((json_data), (IP, PORT))
      
    def keyReleaseEvent(self, event):
      verbose = {"FB":"", "LR":""}
      if event.key() == QtCore.Qt.Key_W: 
        #print "Up rel"
        verbose["FB"] = "S"
      if event.key() == QtCore.Qt.Key_S: 
        #print "D rel"
        verbose["FB"] = "S"
      
      if event.key() == QtCore.Qt.Key_A:
        #print "L pressed"
        verbose["LR"] = "S"
      if event.key() == QtCore.Qt.Key_D: 
        #print "R pressed"
        verbose["LR"] = "S"
        
      print verbose
      json_data=json.dumps(verbose)
      s.sendto((json_data), (IP, PORT))      
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = main_menu()
    app.exec_()
    
    
    

if __name__ == '__main__':      
    main()


    

    