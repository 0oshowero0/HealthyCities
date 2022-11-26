import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

plt.rcParams['ps.fonttype'] = 42
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = ['Arial']
plt.rcParams['xtick.labelsize']=13
plt.rcParams['ytick.labelsize']=13


LABEL_NAMES = np.asarray([
    'road','sidewalk','building','wall','fence','pole','traffic light','traffic sign','vegetation','terrain','sky','person',
    'rider','car','truck','bus','train','motorcycle','bicycle'
])

palette = np.array([[128, 64, 128],
 [244, 35, 232],
 [70, 70, 70],
 [102, 102, 156],
 [190, 153, 153],
 [153, 153, 153],
 [250, 170, 30],
 [220, 220, 0],
 [107, 142, 35],
 [152, 251, 152],
 [70, 130, 180],
 [220, 20, 60],
 [255, 0, 0],
 [0, 0, 142],
 [0, 0, 70],
 [0, 60, 100],
 [0, 80, 100],
 [0, 0, 230],
 [119, 11, 32]])

palette = palette / 255

palette_list = []
for i in range(palette.shape[0]):
    palette_list.append(mcolors.to_hex(palette[i,:]))
    print(mcolors.to_hex(palette[i,:]))

for i in range(len(LABEL_NAMES)):
    print(LABEL_NAMES[i])

sns.palplot(sns.color_palette(palette_list))
plt.show()