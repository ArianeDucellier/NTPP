# NTPP

The obkective of this project is to model earthquake catalogs as point processes using neural networks.

We use the transformer Hawkes process code from Simiao Zuo et al. (2020):

ArXiv: https://arxiv.org/abs/2002.09291

GitHub: https://github.com/SimiaoZuo/Transformer-Hawkes-Process

Their code requires the packages PyTorch and tqdm (see environment.yml to install the required packages).

They also use GPUs to run the code. To run the code on a CPU, change the following lines:

- In Main.py, line 193, modify to:

opt.device = torch.device('cpu')

- In Models.py, line 50, modify to:

self.position_vec = torch.tensor(
    [math.pow(10000.0, 2.0 * (i // 2) / d_model) for i in range(d_model)],
    device=torch.device('cpu'))
