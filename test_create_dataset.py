import modelling_dataset as md 
import numpy as np

m = md.modelling_dataset()
X, y = m.load_data()
m.create_hdf5(X, y, '_64_rgb')

X_train, X_test, y_train, y_test = m.load_hdf5('_64_rgb')

print('Number of classes in y_train: {}'.format(len(np.unique(y_train))))
print('Number of classes in y_test: {}'.format(len(np.unique(y_test))))