import torch
import pathlib

img_path = pathlib.Path("./test_images/IMG-20230714-WA0029.jpg")

# model = torch.hub.load('ultralytics/yolov5', 'bestv5.pt')
# results = model(img_path)
# r_img = results.render() # returns a list with the images as np.array
# img_with_boxes = r_img[0] # image with boxes as np.array

model = torch.hub.load('yolov5', 'custom', path='best.pt', force_reload=True, 
    source='local')
pred = model(img_path)
#pred.show() #show image but can't assign to a variable
pred.save()