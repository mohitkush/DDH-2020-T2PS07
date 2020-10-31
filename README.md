# DDH-2020-T2PS07
## Github repository for Drug Discovery Hackathon 2020 aming to solve problem statement 07 of track 2 
### **data_pipeline** 
Folder contains a constructed python pipeline to download and update data from clinicaltrials.gov and to make it available for searching in a **mySQL database.** The folder has .py and .ipynb file, choose which ever you are confortable with. Kindly follow the instruction given in the code and also make sure you **do not** have any existing sql database of the same name in MYSQL.
### **rdkit_model.py** 
Is a python code to predict phase for drug molecules in clinicalrials. We used RandomForest Classifier to build the model. Follow the instructions given in the code.It uses RDkit as a library, and there has been issues regarding RDkit running in pip environment. Please use Conda environment or use Google colab, link to code: [click here](https://colab.research.google.com/drive/1sJPYc2bMPgAxIO72o8Z1tCMLH-2hrRfM#scrollTo=ki0TndvXirLA) or go to "https://colab.research.google.com/drive/1sJPYc2bMPgAxIO72o8Z1tCMLH-2hrRfM#scrollTo=ki0TndvXirLA" . I would **highly recommend** you to download and use the GUI that is windows executable file(.exe) generated for this model. Here is the link to download = [click here](https://drive.google.com/drive/folders/1TcaO4G9JROImSbB4ZeqZ7VjiN4lnNx3v?usp=sharing) or go to "https://drive.google.com/drive/folders/1TcaO4G9JROImSbB4ZeqZ7VjiN4lnNx3v?usp=sharing" ## **You must download the whole RDkit_model folder**
### **main_data.csv** 
Contains all the features used for model building. 
 
## Also make sure rdkit_model.py and main_data.csv are in the same directory while runnig the python file.

### **bulk_test_mdoel**
Folder contains both .ipynb and .py file to predict phase of multiple drugs on the same time using their smiles string. Program needs to manually upload test_drugs.csv and main_data.csv file so please download these files before running the program.Again we used RDkit library here so it might not work in pip environment. Run it on Google colab, code link for the same: [click here](https://colab.research.google.com/drive/1dQnaAkyPcspsJPKRMWk-t8IlVc44hOW1?usp=sharing) or go to "https://colab.research.google.com/drive/1dQnaAkyPcspsJPKRMWk-t8IlVc44hOW1?usp=sharing"
### **test_drugs.csv**
Contains a bunch of antiviral drugs tested on the model in **bulk_test_model**
