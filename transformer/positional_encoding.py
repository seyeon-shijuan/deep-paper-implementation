import torch
import torch.nn as nn
import math

def get_device():
    return torch.device('cuda' if torch.cuda.is_available() else 'cpu')


class PositionalEncoding(nn.Module):

    def __init__(self, d_model, max_len, device):
        super(PositionalEncoding, self).__init__()

        position = torch.arange(max_len, device=device).double().unsqueeze(1)
        # -math.log(10000.0) / d_model
        # div_term = torch.arange(0, d_model, 2, device=device) / d_model
        div_term = torch.exp(torch.arange(0, d_model, 2, device=device) *(-math.log(10000.0) / d_model))

        pe = torch.zeros(max_len, d_model, device=device)
        # pe[:,::2] = torch.sin(position/10000**(div_term))
        pe[:,::2] = torch.sin(position*div_term)
        # pe[:,1::2] = torch.cos(position/10000**(div_term))
        pe[:,1::2] = torch.cos(position*div_term)

        print('here')



if __name__ == '__main__':
    device = get_device()
    positional_encoding = PositionalEncoding(d_model=6, max_len=10, device=device)

