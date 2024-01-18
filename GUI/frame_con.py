from frame import MainWindow
import sys
import os
from PyQt5.QtWidgets import QApplication, QTreeWidgetItem

#Initial
app = QApplication(sys.argv)
flowApp = MainWindow()

#Parameters
link_lib = "G:\\My Drive\\Target_in_2024\\Project\\flow_app\\Lib"


#Support class


#Support function
def load_tree():
    #load the folder list
    folder_list = [folder for folder in os.listdir(link_lib) if os.path.isdir(os.path.join(link_lib, folder))]

    #add the folder name as the tree element
    for folder in folder_list:
        top = QTreeWidgetItem(flowApp.lib_list)
        top.setText(0, folder)
        #load the library list by read the descriptor file
        libs = open(link_lib+"\\"+folder+"\\descriptor.txt",'r')
        item_list = [line.strip() for line in libs]
        #add the element of the list as the subelement of the tree
        for subItem in item_list:
            subItemWidget = QTreeWidgetItem(top)
            subItemWidget.setText(0, subItem)

#Exe
load_tree()

if __name__ == '__main__':
    
    flowApp.show()
    sys.exit(app.exec_())