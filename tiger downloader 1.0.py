# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 13:27:15 2015

@author: ecallahan

version 0.2a - Added feature to rename database feature classes to match downloaded state/county.  
               Added label to provide feedback on what the script is doing.
version 0.3 -  Changed time of arcpy import for faster initial load. Improved error handling.
               Can now select multiple counties.
version 0.4 -  Corrected error where a space in the state or county name would cause feature classes to not be created.
version 1.0 -  Upgraded to PyQt5
version 1.1 - Fix inconsistent FTP downloads
"""

import sys, os, shutil, numpy as np
from PyQt5 import QtWidgets

root = os.getcwd()

sys.path.append(os.path.join(root, "modules"))
sys.path.append(os.path.join(root, "data"))

from dictionaries import states, counties
from modules import download, process
import tiger_downloader

class Tigerdownloader(QtWidgets.QMainWindow, tiger_downloader.Ui_tiger_downloader):
    def __init__(self,parent=None):
        super(Tigerdownloader, self).__init__(parent)
        self.setupUi(self)
        self.download_dir = os.path.join(root, "data", "download")
        self.folders = ['UNSD','BG','AREALM', 'AREAWATER','ELSD','LINEARWATER','PLACE','POINTLM','ROADS','SCSD','FEATNAMES']
        self.statebox.addItems(sorted(states.values()))
        self.statebutton.clicked.connect(self.list_counties)
        self.downloadbutton.clicked.connect(self.download_click)
        
    def list_counties(self):
        self.listWidget.clear()
        selected_state = str(self.statebox.currentText())
        
        for k, v in states.iteritems():
            if v == selected_state:
                self.statefp = k
                self.statename = v
        for k, v in counties.iteritems():
            if k == self.statefp:
                self.selected_counties = v
        
        for county in sorted(self.selected_counties):
            self.listWidget.addItem(county[1])

    def get(self, statefp, countyfp):

        self.d = download(self.year)

        if os.path.isdir(self.download_dir) == True:
            print("Deleting folders")
            shutil.rmtree(self.download_dir)
            os.mkdir(self.download_dir)
        else:
            os.mkdir(self.download_dir)
        
        for folder in self.folders:
            print folder
            
            try:
                self.d.cdir(folder)
            except:
                print "folder not found"
                
            files = self.d.cnxn.nlst()
            
            for file in files:
                self.feedback.setText('Downloading %s'%folder)
                QtWidgets.QApplication.processEvents()
                if file == 'tl_%s_%s%s_%s.zip'%(self.year,statefp,countyfp,folder.lower()):
                    self.d.dload(root, file)
                elif file == 'tl_%s_%s_%s.zip'%(self.year,statefp,folder.lower()):
                    self.d.dload(root, file)

    def etl(self):
        p = process(root, self.database)
        self.feedback.setText("Extracting Zips")
        QtWidgets.QApplication.processEvents()
        p.unzip()
        self.feedback.setText("Creating Database")
        QtWidgets.QApplication.processEvents()
        p.createdb(self.dbtype, self.statename, self.countyname)
        self.feedback.setText("Select State/County")
        self.d.cnxn.close()
        shutil.rmtree(self.download_dir)
    
    def download_click(self):
        self.database = self.database_name.text()
        self.dbtype = str(self.dbase_box.currentText())
        self.picked_counties = np.array(self.listWidget.selectedItems())
        
        if len(self.picked_counties) == 0:
            self.feedback.setText("No County Selected")
            QtWidgets.QApplication.processEvents()
        elif len(self.database) == 0:
            self.feedback.setText("No Database Name")
            QtWidgets.QApplication.processEvents()
        else:
            for county in self.picked_counties:
                self.selected_county = str(county.text())
                for items in self.selected_counties:
                    if items[1] == self.selected_county:
                        self.countyfp = items[0]
                        self.countyname = items[1]
                
                self.year = str(self.yearbox.currentText())
                
                self.feedback.setText("Connecting...")
                QtWidgets.QApplication.processEvents()
                print("Getting Data")
                self.get(self.statefp, self.countyfp)
                self.etl()
#                except:
#                    raise

            exit()
                
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Tigerdownloader()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
