#-*-coding:utf-8-*-
import pydicom as dicom
import json
def loadFileInformation(filename):
	information = {}
	ds = dicom.read_file(filename)
	information['PatientID'] = ds.PatientID
	information['PatientName'] = ds.PatientName
	information['PatientBirthDate'] = ds.PatientBirthDate
	information['PatientSex'] = ds.PatientSex
	information['StudyID'] = ds.StudyID
	information['StudyDate'] = ds.StudyDate
	information['StudyTime'] = ds.StudyTime
	information['InstitutionName'] = ds.InstitutionName
	information['Manufacturer'] = ds.Manufacturer
	print(ds)
	print(information)
	return information

a=loadFileInformation("/Users/daven/个人资料/项目/肖晟老师/MedData/MedData/dr_sample/1.2.156.147522.44.410947.28674.20180314091415/1.2.156.147522.44.410947.28674.1.20180314091459/1.2.156.147522.44.410947.28674.1.1.20180314091459.dcm")