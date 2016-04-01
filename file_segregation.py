#!/usr/bin/python
import glob,os,logging,shutil
import datetime
mydir="/home/shivaprakash/Videos/"
data_folder="test"
LOG_FILENAME = '2001.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

#getting list of folders in the main folder
folderlist= os.listdir(mydir+data_folder)
#logging
logging.debug('Listed all the files')
print(folderlist)
for folder in folderlist:
    subdir=mydir+data_folder+"/"+folder
    print(subdir,folder)
    logging.debug(subdir,folder)
    os.chdir(subdir)
    file_hdf=glob.glob('*.hdf')
    hdf=file_hdf[0].split('.')
    hdfTiles=hdf[2]
    file_tiff=glob.glob('*.tif')
    for file in file_tiff:
        print(file)
        logging.debug(file)
        name_list=file.split('.')
        name=name_list[2]
        dayName=name[5:]
        newsubdir=mydir+dayName
        if os.path.exists(newsubdir):
            print("Exists")
            logging.debug("Directory Exist")
            shutil.copy(subdir+'/'+file,newsubdir)
            
            os.rename(newsubdir+'/'+file,newsubdir+'/'+name+'_'+hdfTiles+'.tif')
        else:
            print("Dont Exist")
            logging.debug("Directory doesnt Exist")
            os.makedirs(newsubdir)
            shutil.copy(subdir+'/'+file,newsubdir)
            os.rename(newsubdir+'/'+file,newsubdir+'/'+name+'_'+hdfTiles+'.tif')
        
