# Assigment 6  
For this assignment we are performing machine learning techniques on a dataset using Pandas.<br/>  
We are also making a simple web-interface using Flask.<br/>  
  
Development environment:<br/>  
 - Ubuntu 18.04 64-bit<br/>  
 - Python 3.7<br/>  
 - IntelliJ IDEA 2019.2.4 (Ultimate Edition)<br/>  
 - Linux 5.2.3-050203-generic<br/>

Before you start, from the root folder (assignment6) run

    pip install . --user
    pip install -r requirements.txt

## Handling the data
This script takes 3 arguments, csv file, first feature and second feature and returns a scatter plot<br/>
image of both training and validation sets.<br/>

    python data.py csv_file first_feat second_feat

**Usage**<br/>
For these examples you need to be in the 'handling_the_data' directory.<br/>

    cd handling_the_data/

To get see the features insulin and age<br/>
run `python data.py ../diabetes.csv insulin age`<br/>
**Expected result**<br/>
![insulin X age validation](handling_data_1.png)
![insulin X age training](handling_data_2.png)<br/>
Or to get features glucose and pregnant<br/>
run `python data.py ../diabetes.csv glucose pregnant`<br/>
Expected result<br/>
![glucose X pregnant validation](handling_data_3.png)
![glucose X pregnant training](handling_data_4.png)<br/>

## Fitting a machine learning model
This script runs the fitting process of machine learning on 3 different feature subsets.<br/>
It does this using 3 different machine learning algorithms K neighbor, Logistic Regression and Support vector machine.<br/>
The script runs with 3, 5 and all features. I have not extended the script for user input.<br/>
**Usage**
For these examples you need to be in the 'fitting_machine_learning_model' directory.<br/>

    cd fitting_machine_learning_model/
   then run `python fitting.py`

**Expected result**<br/>
![accuracy score](fitting_machine_learning_model_1.png)<br/>

## Visualizing the classifier
This script can visualize the classifier when the chosen feature subset has only 2 features.<br/>
This script is also not extended for user input.<br/>
The script uses these classifiers
- insulin and age
- glucose and pregnant
- triceps and pressure

**Usage**
For these examples you need to be in the 'visualizing_the_classifier' directory.<br/>

    cd visualizing_the_classifier/

then run `python visualize.py`<br/>
**Expected result**<br/>
![insulin X age](visualizing_the_classifier_1.png)
![glucose X pregnant](visualizing_the_classifier_2.png)
![triceps X pressure](visualizing_the_classifier_3.png)<br/>

## Visualization through a web app
This script uses Flask to run a simple web-interface showing the results of 'Fitting a machine learning model' and 'Visualizing the classifier'<br/>
**Usage**
For these examples you need to be in the 'visualization_through_web_app' directory.<br/>

    cd visualization_through_web_app/
Then to start server run `python web_visualization.py`<br/>
You should then be able to go to localhost:5001 in your browser.<br/>
To close server pres 'ctrl+c'
**Expected result**<br/>
![Terminal](visualization_through_web_app_1.png)
![Web page](visualization_through_web_app_2.png)

## Interactive visualization
Did not have enough time to finish this task

## Documentation and help pages
Fro this task we are making a documentation page auto-generated from our docstrings.<br/>
We where free to chose the tool to do this and have chosen Sphynx.<br/>
The page is already generated.<br/>
**Usage**
To get access to the documentation page you need to start the server as in 'Visualization through a web app'.<br/>
First go to the 'visualization_through_web_app' directory.<br/>

    cd visualization_through_web_app/
Then run the server `python web_visualization.py`<br/>
At the bottom of the page there is a 'Sphinx docs' link<br/>
![Show doc link](docs_1.png)
**Expected result**<br/>
![Documentation page](docs_2.png)
To close server pres 'ctrl+c'