import os
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras import optimizers
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dropout, Flatten, Dense, Activation
from tensorflow.python.keras.layers import Convolution2D, MaxPooling2D
from tensorflow.python.keras import backend as K

K.clear_session()
data_entrenamiento = './data/entrenamiento'
data_validacion = './data/validacion'

# Rutas de imagenes a entrenar y validar
data_entrenamiento = './data/entrenamiento'
data_validacion = './data/validacion'

# Preparamos nuestras imagenes
entrenamiento_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

entrenamiento_generador = entrenamiento_datagen.flow_from_directory(
    data_entrenamiento,
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical')

validacion_generador = test_datagen.flow_from_directory(
    data_validacion,
    target_size=(150, 150),
    batch_size=32,
    class_mode='categorical')

cnn = Sequential()
cnn.add(Convolution2D(32, (3, 3), padding='same', input_shape=(150, 150, 3), activation='relu'))
cnn.add(MaxPooling2D(pool_size=(2, 2)))

cnn.add(Convolution2D(64, (2, 2), padding='same'))
cnn.add(MaxPooling2D(pool_size=(2, 2)))

cnn.add(Flatten())
cnn.add(Dense(256, activation='relu'))
cnn.add(Dropout(0.5))
cnn.add(Dense(3, activation='softmax'))

cnn.compile(loss='categorical_crossentropy',
            optimizer=optimizers.Adam(lr=0.0004),
            metrics=['accuracy'])

cnn.fit_generator(
    entrenamiento_generador,
    steps_per_epoch=1000,
    epochs=20,
    validation_data=validacion_generador,
    validation_steps=300)

target_dir = './modelo/'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

cnn.save('./modelo/modelo.h5')
cnn.save_weights('./modelo/pesos.h5')
