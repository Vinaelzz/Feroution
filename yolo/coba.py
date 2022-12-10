import torch

model1 = torch.hub.load("D:\KULIAH PENS\MBKM\Dicoding\Project akhir\yolo", 'custom', path="best.pt", source='local')

img = 'D:\KULIAH PENS\MBKM\Dicoding\Project akhir\yolo\photos\cobakomedo11.jpg'

results = model1(img)

results.show()
