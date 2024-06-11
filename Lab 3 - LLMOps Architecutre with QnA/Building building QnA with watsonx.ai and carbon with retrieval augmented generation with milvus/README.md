# Building Apps with watsonx.ai and Carbon
This repository contains code from a webapp that uses Flask Python as the backend and vanilla Java Script, HTML, CSS as the front-end.
The front-end also uses an open source HTML web component created by IBM, called [Carbon](https://web-components.carbondesignsystem.com/?path=/docs/introduction-welcome--page).
This application allows you to conduct questions and answers using your own documents with the help of the LLM Model. The method used for this is called
[RAG](https://research.ibm.com/blog/retrieval-augmented-generation-RAG).


Try directly the application that has been deployed [Here](https://rag-qna.1gmk3v763a4v.us-south.codeengine.appdomain.cloud/rag#)

## How does this app work? 🚀
This application allows users to conduct questions and answers with LLM regarding uploaded documents. The following are the capabilities of this application:
1. Users can upload documents to knowledge repositories such as Milvus and Watson Discovery.
2. Users can ask questions by selecting LLM model, knowledge repository. Users can activate the streaming feature to get answers streaming. If streaming is disabled additional information regarding the time required for retrieval and generation will be displayed.

### Sample Questions
The following are examples of questions about whether the application is running properly.
- What is the retirement age?
- What clothes do employees wear on Wednesday?
- What are the THR rules?
Try asking other questions whose answers may or may not be documented.


### Examples of documents that can be uploaded
You can use your own documentation to test RAG capabilities using different LLM models, or different knowledge repositories.
Here are some documents that are already available in Milvus and Watson Discovery:
- [Maitenance Manual](https://github.ibm.com/Fadly-Hidayat/watsonx-llmops-vn/blob/main/Lab%203%20-%20LLMOps%20Architecutre%20with%20QnA/Document%20Sources/Maintenance-Manual.pdf)
- [Paper Flowers](https://github.ibm.com/Fadly-Hidayat/watsonx-llmops-vn/blob/main/Lab%203%20-%20LLMOps%20Architecutre%20with%20QnA/Document%20Sources/paper_flowers.pdf)

You can also use this document if you want.
- [Singapore Court Cases](https://github.ibm.com/Fadly-Hidayat/watsonx-llmops-vn/blob/main/Lab%203%20-%20LLMOps%20Architecutre%20with%20QnA/Document%20Sources/singapore-court-case1.pdf)
- [Singapore Court Case 2](https://github.ibm.com/Fadly-Hidayat/watsonx-llmops-vn/blob/main/Lab%203%20-%20LLMOps%20Architecutre%20with%20QnA/Document%20Sources/singapore-court-case2.pdf)  

Download this document and upload it to the watson discovery


## Requirements 🚀
### Technology that can be used
To build this webapp several SDKs are used to enable interaction with the required technology or services.
1. [watsonx.ai python SDK](https://ibm.github.io/watsonx-ai-python-sdk/)
2. [Milvus python SDK](https://milvus.io/api-reference/pymilvus/v2.4.x/About.md)
3. [Watson Discovery python SDK](https://github.com/watson-developer-cloud/python-sdk/blob/master/ibm_watson/discovery_v2.py)

Apart from using the SDK, we can actually also use the API. Below are documentation links for several APIs that you may find useful.
- [watsonx.ai API Documentation](https://cloud.ibm.com/apidocs/watsonx-ai)
- [Watson Discovery API Documentation](https://cloud.ibm.com/apidocs/discovery-data?code=python)
  
### Credentials that must be provided
So that this web application can be run properly on a local computer or in a Docker container, you must prepare the following credentials and secrets.
- watsonx.ai APIKEY
- watsonx.ai PROJECT_ID
- watsonx.ai URL
- Watson Discovery APIKEY
- Watson Discovery PROJECT_ID
- Watson Discovery URL
- Milvus Host
- Milvus Port
- Milvus Password 
  
## How to get started 🚀
There are several ways to deploy the code in this repository to become an interoperable webapp.
First, you can run the code on your local computer. The second way, you can deploy it with Docker Container.
Using Docker containers is profitable because they can be deployed anywhere easily.

### Running on Local Computer
1. Open the terminal, cd into the Lab 4 directory.
2. create python virtual environment, here is an example if you want to create a virtual environment called 'genai'
```
python -m venv genai
```  

3. activate the python virtual environment that was just created
```
source genai\bin\activate
```  

4. install the dependencies in requirements.txt
```
python -m pip install -r requirements.txt
```  

5. Export secret and credentials by replacing all values ​​in the double quote with your credentials. Paste the command in the terminal.  
```
export WX_API_KEY="IAM-APIKEY"
export WX_PROJECT_ID="WATSONXAI-PROJECT-ID"
export WX_URL="WATSONXAI-URL"
export WD_API_KEY="WATSON-DISCOVERY-APIKEY"
export WD_PROJECT_ID="WATSON-DISCOVERY-PROJECT-ID"
export WD_URL="WATSON-DISCOVERY-INSTANCE-URL"
export milvus_host="MILVUS-HOST"
export milvus_port="LISTEN-TO-PORT"
export milvus_password="MILVUS-PASSWORD"
```    

6. cd to the app folder and run the application
```
cd app
python main.py
```  
7. Open local `127.0.0.0:8080` or the IP that appears in the terminal after the application is run.


### Running using Docker Container

1. Open the terminal, cd into the Lab 4 directory.
2. Build docker image using docker file
```
docker build -t qna .
```  
3. Run docker container dengan menjadikan credentials dan secret sebagai environment variable.
```
docker run --env "WX_API_KEY=IAM-APIKEY" \
--env "WX_PROJECT_ID=WATSONXAI-PROJECT-ID" \
--env "WX_URL=WATSONXAI-URL" \
--env "WD_API_KEY=WATSON-DISCOVERY-APIKEY" \
--env "WD_PROJECT_ID=WATSON-DISCOVERY-PROJECT-ID" \
--env "WD_URL=WATSON-DISCOVERY-INSTANCE-URL" \
--env "milvus_host=MILVUS-HOST" \
--env "milvus_port=LISTEN-TO-PORT" \
--env "milvus_password=MILVUS-PASSWORD" \
-p 8080:8080 --name qna-container qna
```  
4. Open the deployment URL.

