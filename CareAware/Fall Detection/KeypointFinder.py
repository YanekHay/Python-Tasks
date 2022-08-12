from fnmatch import translate
import cv2
import numpy as np
import matplotlib.pyplot as plt
import torchvision
from torchvision import transforms as T
import torch
from math import pi



if torch.cuda.is_available():
  device = "cuda"
else:
  device = "cpu"
  
print(torch.cuda.get_device_name(0))
### Getting the body points
model = torchvision.models.detection.keypointrcnn_resnet50_fpn(pretrained=True)
model = model.to(device)
model.eval()

# preprocess the input image
transform = T.Compose([T.ToTensor()])

#In this cell we want to visualize the body points putting it on the image.
transform = T.Compose([T.ToTensor(), T.Resize((500, 500))])
mask = np.array([0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ])


#     long map(long x, long in_min, long in_max, long out_min, long out_max)
# {
#   return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
# }
def map(x,min_from,max_from,min_to,max_to):
  return (x-min_from)*(max_to-min_to)/(max_from-min_from)+min_to

def theta(x, y):
  if torch.all(x == y):
    return 0
  return torch.arcsin((x[0] - y[0]) / ((x[0] - y[0]) **2 + (x[1] - y[1]) **2 )** 0.5 ) /(2*pi)

def ewa_(x, alpha):
  l = []
  temp = 0
  for t, item in enumerate(x):
    temp = (alpha * item + (1 - alpha)*temp)/(1 - alpha ** (t + 1))
    l.append(temp)  
    
  return l

cinematic_features = []
heights = []
height_width_ratio = []


cap = cv2.VideoCapture(0)
cv2.plot

while cap.isOpened():
    _, frame = cap.read()
    # flip the frame to horizontal direction
    frame = cv2.flip(frame, 1)
    height , width, channel = frame.shape

    # combine frame and background image using the condition
    #output_image = np.where(condition, frame, bg_image)
    
    
    image_tf = transform(frame)
    
    output = model([image_tf.to(device)])
    
    if not output:
      continue
    

    #image_tf = image_tf.transpose(0,1).transpose(1,2)


    points = output[0]["keypoints"][0][mask][...,:-1]
    points = points.detach().cpu().numpy()
    
    image_tf = image_tf.detach().cpu().numpy()
    # show outputs
    #cv2.imshow("mask", mask)

    
    for point in points:
        point[0] = map(point[0],0,500,0,width)
        point[1] = map(point[1],0,500,0,height)
        point_ = np.array(point,dtype='int')
        frame = cv2.circle(frame,center=point_,radius=5,color = (255,0,0))
    
    cv2.imshow("Output", frame)

    
    ## If 'Q' pressed close windows
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
