import cv2, os, glob, json, tqdm
import imagesize as ims


# data_root = '/data/users/mk/video-crawler/AVSpeechDownloader/preprocess'
data_root = '/data/users/mk/data/'
dir_names = glob.glob(os.path.join(data_root, '*/*'))

w_thresh = 150 

with open("ai_img_list_all.json", "w") as fp:
    json.dump(dir_names, fp)

# import ipdb; ipdb.set_trace()

true_list = []
wh_list = []
dir_img_list = []


for dir_name in tqdm.tqdm(dir_names):

    num_t = 0
    for file_name in glob.glob(os.path.join(dir_name, '*.jpg')):
        width, height = ims.get(file_name)
        wh_list.append((width, height))
        if width > w_thresh: num_t += 1
        # print(width, height, end=' ')
        dir_img_list.append((dir_name, num_t))

    if num_t > 20:
        true_list.append(dir_name)
        # print("True \n")
        
with open("ai_dir_imgnum_list.json", "w") as fp:
    json.dump(dir_img_list, fp)

with open("ai_img_list_b192.json", "w") as fp:
    json.dump(true_list, fp)

with open("ai_img_wh_list.json", "w") as fp:
    json.dump(wh_list, fp)


print('Num T: {}'.format(num_t))
print('T Ratio: {:.2f}'.format(num_t / len(dir_names)))
