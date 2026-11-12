class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__() 
        
        # First Convolutional Layer
        # 3 = input channels (RGB = 3, Grayscale = 1)
        # 6 = output channels (feature maps)
        # 5 = 5x5 kernel size (image will be 28x28 after conv on a 32x32 input)
        self.conv1 = nn.Conv2d(3, 6, 5)
        
        # Second Convolutional Layer (takes 6 channels from conv1, outputs 16)
        self.conv2 = nn.Conv2d(6, 16, 5)
        
        # Max Pooling Layer
        # 2 = kernel size (2x2 window)
        # 2 = stride (how many pixels the window moves)
        self.pool = nn.MaxPool2d(2, 2)
        
        # Fully Connected (Linear) Layers
        # 16 * 5 * 5 = flattened feature volume (16 channels of 5x5 images)
        # 120 = hidden layer size
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        
        # Output Layer (10 classes for CIFAR-10)
        self.fc3 = nn.Linear(84, 10)
        
        # Activation Function
        self.relu = nn.ReLU()

    def forward(self, x):
        out1 = self.conv1(x)
        out1 = self.relu(out1)
        out1 = self.pool(out1)
        
        out2 = self.conv2(out1)
        out2 = self.relu(out2)
        out2 = self.pool(out2)
        
        # Flatten the 3D tensor into a 1D vector for the linear layers
        out2 = out2.view(-1, 16 * 5 * 5)
        
        # FC Layer 1: Linear -> ReLU
        fcout1 = self.fc1(out2)
        fcout1 = self.relu(fcout1)
        
        # FC Layer 2: Linear -> ReLU
        fcout2 = self.fc2(fcout1)
        fcout2 = self.relu(fcout2)
        
        # Output Layer (raw logits)
        output = self.fc3(fcout2)
        
        return output