# Overview

The project deploys a Machine Learning application that predicts house prices in Boston given house attributes, such as house rooms.  The intent of this project is to incorporate Continuous Integration and Continuous Development with Python and Azure DevOps. 

## Project Plan

* A link to a Trello board for the project: https://trello.com/b/OXwAIq3N/ml
* A link to a spreadsheet that includes the original and final project plan> https://docs.google.com/spreadsheets/d/e/2PACX-1vTt4vtQsiF_C0PBh4ODCjn417omVvN1iWzpKynbBROILolDKPzl3tUEDiE8Ss4hoMM8NGUViOTyy37E/pubhtml

## Instructions
 
Architectural Diagram
![DevOps-Project-2](DevOps-Project-2.png)

1. Setup and/or start up the Azure Cloud Shell on Azure Subscription
2. Clone the following Github repository into Cloud Shell instance: https://github.com/gmart009/udacity-azure-devops
3. Go to the local cloned repo in Cloud Shell and run the following command on the shell to setup dev environment with all dependencies and to ensure all tests successfully complete: make all 
![make-all-output](make-all-output.png)
4. make changes to app and push changes to Github, at which point the automatic DevOps pipeline will build and test code, as well as deploy build into App Service plan
5. After deployment is complete, you can locally test code by editing the ./make_predict_azure_app.sh file with the app service name.
6. Run the /make_predict_azure_app.sh script and you should see the following output:
Make Prediction Output
![make-prediction-output](make-prediction-output.png)

Streamed Output
![streamed-output](streamed-output.png)



<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell


* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>


