import urllib.request
import cv2
import numpy as np
import os


######### Basically collect all the negative images from Image-net.org #############

negative_images_url = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
positive_images_url = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07747607'

def store_raw_images(url_link,folder_name):
    image_urls = urllib.request.urlopen(url_link).read().decode()
    pic_num = 1

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for i in image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, folder_name+"/"+str(pic_num)+".jpg")
            img = cv2.imread(folder_name+"/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite(folder_name+"/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
        except Exception as e:
            print(str(e))  


def bad_files_screener(folder_name):
    for file_type in [folder_name]:
        for img in os.listdir(file_type):
            for bad_pic in os.listdir('badpics'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    bad_pic = cv2.imread('badpics/'+str(bad_pic))
                    current_image = cv2.imread(current_image_path)

                    # check to see if this is a bad picture for training if so DELETE IT
                    if bad_pic.shape == current_image.shape and not(np.bitwise_xor(bad_pic,current_image).any()):
                        print('Getting rid of ' + str(current_image_path))
                        os.remove(current_image_path)
                except Exception as e:
                    print(str(e))


def create_pos_n_neg(folder_name):
    for file_type in [folder_name]:
        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)
            elif file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 100 100\n'
                with open('info.dat','a') as f:
                    f.write(line)



# lets collect images frostore_raw_images()
store_raw_images(negative_images_url,'neg')
store_raw_images(positive_images_url,'pos')


# Get rid of the images that are bad images
bad_files_screener('neg')
bad_files_screener('pos')

#Constructur to make a list of negative and positive files within a txt file
create_pos_n_neg('neg')
create_pos_n_neg('pos')
























