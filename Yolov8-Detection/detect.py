# path = "/Users/siddhartha/Desktop/PROJECTS/Fungus-ROI-Detection/Annotations/imageset/"
path2 = "/Users/siddhartha/Desktop/PROJECTS/Fungus-ROI-Detection/Annotations/imageset/F048a01-12.jpg"
from ultralytics import YOLO

model = YOLO("best.pt")

results = model.predict(source=path2)

# results = model.predict(source=0, stream=True)

# print(results)

for result in results:
    # Detection
    result.boxes.xyxy   # box with xyxy format, (N, 4)
    result.boxes.xywh   # box with xywh format, (N, 4)
    result.boxes.xyxyn  # box with xyxy format but normalized, (N, 4)
    result.boxes.xywhn  # box with xywh format but normalized, (N, 4)
    result.boxes.conf   # confidence score, (N, 1)
    result.boxes.cls    # cls, (N, 1)

#     # Segmentation
#     result.masks.data      # masks, (N, H, W)
#     result.masks.xy        # x,y segments (pixels), List[segment] * N
#     result.masks.xyn       # x,y segments (normalized), List[segment] * N

#     # Classification
#     result.probs     # cls prob, (num_class, )

# # Each result is composed of torch.Tensor by default,
# # in which you can easily use following functionality:
# result = result.cuda()
# result = result.cpu()
# result = result.to("cpu")
# result = result.numpy()

