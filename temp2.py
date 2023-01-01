




import glob
import os
val_dir='/local/scratch/c_adabouei/video_analysis/dataset/kinetics-dataset/all_files/k400_targz/val/'
f_new = open("val_updated.txt","a")
f=open('val.txt','r')
l=f.readlines()
for i in l:
    path, label = i.split(' ')
    temp = glob.glob(os.path.join(val_dir, path))
    if(len(temp) != 0):
        #add to new file
        f_new.write("{} {}".format(path,label))
    else:
        print("1")
f.close()
f_new.close()