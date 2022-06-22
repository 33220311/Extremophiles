import keras
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dense, Dropout, Activation
from keras.layers.normalization import BatchNormalization
from keras import optimizers
from keras.utils import np_utils
from sklearn.metrics import roc_auc_score
from keras.callbacks import EarlyStopping 
from keras import optimizers

seed_value= s_value
tf.random.set_seed(seed_value)
n_cols = X_train.shape[1]

model = Sequential()
model.add(Dense(100,activation='relu',kernel_initializer='he_uniform', input_shape=(n_cols,)))
model.add(Dense(1, activation='sigmoid'))
sgd = optimizers.SGD(lr=0.001, decay=1e-8, momentum=0.8, nesterov=True)
model.compile(loss='mean_squared_error',optimizer=sgd,
              metrics=['accuracy'])
from keras.callbacks import TensorBoard, ModelCheckpoint, EarlyStopping, CSVLogger
checkpointer = ModelCheckpoint(
    filepath='folder/.{epoch:03d}-{val_loss:.3f}.h5',
    verbose=1,
    save_best_only=True)
history = model.fit(X_train_scaled, y_train,    
   batch_size=60, 
   epochs = 1000, 
   verbose = 1, 
   validation_data=(X_test_scaled,y_test), 
   callbacks = [EarlyStopping(monitor = 'val_loss', patience = 150),checkpointer]
)