import torch
from torchvision.datasets import ImageFolder
from torchvision import transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])
dataset = ImageFolder(root='./data',transform=transform)

print(dataset.class_to_idx)
print(dataset.classes)

dataloader = DataLoader(dataset=dataset,shuffle=True,batch_size=50)

