import arcpy,shutil,os
from arcpy.sa import *
Result="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\TEST\\2015"
TestFolder="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\TEST"
arcpy.env.workspace="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\TEST\\2015"
rasterlist = arcpy.ListRasters("*","HDF")
projection = arcpy.SpatialReference(4326)

#spliting of name MOD13A1.A2001001.h24v05.005.2008270033303.hdf
for raster in rasterlist:
	name=raster.split('.')
	name1=name[1]
	name2=name[2]
	newName="n"+str(name1[3:])+str(name2[1:3])+str(name2[4:])
	newSubFolder=str(name1[5:])
	filename=Result+"\\"+newSubFolder+"\\"+newName
	path=Result+"\\"+newSubFolder
	if os.path.exists(path):
		print("Folder exists"+newSubFolder)
	
		arcpy.ExtractSubDataset_management(raster, filename+".tif", "0")
		
		arcpy.ProjectRaster_management(filename+".tif", filename+"p"+".tif",projection,"","","","","")
		arcpy.Delete_management(filename+".tif")
	else:
		arcpy.CreateFolder_management(Result,newSubFolder)
		print("folder made"+newSubFolder)
		arcpy.ExtractSubDataset_management(raster, filename+".tif", "0")
		arcpy.ProjectRaster_management(filename+".tif", filename+"p"+".tif",projection,"","","","","")
		arcpy.Delete_management(filename+".tif")

arcpy.env.workspace="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\TEST\\2015"
rasterlist = arcpy.ListRasters("*","HDF")
for raster in rasterlist:
	delete_hdf=Result+"\\"+raster
	os.remove(delete_hdf)	
	
arcpy.CreateFolder_management(TestFolder,"out_mosaic")	
folderlist=os.listdir(Result)

for folder in folderlist:
	print(folder)
	subdir=Result+"\\"+folder
	print(subdir)
	
	arcpy.env.workspace=subdir
	rasterlist_tiff=arcpy.ListRasters("*","TIF")
	mosaicName=rasterlist_tiff[0]
	arcpy.MosaicToNewRaster_management(rasterlist_tiff,TestFolder+"\\"+"out_mosaic",mosaicName[:6]+"mos.tif", projection,"16_BIT_SIGNED", "", "1", "","")

arcpy.CreateFolder_management(TestFolder,"out_clip")
clip_folder=TestFolder+"\\"+"out_clip"
arcpy.env.workspace=TestFolder+"\\"+"out_mosaic"
uttarkhandShape="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\shapefiles\\uttarakhand.shp"
rasterlist_tiff_clip=arcpy.ListRasters("*","TIF")
for raster in rasterlist_tiff_clip:
	print("clipping"+" "+raster)
	outName="NDVI"+raster[1:6]+".tif"
	arcpy.Clip_management(raster, "#", clip_folder+"\\"+outName,uttarkhandShape, "", "ClippingGeometry", "")