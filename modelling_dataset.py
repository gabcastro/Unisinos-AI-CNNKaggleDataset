import cv2
import glob
import numpy as np
import pandas as pd 

from sklearn.model_selection import train_test_split

import keras

class modelling_dataset():

    def __init__(self):
        self.map_animals = {
            0: 'bald_eagle'#,
            # 1: 'black_bear',
            # 2: 'bobcat',
            # 3: 'canada_lynx',
            # 4: 'columbian_black-tailed_deer',
            # 5: 'cougar',
            # 6: 'coyote',
            # 7: 'deer',
            # 8: 'elk',
            # 9: 'gray_fox',
            # 10: 'gray_wolf',
            # 11: 'mountain_beaver',
            # 12: 'nutria',
            # 13: 'raccoon',
            # 14: 'raven',
            # 15: 'red_fox',
            # 16: 'ringtail',
            # 17: 'sea_lions',
            # 18: 'seals',
            # 19: 'virginia_opossum'
        }

        self.picture_size = 64
        self.pics = []
        self.labels = []
        self.total_pics_by_class = {}
        self.test_size = 0.15
        self.num_classes = len(self.map_animals)


    def load_data(self):
        for k, char in self.map_animals.items():
            pictures = [k for k in glob.glob('./oregon_wildlife/%s/*' % char)]
            nb_pic = len(pictures)

            print('\nReading {}º folder ({}) with a total of {} images'.format(k + 1, char, nb_pic))

            i, rs, rd = 0, 0, 0
            for pic in np.random.choice(pictures, nb_pic):
                try:
                    a = cv2.imread(pic)
                    try:
                        a = cv2.resize(a, (self.picture_size, self.picture_size))            
                        self.pics.append(a)
                        self.labels.append(k)
                        i += 1
                    except:
                        rs += 1
                        print('{} - Wasn\'t possible resize image: {}'.format(rs, pic))
                except:
                    rd += 1
                    print('{} - Wasn\'t possible read. Image: {}'.format(rd, pic))

            self.total_pics_by_class[char] = i

        return np.array(self.pics), np.array(self.labels) 

    def preprocessing_data(self, X, y):
        y = keras.utils.to_categorical(y, self.num_classes)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size)

        X_train = X_train.astype('float32')/255.
        X_test = X_test.astype('float32')/255.

        return X_train, X_test, y_train, y_test

    @property
    def classes_summary(self):
        return pd.DataFrame(self.total_pics_by_class.items(), columns=['Class', 'Total Items'])