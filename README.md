# KSA Plants Classification ( Binary Classification CNN model ) 
![Triangle Frame Pattern Tumblr Banner](https://user-images.githubusercontent.com/59482214/141875921-19455910-b0c0-4bb0-8881-f2034021c231.png)
#### In this project Deep learning is used  to perform binary classification on two of the KSA flora families. The first is the *Caryophyllaceae* family, which has 45 plants in Saudi Arabia, and the second type is the  *Boraginaceae* family, which has 41 plants.
#### The project aims to accomplish three primary goals:
-  Collecting a data set of images of the widely distributed plants in KSA.
-  Use the dataset to build  binary classification CNN model based on the two most frequent families. 
-  Deploy the model as a web app.
#### Before I go into detail about the goals, I'd want to give you an overview of the project's structure:
capStoneProject
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
