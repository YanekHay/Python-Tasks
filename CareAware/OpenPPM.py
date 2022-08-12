import cv2
import matplotlib.pyplot as plt
import torchvision

rgb_images = [cv2.rotate(cv2.imread(f"C:\\Users\\Yanek\\Downloads\\mensa_seq0_1.1\\rgb\\seq0_{i:04d}_0.ppm"),rotateCode = 2) for i in range(1000)]
depth_images = [cv2.rotate(cv2.imread(f"C:\\Users\\Yanek\\Downloads\\mensa_seq0_1.1\\depth\\seq0_{i:04d}_0.pgm"),rotateCode = 2) for i in range(1000)]


### Getting the body points
model = torchvision.models.detection.keypointrcnn_resnet50_fpn(pretrained=True)
model.eval()

from torchvision import transforms as T


# preprocess the input image
transform = T.Compose([T.ToTensor()])

img_tensor = transform(rgb_images[0])
# forward-pass the model
# the input is a list, hence the output will also be a list
output = model([img_tensor])

plt.imshow(rgb_images[0])
# cv2.imshow(winname = "image",mat = rgb_images
x_keypoints = []
y_keypoints = []
print(output[0]["keypoints"][0,])
for keypoint_set in output[0]["keypoints"]:
    for keypoint in keypoint_set:                    
            x_keypoints.append(keypoint[0].item())
            y_keypoints.append(keypoint[1].item())
# print(x_keypoints,y_keypoints)
plt.scatter(x_keypoints,y_keypoints)
plt.show()




