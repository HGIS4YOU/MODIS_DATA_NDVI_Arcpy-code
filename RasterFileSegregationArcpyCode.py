import arcpy,os
from arcpy.sa import *
arcpy.env.workspace="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\TEST\\NDVI"
Result="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\TEST\\NDVI"
rasterlist = arcpy.ListRasters("*","TIF")
for raster in rasterlist:
	newSubFolder=raster[6:9]
	filename=Result+"\\"+newSubFolder+"\\"+raster
	path=Result+"\\"+newSubFolder
	if os.path.exists(path):
		print("Folder exists"+newSubFolder)
		arcpy.Copy_management(raster, filename)
	else:
		arcpy.CreateFolder_management(Result,newSubFolder)
		print("folder made"+newSubFolder)
		arcpy.Copy_management(raster, filename)

