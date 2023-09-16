import cv2;
import numpy as np;
import matplotlib.pyplot as plt;
import os;
import sys;

#Remove interfering samples

def func(img,pic_path,pic):
	gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
	r,c = gray_img.shape[:2];
	dark_sum=0;
	dark_prop=0;
	piexs_sum=r*c;
	

	for row in gray_img:
		for colum in row:
			if colum<40:
				dark_sum+=1;
	dark_prop=dark_sum/(piexs_sum);	
	print("dark_sum:"+str(dark_sum));
	print("piexs_sum:"+str(piexs_sum));
	print("dark_prop=dark_sum/piexs_sum:"+str(dark_prop));
	if dark_prop >=0.75;
		print(pic_path+" is dark!");
		cv2.imwrite("../DarkPicDir/"+pic,img);
	else:
		print(pic_path+" is bright!")
	#hist(pic_path);
 

def hist(pic_path):
	img=cv2.imread(pic_path,0);
	hist = cv2.calcHist([img],[0],None,[256],[0,256])
	r,c = img.shape[:2];
	dark_sum=0;
	for row in img:
		for colum in row:
			if colum==0:
				dark_sum+=1;
	print(pic_path+"dark_sum:"+str(dark_sum));
	if dark_sum > 2510:
			os.remove(pic_path)

def readAllPictures(pics_path):
	if not os.path.exists(pics_path):
		print("error！")
		return;
	allPics = [];
	pics = os.listdir(pics_path);
	for pic in pics:
		pic_path = os.path.join(pics_path,pic);
		if os.path.isfile(pic_path):
			allPics.append(pic_path);
			img=cv2.imread(pic_path);
			func(img,pic_path,pic);
	return allPics;
 

def createDarkDir():
	DarkDirPath = "../DarkPicDir";
	isExists = os.path.exists(DarkDirPath);
	if not isExists:
		os.makedirs(DarkDirPath);
		print("dark pics dir is created successfully!");
		return True;
	else:
		return False;

if __name__ =='__main__':

		for person in os.listdir('/lustre/home/acct-eejxh/eejxh/yhy/gait/processed'):
			for condi in os.listdir('/lustre/home/acct-eejxh/eejxh/yhy/gait/processed/{}'.format(person)):
				for angel in os.listdir('/lustre/home/acct-eejxh/eejxh/yhy/gait/processed/{}/{}'.format(person,condi)):
					for file in os.listdir('/lustre/home/acct-eejxh/eejxh/yhy/gait/processed/{}/{}/{}'.format(person,condi,angel)):
						hist('/lustre/home/acct-eejxh/eejxh/yhy/gait/processed/{}/{}/{}/{}'.format(person,condi,angel,file))
