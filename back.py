import cv2
import os

#img = cv2. imread("galaxy.jpg",0) #0 for grayscale, 1 for color, -1 for color with alpha channels(transparency.etc)

"""print(type(img))
print(img)
print(img.shape) """
class ResizeClass:
	def __init__(self, file):
		global img
		img = os.path.abspath(file)
		print(file+' cool')

	def rename(file_path):
		split = file_path.split("/")
		original_name = split[-1]
		return original_name

	def showdimensions(img):
		image = cv2.imread(img,1)
		print(image.shape)
		print(image.ndim)
		return image.shape

	def half(file_path):
		img = cv2.imread(file_path,1)
		resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
		cv2.imshow("Half",resized_image)
		original_name = ResizeClass.rename(file_path)
		newname = 'half_'+original_name
		desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
		cv2.imwrite(desktop+'/'+newname,resized_image)
		cv2.waitKey(400)
		cv2.destroyAllWindows()	
		#return os.path.abspath('')+'/'+newname
		return desktop+'/'+newname

	def low(file_path):
		img = cv2.imread(file_path,1)
		resized_image = cv2.resize(img,(320,200))
		cv2.imshow("Low",resized_image)
		original_name = ResizeClass.rename(file_path)
		newname = 'low_'+original_name
		desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
		cv2.imwrite(desktop+'/'+newname,resized_image)
		cv2.waitKey(400)
		cv2.destroyAllWindows()	
		return desktop+'/'+newname

	def medium(file_path):
		img = cv2.imread(file_path,1)
		resized_image = cv2.resize(img,(432,227))
		cv2.imshow("Medium",resized_image)
		original_name = ResizeClass.rename(file_path)
		newname = 'medium_'+original_name
		desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
		cv2.imwrite(desktop+'/'+newname,resized_image)
		cv2.waitKey(400)
		cv2.destroyAllWindows()
		return desktop+'/'+newname

	def high(file_path):
		img = cv2.imread(file_path,1)
		resized_image = cv2.resize(img,(1060,795))
		cv2.imshow("Medium",resized_image)
		original_name = ResizeClass.rename(file_path)
		newname = 'high_'+original_name
		desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
		cv2.imwrite(desktop+'/'+newname,resized_image)
		cv2.waitKey(400)
		cv2.destroyAllWindows()
		return desktop+'/'+newname


#cv2.imwrite('resized_'+image,re)