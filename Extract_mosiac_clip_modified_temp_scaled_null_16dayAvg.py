import arcpy,shutil,os
from arcpy.sa import *
TestFolder="E:\\Shivaprakash\\TEST\\NDVI_INDIA\\TEST"
arcpy.env.workspace="E:\\Shivaprakash\\TEST\\NDVI_INDIA\\TEST"
folderlist=os.listdir(TestFolder)
for folder in folderlist:

	Result="E:\\Shivaprakash\\TEST\\NDVI_INDIA\\TEST\\"+folder
	TestFolder="E:\\Shivaprakash\\TEST\\NDVI_INDIA\\TEST"
	arcpy.env.workspace="E:\\Shivaprakash\\TEST\\NDVI_INDIA\\TEST\\"+folder
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

	arcpy.env.workspace="E:\\Shivaprakash\\TEST\\NDVI_INDIA\\TEST\\"+folder
	rasterlist = arcpy.ListRasters("*","HDF")
	for raster in rasterlist:
		delete_hdf=Result+"\\"+raster
		os.remove(delete_hdf)	
	out_mosaic="out_mosaic"+folder	
	arcpy.CreateFolder_management(TestFolder,out_mosaic)	
	folderlist=os.listdir(Result)

	for folder1 in folderlist:
		print(folder1)
		subdir=Result+"\\"+folder1
		print(subdir)
		
		arcpy.env.workspace=subdir
		rasterlist_tiff=arcpy.ListRasters("*","TIF")
		mosaicName=rasterlist_tiff[0]
		arcpy.MosaicToNewRaster_management(rasterlist_tiff,TestFolder+"\\"+"out_mosaic"+folder,mosaicName[:6]+"mos.tif", projection,"16_BIT_UNSIGNED", "", "1", "","")
	
	out_clip="out_clip"+folder
	arcpy.CreateFolder_management(TestFolder,out_clip)
	clip_folder=TestFolder+"\\"+out_clip
	arcpy.env.workspace=TestFolder+"\\"+out_mosaic
	uttarkhandShape="E:\\Shivaprakash\\TEST\\NDVI_INDIA\\SHAPE_FILES\\INDIA\\INDIA.shp"
	rasterlist_tiff_clip=arcpy.ListRasters("*","TIF")
	for raster in rasterlist_tiff_clip:
		print("clipping"+" "+raster)
		outName="TEMP"+raster[1:6]+".tif"
		arcpy.Clip_management(raster, "#", clip_folder+"\\"+outName,uttarkhandShape, "", "ClippingGeometry", "")
	
	
	
	folder_name=out_clip+"scaled"
	arcpy.CreateFolder_management(TestFolder,folder_name)
	arcpy.env.workspace="E:\\Shivaprakash\\TEST\\NDVI_INDIA\\TEST\\"+out_clip
	rasterlist_tiff=arcpy.ListRasters("*","TIF")
	for raster in rasterlist_tiff:
		outRaster=TestFolder+"\\"+folder_name+"\\"+raster
		Out=Raster(raster)*0.02
		Out.save(outRaster)
	
	
	folder_addNull= out_clip+"_addNull"
	arcpy.CreateFolder_management(TestFolder,folder_addNull)
	acrpy.env.workspace="E:\\Shivaprakash\\TEST\\NDVI_INDIA\\TEST\\"+folder_name
	rasterlist_tiff_null=arpy.ListRasters("*","TIF")
	whereClause="VALUE=0"
	for raster in rasterlist_tiff_null:
		outRasterNull=TestFolder+"\\"+folder_addNull+"\\"+raster
		OutNull=SetNull(raster,raster,whereClause)
		OutNull.save(outRasterNull)
	
	
	
	folder_avg16days=out_clip+"_avg16days"
	arcpy.CreateFolder_management(TestFolder,folder_avg16days)
	acrpy.env.workspace="E:\\Shivaprakash\\TEST\\NDVI_INDIA\\TEST\\"+folder_addNull
	rasterlist_tiff_avg16=arcpy.ListRasters("*","TIF")
	arcpy.CopyRaster_management(rasterlist_tiff_avg16[0],TestFolder+"\\"+folder_avg16days+"\\"+rasterlist_tiff_avg16[0],"","","","","","")
	raster_odd=rasterlist_tiff_avg16[1::2]
	raster_even=rasterlist_tiff_avg16[2::2]
	counter=0
	for rasterEven in raster_even:
		outRasterAvg=TestFolder+"\\"+folder_avg16days+"\\"+rasterEven
		OutEven=(Raster(rasterEven)+Raster(raster_odd[counter]))/2
		OutEven.save(OutRasterAvg)
		counter++
	
	
	
	
	