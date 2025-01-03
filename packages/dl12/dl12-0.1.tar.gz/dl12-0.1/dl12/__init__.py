p1='''
import numpy as np

def unit(x):
    if x>=0:
        return 1
    else :
        return 0
    
def perceptron_model(x,w,b):
    v=np.dot(w,x)+b
    return unit(v)

def notgate(x):
    w=-1
    b=0.5
    return perceptron_model(x,w,b)

def orgate(x):
    w=np.array([1,1])
    b=-0.5
    return perceptron_model(x,w,b)

def andgate(x):
    w=np.array([1,1])
    b=-1.5
    return perceptron_model(x,w,b)

def xor(x):
    y1=andgate(x)
    y2=orgate(x)
    y3=notgate(y1)
    y4=np.array([y2,y3])
    return andgate(y4)

xor(np.array([0,1]))

'''

p2='''
from tensorflow.keras import models , optimizers ,layers , losses
import numpy as np
import matplotlib.pyplot as plt

X=np.random.randn(1000,10)
y=np.random.randn(1000,1)

def create_model():
    model=models.Sequential([
        layers.Dense(50,activation='relu',input_shape=(10,)),
        layers.Dense(20,activation='relu'),
        layers.Dense(1)
    ])
    return model

def train_model_with_history(model,optimizer,optimizer_name,batch_size,epochs,X,y):
    model.compile(optimizer=optimizer,loss=losses.Huber())
    history=[]
    print(f"Optimizer :{optimizer_name}")
    for epoch in range(epochs):
        hist=model.fit(X,y,batch_size=batch_size,epochs=1,verbose=0)
        loss=hist.history['loss'][0]
        history.append(loss)
        print(f"Epoch: {epoch+1}/{epochs} , Loss:{loss:.4f}")
    return history

sgd=optimizers.SGD(learning_rate=0.01)
adam=optimizers.Adam(learning_rate=0.001)

hist1=train_model_with_history(create_model(),sgd,'SGD',32,32,X,y)
hist2=train_model_with_history(create_model(),adam,'Adam',32,32,X,y)

epochs=32
plt.plot(range(1, epochs + 1), hist1, label='SGD (ReLU)', color='blue')
plt.plot(range(1, epochs + 1), hist2, label='Adam (ReLU)', color='red')


plt.title('SGD vs Adam Optimizer: Loss Comparison')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()
'''

p3='''
from tensorflow.keras import models,layers,models,datasets
import matplotlib.pyplot as plt

(X_train,y_train),(X_test,y_test)=datasets.mnist.load_data()
X_train=X_train.reshape((X_train.shape[0],28,28,1)).astype('float32')/255
X_test=X_test.reshape((X_test.shape[0],28,28,1)).astype('float32')/255

model=models.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64,activation='relu'),
    layers.Dense(10,activation='softmax')
    
])

model.compile(optimizer='sgd',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
history=model.fit(X_train,y_train,epochs=5,validation_data=(X_test,y_test))

test_loss,test_acc=model.evaluate(X_test,y_test)
print(f'Test Accuracy: {test_acc}')

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Val'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Val'], loc='upper left')
plt.show()
'''

p4='''
import torch
import torchvision
from torchvision.transforms import functional as F
import matplotlib.pyplot as plt
import cv2
import numpy as np

model=torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

coco_labels= [
    '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
    'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
    'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
    'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
    'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
    'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
    'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
    'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
    'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
    'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
    'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
    'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
]
def detect(image_path,ct=0.5):
    image=cv2.imread(image_path)
    if image is None:
        print("Error")
        return None
    
    org=image.copy()
    image_tensor=F.to_tensor(image)
    
    with torch.no_grad():
        predictions=model([image_tensor])
        
    labels=predictions[0]['labels'].cpu().numpy()
    boxes=predictions[0]['boxes'].cpu().numpy()
    scores=predictions[0]['scores'].cpu().numpy()
    
    for i,box in enumerate(boxes):
        if scores[i]>=ct:
            label=coco_labels[labels[i]]
            score=scores[i]
            box=boxes[i]
            start_point = (int(box[0]), int(box[1]))
            end_point = (int(box[2]), int(box[3]))
            cv2.rectangle(org,start_point,end_point,(0,255,0),2)
            cv2.putText(org,f"{label} :{score:.2f}" ,start_point,cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
            
    return org

if __name__=="__main__":
    ip='traffic.jpeg'
    detected=detect(ip)
    
    if detected is not None:
        detected=cv2.cvtColor(detected,cv2.COLOR_BGR2RGB)
    
        plt.figure(figsize=(20,10))
        plt.imshow(detected)
        plt.axis('off')                
        plt.show()
                        
            

'''

p5='''
import tensorflow as tf
import numpy as np
import tensorflow.keras as ke
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import SimpleRNN, Dense, Dropout, BatchNormalization
from tensorflow.keras.models import Sequential
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the input data to range [0, 1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# One-hot encode the labels
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# RNN expects sequential data, so we treat each row of the image as a time step
timesteps = x_train.shape[1]  # 28 rows
input_dim = x_train.shape[2]  # 28 columns

# Build the RNN model
model = Sequential([
    SimpleRNN(128, input_shape=(timesteps, input_dim), activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=64, validation_split=0.2)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=2)
print(f"Test accuracy: {test_accuracy:.2f}")
'''

