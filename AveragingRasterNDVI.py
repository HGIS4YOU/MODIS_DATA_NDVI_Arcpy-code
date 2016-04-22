import arcpy
from arcpy.sa import *
TestFolder="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\TEST\\NDVI\\001"
arcpy.env.workspace="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\TEST\\NDVI\\001"
raster_list=arcpy.ListRasters("*","TIF")
TotalRaster=0
FileName="TotalRaster001.tif"
TotalRasterOut=TestFolder+"\\"+FileName
for raster in raster_list:
	TotalRaster=TotalRaster+Raster(raster)
TotalRaster.save(TotalRasterOut)

TotalRasterIn=TestFolder+"\\"+FileName	
AverageRaster=0
AverageRaster=Raster(TotalRasterIn)/15.0
AvgRasterOut=TestFolder+"\\"+"AvgRaster001.tif"
AverageRaster.save(AvgRasterOut)