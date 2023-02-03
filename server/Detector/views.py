from django.shortcuts import render
# Create your views here.
from .models import Xrays
import json


## For Prediction
import torch
import torchvision
import torchvision.transforms as transforms
from PIL import Image


def uploadXray(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            image = request.FILES['xray_image']
            obj = Xrays(image = image, uploadedBy = request.user)
            obj.save()
            result = predictXray(obj)
            obj.result = result
            obj.save()
    return JsonResponse({'objectId' : obj.id})


classes = ['COVID', 'Lung_Opacity', 'Normal', 'Viral Pneumonia']
def predictXray(xrayImage):
    img = Image.open(xrayImage.image).convert('RGB')
    trans = transforms.Compose([transforms.ToTensor()])
    transimg = trans(img)
    model = torchvision.models.resnet152(pretrained=False)
    model.fc = torch.nn.Linear(2048,4)
    model.load_state_dict(torch.load('xyz_epoch_1.pt'))
    model.eval()
    with torch.no_grad():
        output = model(transimg.unsqueeze(0))

    return classes[torch.argmax(output).item()]