p8='''
import numpy
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist

(X_train,y_train),(X_test,y_test)=mnist.load_data()
print(f"Training data shape: {X_train.shape}")
print(f"Test data shape: {X_test.shape}")

plt.subplot(2,2,1)
plt.imshow(X_train[0],cmap=plt.get_cmap('gray'))
plt.subplot(2,2,2)
plt.imshow(X_train[1],cmap=plt.get_cmap('gray'))
plt.subplot(2,2,3)
plt.imshow(X_train[2],cmap=plt.get_cmap('gray'))


num_pixels=X_train.shape[1]*X_train.shape[2]
X_train=X_train.reshape(X_train.shape[0],num_pixels).astype('float32')
X_test=X_test.reshape(X_test.shape[0],num_pixels).astype('float32')
X_train=X_train/255
X_test=X_test/255

print(f"Shape of reshaped training data: {X_train.shape}")
print(f"Shape of reshaped test data: {X_test.shape}")

noise_factor=0.2
x_train_noisy=X_train+noise_factor*numpy.random.normal(loc=0.0,scale=1.0,size=X_train.shape)
x_test_noisy=X_test+noise_factor*numpy.random.normal(loc=0.0,scale=1.0,size=X_test.shape)
x_train_noisy=numpy.clip(x_train_noisy,0.,1.)
x_test_noisy=numpy.clip(x_test_noisy,0.,1.)

model=Sequential()
model.add(Dense(500,input_dim=num_pixels,activation='relu'))
model.add(Dense(300,activation='relu'))
model.add(Dense(300,activation='relu'))
model.add(Dense(100,activation='relu'))
model.add(Dense(500,activation='relu'))
model.add(Dense(784,activation='sigmoid'))

model.compile(loss='mean_squared_error',optimizer='adam')
print("Training the model..")
model.fit(x_train_noisy,X_train,validation_data=(x_test_noisy,X_test),epochs=4,batch_size=400)
print("Evaluating the model...")
pred=model.predict(x_test_noisy)

print(f"Shape of predicted data: {pred.shape}")
print(f"Shape of test data: {X_test.shape}")

X_test=numpy.reshape(X_test,(10000,28,28))*255
pred=numpy.reshape(pred,(10000,28,28))*255
x_test_noisy=numpy.reshape(x_test_noisy,(-1,28,28))*255

plt.figure(figsize=(20,4))
print("Test Images")
for i in range(10,20,1):
    plt.subplot(2,10,i+1)
    plt.imshow(X_test[i,:,:],cmap='gray')
    curr_lbl=y_test[i]
    plt.title(f"Label: {curr_lbl}")
plt.show()

plt.figure(figsize=(20,4))
print("Test Images with Noise")
for i in range(10,20,1):
    plt.subplot(2,10,i+1)
    plt.imshow(x_test_noisy[i,:,:],cmap='gray')
    curr_lbl=y_test[i]
    plt.title(f"Label: {curr_lbl}")
plt.show()

plt.figure(figsize=(20,4))
print("Reconstruction of Noisy Test Images")
for i in range(10,20,1):
    plt.subplot(2,10,i+1)
    plt.imshow(pred[i,:,:],cmap='gray')
    curr_lbl=y_test[i]
    plt.title(f"Label: {curr_lbl}")
plt.show()

'''

p9='''
import numpy as np
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def generate_data(samples=1000,features=50):
    np.random.seed(42)
    X=np.random.rand(samples,features)>0.5
    y=(np.sum(X,axis=1)>(features/2)).astype(int)
    return X,y

class StackedRBMs:
    def __init__(self,rbm_layers,rbm_learning_rate=0.1,rbm_n_iter=10):
        self.rbms=[
            BernoulliRBM(n_components=n_components,learning_rate=rbm_n_iter) for n_components in rbm_layers
        ]
        self.logistic_regression=LogisticRegression()
    
    def pretrain(self,X):
        print("Starting unsupervised pretraining with RBMS...")
        current_input=X
        for idx,rbm in enumerate(self.rbms):
            print(f"Training RBM layer {idx+1}/{len(self.rbms)}...")
            rbm.fit(current_input)
            current_input=rbm.transform(current_input)
            
    def fine_tune(self,X,y):
        print("Starting supervised film_tuning with logistic regression")
        for rbm in self.rbms:
            X=rbm.transform(X)
        self.logistic_regression.fit(X,y)
    
    def predict(self,X):
        for rbm in self.rbms:
            X=rbm.transform(X)
        return self.logistic_regression.predict(X)
    
if __name__=="__main__":
    X,y=generate_data()
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
    rbm_layers=[128,64]
    stacked_rbm=StackedRBMs(rbm_layers=rbm_layers,rbm_learning_rate=0.1,rbm_n_iter=50)
    stacked_rbm.pretrain(X_train)
    stacked_rbm.fine_tune(X_train,y_train)
    
    y_pred=stacked_rbm.predict(X_test)
    accuracy=accuracy_score(y_test,y_pred)
    print(f"Test Accuracy:{accuracy*100:.2f}%")

'''