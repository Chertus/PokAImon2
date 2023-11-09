import torch
import torch.nn as nn
import torch.nn.functional as F

class DQN(nn.Module):
    def __init__(self, input_shape, num_actions):
        super(DQN, self).__init__()
        # Define the layers of the network
        self.conv1 = nn.Conv2d(input_shape[0], 32, kernel_size=8, stride=4)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=4, stride=2)
        self.conv3 = nn.Conv2d(64, 64, kernel_size=3, stride=1)

        # Calculate the size of the output from the last convolutional layer
        self.fc_input_dim = self.feature_size(input_shape)

        self.fc1 = nn.Linear(self.fc_input_dim, 512)
        self.fc2 = nn.Linear(512, num_actions)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = x.view(x.size(0), -1) # Flatten the tensor
        x = F.relu(self.fc1(x))
        return self.fc2(x)

    def feature_size(self, input_shape):
        return nn.Conv2d(input_shape[0], 32, kernel_size=8, stride=4)\
            .forward(torch.zeros(1, *input_shape)).view(1, -1).size(1)

# Example usage
# input_shape = (number of channels, height, width) of the processed game state
# num_actions = number of possible actions in the game
model = DQN(input_shape=(3, 84, 84), num_actions=10)
