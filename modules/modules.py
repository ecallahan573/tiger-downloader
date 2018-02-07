# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 08:52:25 2015

@author: ecallahan
"""
from ftplib import FTP
import os, zipfile

class download():
    
    def __init__(self, year):
        self.cnxn = FTP('ftp.census.gov', 'anonymous')
        self.froot = '/geo/tiger/TIGER%s/'%year
        self.cnxn.cwd(self.froot)
        
    def cdir(self, directory):
        self.cnxn.cwd(self.froot)
        self.directory = directory
        self.cnxn.cwd(directory)
        
    def dload(self, path, dfile):
        folder = os.path.join(path,'data','download')
        local_filename = os.path.join(folder, dfile)
        save = open(local_filename, 'wb')
        self.cnxn.retrbinary('RETR ' + dfile, save.write)
        save.close()
        
class process():
    
    def __init__(self, directory, database_name):
        
        self.directory = directory
        self.database_name = database_name
        #arcpy.env.workspace = self.directory
        
    def unzip(self):
        path = os.path.join(self.directory, 'data', 'download')
        zfiles = os.listdir(path)
        for zfile in zfiles:
            fh = open(os.path.join(path, zfile), 'rb')
            z = zipfile.ZipFile(fh)
            z.extractall(path)
            
    
    def createdb(self,dbtype, statename, countyname):
        import arcpy
        dbase_name = self.database_name
        print statename, countyname
        
        try:
            if dbtype == 'File Geodatabase':
                arcpy.CreateFileGDB_management(self.directory,str(self.database_name))
            elif dbtype == 'Personal Geodatabase':
                print dbase_name
                print self.directory
                arcpy.CreatePersonalGDB_management(self.directory,str(self.database_name))
        except:
            print "database exists?"
        
        def import_shapes():
            path = os.path.join(self.directory, 'data', 'download')
            arcpy.env.workspace = path
            fc = arcpy.ListFeatureClasses()
    
            for feature in fc:
                if dbtype == 'Personal Geodatabase':
                    ext = '.mdb'
                else:
                    ext = '.gdb'
                    
                shapefile = os.path.join(path,feature)
                try:
                    arcpy.FeatureClassToFeatureClass_conversion(shapefile, os.path.join(self.directory,str(self.database_name) + ext), statename.replace(" ", "_") + '_' + countyname.replace(" ", "_") + '_' + feature[feature.rfind('_')+1:-4])
                except:
                    print "feature exists?"
                    
        import_shapes()

            
