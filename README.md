ABSTRACT:

Digit recognition is the ability of a computer or device to take as input digit from source such as printed physical 
documents, pictures and other devices. It also can use digit as a direct input to a touch screen and then interpret it as text.
This is useful as it allows the user to quickly write down number and text to the devices. 
There are many applications for digit recognition are available this day. There are many technique that have been 
developed to recognize the digit. One of them is Optical Character Recognition (OCR).
OCR will read text from scanned document and translating the images into a form that computer can manipulate it.
In this project I have used three (3) classification algorithm to recognize the digit which are:
i): Support Vector Machine (SVM)
ii): K-Nearest Neighbor (KNN) 
iii): Convolution Neural Network (CNN) . 

 

DATASET: 

I have used MNIST dataset for training and evaluation for classification. 
MNIST problem is a dataset for evaluating machine learning models on the handwritten digit classification problem. 
The dataset was constructed from a number of scanned document dataset available from the 
National Institute of Standards and Technology (NIST). Each image in this dataset is a 28 by 28 pixel square (748 pixels total).
There are 70000 images in the dataset out of which I’ve taken 60000 for model training and 10000 for testing purpose. 

RESULT:

Following result has been observed after training machine on given dataset using above mentioned machine learning algorithms:
using K-NN for n=5 , the accuracy comes out to be 97.189 %.
using SVM with kernel=poly , the accuracy comes out to be 97.839 %.
Using CNN, with 32 filters of 3X3 , the accuracy comes out to be 98.8 %.
 

 
