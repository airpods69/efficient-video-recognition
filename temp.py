

import os
import shutil
dir='/local/scratch/c_adabouei/video_analysis/dataset/kinetics-dataset/all_files/k400_targz/replacement/replacement_for_corrupted_k400'
train_dir='/local/scratch/c_adabouei/video_analysis/dataset/kinetics-dataset/all_files/k400_targz/train/'
val_dir='/local/scratch/c_adabouei/video_analysis/dataset/kinetics-dataset/all_files/k400_targz/val/'
for f in os.listdir(dir):
    if(os.path.exists(train_dir+f)):
        # print('train')
        shutil.move(dir+'/'+f , train_dir+f)
    elif(os.path.exists(val_dir+f)):
        # print('val')
        shutil.move(dir+'/'+f , val_dir+f)
    else:
        print('test')