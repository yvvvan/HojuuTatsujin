import torch
import pathlib
import cv2

cap = cv2.VideoCapture(0)

# Capture frame
ret, frame = cap.read()
if ret:
    cv2.imwrite('image.jpg', frame)
    print("saved")
else:
    print("error")

# img_path = pathlib.Path("mahjongcv/test_images/IMG-20230714-WA0029.jpg")

# model = torch.hub.load('ultralytics/yolov5', 'bestv5.pt')
# results = model(img_path)
# r_img = results.render() # returns a list with the images as np.array
# img_with_boxes = r_img[0] # image with boxes as np.array

model = torch.hub.load('mahjongcv/yolov5', 'custom', path='mahjongcv/best.pt', force_reload=True, 
    source='local')

while True:
    ret, frame = cap.read()

    pred = model(frame)
    #pred.show() #show image but can't assign to a variable
    # pred.save()
    print(pred.pandas().xyxy[0])
# for index, row in pred.pandas().xyxy[0].iterrows():
#     print(row['xmin'], row['ymin'], row['name'])


cap.release()