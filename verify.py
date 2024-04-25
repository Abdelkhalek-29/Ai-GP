import torch

def calculate_similarity(feature_vector1, feature_vector2):
    tensor1 = torch.tensor(feature_vector1)
    tensor2 = torch.tensor(feature_vector2)
    
    distance = (tensor1 - tensor2).norm().item()
    
    if distance < 1.0:
        return True
    else:
        return False
