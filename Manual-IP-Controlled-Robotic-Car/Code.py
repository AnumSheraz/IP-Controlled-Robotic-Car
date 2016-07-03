
import sys
from PyQt4 import QtGui, QtCore
import time, socket, json

from main import Ui_MainWindow

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

IP = "localhost"
PORT = 8001

class main_menu(QtGui.QMainWindow):

    def __init__(self):
        super(main_menu, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()         
        
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
