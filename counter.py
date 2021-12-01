import cv2
import matplotlib.pylot as plt 
import cvlib as cv
from cvlib.object_detection import draw_bbox
im = cv2. imread( "image.jpeg")
bbox, label, conf =cvimagedetect_common_objects( im)
output_image = draw_bbox( im,bbox, label, conf)
plt.imshow( output_image)
plt.show()
print("The # of vehicles in the image is " +str(label.count ("car")))
