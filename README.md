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
# 1.Collocting The dataset :
![Triangle Frame Pattern Tumblr Banner](https://user-images.githubusercontent.com/59482214/141875921-19455910-b0c0-4bb0-8881-f2034021c231.png)

