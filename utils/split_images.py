import numpy as np
import matplotlib.pyplot as plt

# 假设你的三维数据是一个形状为 (32, 192, 320) 的numpy数组
data = np.load('./00633/stage2_C3_features.npy', mmap_mode='r')

# 遍历每个通道并进行可视化
num_channels = data.shape[0]  # 获取通道数
for channel in range(num_channels):
    fig = plt.figure(figsize=(data.shape[2]/100, data.shape[1]/100), dpi=300)  # 设置图像大小与原图相同
    plt.imshow(data[channel, :, :])
    plt.axis('off')  # 去除坐标轴
    # 保存图像
    save_path = f'channel_{channel+1}_visualization.png'
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.0)
    plt.show()
    # 关闭当前图像
    plt.close()
    print(f'Saved visualization of Channel {channel+1} to {save_path}')
