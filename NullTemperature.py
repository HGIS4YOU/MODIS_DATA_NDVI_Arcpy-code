import arcpy
import * form arcpy.sa
TestFolder="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\TEST\\NDVI"
arcpy.env.workspace="D:\\Shivaprakash\\TEST\\modis_uttrakanda\\TEST\\NDVI"
FolderList=os.listdir(TestFolder)
for folder in FolderList:

	folder_addNull= folder+"_addNull"
	arcpy.CreateFolder_management(TestFolder,folder_addNull)
	acrpy.env.workspace="E:\\Shivaprakash\\TEST\\NDVI_INDIA\\TEST\\NDVI\\"+folder
	rasterlist_tiff_null=arpy.ListRasters("*","TIF")
	whereClause="VALUE=0"
	for raster in rasterlist_tiff_null:
		outRasterNull=TestFolder+"\\"+folder_addNull+"\\"+raster
		OutNull=SetNull(raster,raster,whereClause)
		OutNull.save(outRasterNull)
