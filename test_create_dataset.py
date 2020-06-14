import modelling_dataset as md 

m = md.modelling_dataset()
X, y = m.load_data()
m.create_hdf5(X, y)