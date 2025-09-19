在ub20+torch2.4.1+cu118配置环境
# 安装
1. 使用conda创建环境
```
conda create -n graspnet python=3.8
```
2. 安装torch
```
conda install pytorch==2.4.1 torchvision==0.19.1 torchaudio==2.4.1 pytorch-cuda=11.8 -c pytorch -c nvidia
```
3. 安装pointnet2&&knn
```
cd pointnet2
python setup.py install
cd ../knn
python setup.py install
```
4. 安装graspnetAPI
```
cd ../graspnetAPI
pip install .
```
4. 安装graspnet-baseline
```
cd ../graspnet-baseline
pip install .
```
# 使用
```
export XDG_SESSION_TYPE=x11
python demo.py --checkpoint_path logs/log_kn/checkpoint.tar
```
# 参考
- https://github.com/H-Freax/GraspNet_Pointnet2_PyTorch1.13.1?tab=readme-ov-file#usage