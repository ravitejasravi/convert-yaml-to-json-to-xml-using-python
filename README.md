# convert-yaml-to-json-to-xml-using-python
converting yaml to json to xml using python in a single web page.

This web application is developed using flask web framework, for this you need to setup certain environment. 

First download the code and open command prompt in project folder, then execute below code.
  
For Windows

                py -3 -m venv venv  

For Mac/Linux

                python3 -m venv venv
                
This will create venv folder within project folder.
Then for activating the environment, run the below code

For Windows 

              venv\Scripts\activate
              
For Mac/Linux

              . venv/bin/activate
              
Then install flask in project environment.
  
              pip install Flask
              
Then install xmltodict module to convert json to xml.
              
              pip install xmltodict

Then install pyyaml module to convert yaml to json.

              pip install PyYAML
              
There you go,, you can run the flask app using below command.

              flask --app hello --debug run
