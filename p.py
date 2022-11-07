import tensorflow as tf
#from tensorflow.keras import models, layers
#import matplotlib.pyplot as plt

model = tf.keras.models.load_model("Banna_project_model2.h5")
model.save(f"/2/")
