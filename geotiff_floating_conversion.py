import arcpy
from arcpy.sa import *
TestFolder="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\TEST"
folder_name="2004"+"out_clip"
arcpy.CreateFolder_management(TestFolder,folder_name)
arcpy.env.workspace="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\TEST\\out_clip"
rasterlist_tiff=arcpy.ListRasters("*","TIF")
for raster in rasterlist_tiff:
	outRaster=TestFolder+"\\"+folder_name+"\\"+raster
	Out=Raster(raster)*0.0001
	Out.save(outRaster)