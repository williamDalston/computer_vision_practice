
import numpy as np

#create a small image that reflects the three color channels

arr_float_3d = np.ones((3,2,4))
print(arr_float_3d)

#download MNIST dataset of handwritten digits

from sklearn import datasets
mnist = datasets.fetch_mldata('MNIST origional')
mnist.data.shape  #contains 70,000 images of 28x28 =784 pixels each
mnist.target.shape