import mmcv

import mmcv_custom   # noqa: F401,F403
import mmseg_custom   # noqa: F401,F403
from mmseg.apis import inference_segmentor, init_segmentor, show_result_pyplot
from mmseg.core.evaluation import get_palette
from mmcv.runner import load_checkpoint
from mmseg.core import get_classes
import cv2
import os.path as osp
from pathlib import Path
import pandas as pd
from tqdm import tqdm
import numpy as np
import setproctitle
setproctitle.setproctitle('segmentation@hanzhenyu')


INPUT_PATH = Path('./GoogleStreetView')
SAVE_PATH = Path('../../../temp_output/GoogleStreetView_Segmentation')
SAVE_VIS_PATH = Path('../../../temp_output/GoogleStreetView_Segmentation_Vis')

SAVE_PATH.mkdir(exist_ok=True,parents=True)
SAVE_VIS_PATH.mkdir(exist_ok=True,parents=True)

LABEL_NAMES = np.asarray([
    'road','sidewalk','building','wall','fence','pole','traffic light','traffic sign','vegetation','terrain','sky','person',
    'rider','car','truck','bus','train','motorcycle','bicycle'
])

def main():
    args = {}
    args['config'] = 'configs/cityscapes/mask2former_beit_adapter_large_896_80k_cityscapes_ss.py'
    args['checkpoint'] = './mask2former_beit_adapter_large_896_80k_cityscapes.pth.tar'
    args['device'] = 'cuda:0'
    args['palette'] = 'cityscapes'
    args['opacity'] = 0.5


    # build the model from a config file and a checkpoint file
    
    model = init_segmentor(args['config'], checkpoint=None, device=args['device'])
    checkpoint = load_checkpoint(model, args['checkpoint'], map_location='cpu')
    if 'CLASSES' in checkpoint.get('meta', {}):
        model.CLASSES = checkpoint['meta']['CLASSES']
    else:
        model.CLASSES = get_classes(args['palette'])
        
    # test a single image
    
    for region in INPUT_PATH.iterdir():
        region_path = INPUT_PATH.joinpath(region.stem)
        save_region_path = SAVE_PATH.joinpath(region.stem)
        save_vis_region_path = SAVE_VIS_PATH.joinpath(region.stem)
        save_region_path.mkdir(exist_ok=True,parents=True)
        save_vis_region_path.mkdir(exist_ok=True,parents=True)
        stitch_meta_info = pd.read_csv(region_path.joinpath('stitch_meta_info.csv'))

        segmentation_df = pd.DataFrame()
        for idx in tqdm(range(stitch_meta_info.shape[0])):
            result = inference_segmentor(model, str(region_path.joinpath(stitch_meta_info.loc[idx,'file_name'])))[0]

            # 整理信息
            tmp_seg_results = {}
            for i in range(len(LABEL_NAMES)):
                tmp_seg_results[LABEL_NAMES[i]] = [np.sum(np.sum((result == i))).astype(float) / (result.shape[0] * result.shape[1])]

            
            # save pred results
            cv2.imwrite(str(save_region_path.joinpath(stitch_meta_info.loc[idx,'file_name'][:-4] + '.png')), np.expand_dims(result,2).astype('uint8'))

            # save visable results
            if hasattr(model, 'module'):
                model = model.module
            vis = model.show_result(str(region_path.joinpath(stitch_meta_info.loc[idx,'file_name'])), [result],
                                    palette=get_palette(args['palette']),
                                    show=False, opacity=args['opacity'])


            cv2.imwrite(str(save_vis_region_path.joinpath(stitch_meta_info.loc[idx,'file_name'][:-4] + '.png')), vis)
            
            segmentation_df = pd.concat([segmentation_df,pd.DataFrame(tmp_seg_results)])
        segmentation_meta_info = stitch_meta_info.join(segmentation_df.reset_index())
        segmentation_meta_info.to_csv(save_region_path.joinpath('segmentation_meta_info.csv'),index=False)




if __name__ == '__main__':
    main()