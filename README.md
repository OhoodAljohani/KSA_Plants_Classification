# KSA Plants Classification ( Binary Classification CNN model ) 
#### In this project Deep learning is used  to perform binary classification on two of the KSA flora families. The first is the *Caryophyllaceae* family, which has 45 plants in Saudi Arabia, and the second type is the  *Boraginaceae* family, which has 41 plants.
#### The project aims to accomplish three primary goals:
-  Collecting a data set of images of the widely distributed plants in KSA.
-  Use the dataset to build  binary classification CNN model based on the two most frequent families. 
-  Deploy the model as a web app.
#### Before I go into detail about the goals, I'd want to give you an overview of the project's structure:
1. The scrape file is jupyter-notebook and the script will colloct plants names and use it as search-words in https://www.google.com/imghp?hl=en . It resulted in collecting 4343 images. 
2. data/images file is the directory to the collected images.
3. EDA file is jupyter-notebook and the script will answer questions about the data balance, average image, color palette, and sizes.
4. data_agumatution jupyter-notebook and the script will generate images from the two classes (Caryophyllaceae and Boraginaceae). 
5. train jupyter-notebook and the script will build and train cnn model. 
6. model this directory holds the saved model. 
7. app is python file and the script will build flask app.
8. templates folder holds the app interface main.html. 
9. dependencey is jupyter-notebook and the script prints the most important packages versions 
``` bash
KSA_Plants_Classification
|–– main
|–– scrape.ipynb
|–– EDA.ipynb
|–– scrape.ipynb
|-- data_agumatution.ipynb
|–– train.ipynb
|–– data
|  |–– data.csv
|  |–– train.csv
|  |–– test.csv
|  |–– images
|  |  |–– ACANTHACEAE
|  |  |–– AIZOACEAE
|  |  |–– ALLIACEAE
|  |  |–– ALOACEAE
|  |  |–– AMARANTHACEAE
|  |  |–– AMARYLLIDACEAE
|  |  |–– ANACARDIACEAE
|  |  |–– APOCYNACEAE
|  |  |–– ARISTOLOCHIACEAE
|  |  |–– ASCLEPIADACEAE
|  |  |–– ASPARAGACEAE
|  |  |–– ASPHODELACEAE
|  |  |–– BARBEYACEAE
|  |  |–– BERBERIDACEAE
|  |  |–– BORAGINACEAE
|  |  |–– BURSERACEAF
|  |  |–– CACTACEAE
|  |  |–– CAMPANULACEAE
|  |  |–– CAPPARACEAE
|  |  |–– CAPRIFOLIACEAE
|  |  |–– CARYOPHYLLACEAE
|–– dependencey
|  |–– versions.ipynb
|–– model
|  |–– flora.h5
|–– plots
|–– static
|  |–– css
|–– templates
|  |–– main.html
``` 
# 1. Collocting The dataset :
![Triangle Frame Pattern Tumblr Banner](https://user-images.githubusercontent.com/59482214/141875921-19455910-b0c0-4bb0-8881-f2034021c231.png)

#### The dataset contains 4,343 images - after data agumatution 7021 images. It has two columns, the first column *Label* is the name of the plant family, and the second !
*img* is nummpy array of the image. 
- Image sizes range from 1*1 to 2816*1880 pixle. 
- The labels are distributed as follows: 
![imagesperfamily](https://user-images.githubusercontent.com/59482214/141881777-9dd5304f-9efa-4f1d-bfa2-768a2cf16331.png)
- Example of one images is : From the BARBEYACEAE Family 
![BARBEYACEAE Family](https://user-images.githubusercontent.com/59482214/141881961-ede286d2-4c04-4ae4-8381-8b036b77fb1d.png)
# 2. CNN model :
- The CNN model structure is as following : 
```
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 32, 32, 32)        896       
                                                                 
 activation (Activation)     (None, 32, 32, 32)        0         
                                                                 
 conv2d_1 (Conv2D)           (None, 30, 30, 32)        9248      
                                                                 
 conv2d_2 (Conv2D)           (None, 28, 28, 64)        18496     
                                                                 
 activation_1 (Activation)   (None, 28, 28, 64)        0         
                                                                 
 max_pooling2d (MaxPooling2D  (None, 14, 14, 64)       0         
 )                                                               
                                                                 
 conv2d_3 (Conv2D)           (None, 14, 14, 64)        36928     
                                                                 
 activation_2 (Activation)   (None, 14, 14, 64)        0         
                                                                 
 conv2d_4 (Conv2D)           (None, 12, 12, 64)        36928     
                                                                 
 conv2d_5 (Conv2D)           (None, 10, 10, 64)        36928     
                                                                 
 conv2d_6 (Conv2D)           (None, 8, 8, 64)          36928     
                                                                 
 activation_3 (Activation)   (None, 8, 8, 64)          0         
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 4, 4, 64)         0         
 2D)                                                             
                                                                 
 flatten (Flatten)           (None, 1024)              0         
                                                                 
 dense (Dense)               (None, 32)                32800     
                                                                 
 activation_4 (Activation)   (None, 32)                0         
                                                                 
 dense_1 (Dense)             (None, 1)                 33        
                                                                 
=================================================================
Total params: 209,185
Trainable params: 209,185
Non-trainable params: 0
_________________________________________________________________
```
- The CNN model accuracy is : 0.6723 , The model was unstable and the accuracy is low, I believe the model didn't generalize. 
### Limitation : 
- The Dataset Gathering produced a poor group of photos.
- Classification difficulties were caused by the Dataset Size.
- Domain of Knowledge: I had limited experience with the subject, which caused the process to be delayed.
### Future Work 
#### n the future, I would search for a specialist supervisor and would make sure that all of the data was collected in the best way. I would strongly consider the Use of ensemble learning and  transfer learning.

### Conclusion:
#### The data from the KSA flora photos was obtained and utilized to perform binary classification of the two most well-known species. For a variety of factors, the model fell short. There were several hurdles throughout the development process, particularly in the data collation and model training stages. The accuracy of the model is 67 percent, indicating that it did not generalize effectively.
