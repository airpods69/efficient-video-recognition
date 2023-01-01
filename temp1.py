

import glob
import os
train_dir='/local/scratch/c_adabouei/video_analysis/dataset/kinetics-dataset/all_files/k400_targz/train/'
f_new = open("train_updated.txt","a")
f=open('train.txt','r')
l=f.readlines()
for i in l:
    path, label = i.split(' ')
    temp = glob.glob(os.path.join(train_dir, path))
    if(len(temp) != 0):
        #add to new file
        f_new.write("{} {}".format(path,label))
    else:
        print("1")
f.close()
f_new.close()