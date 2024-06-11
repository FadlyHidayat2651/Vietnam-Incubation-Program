import json
import requests
import ast, os
import pandas as pd
import time

from ibm_watson import DiscoveryV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

import logging
import numpy as np
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from sentence_transformers import SentenceTransformer
from pymilvus import CollectionSchema, FieldSchema, DataType, Collection
from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)

#Creds related to watson discovery
WD_API_KEY = os.environ['WD_API_KEY']
WD_PROJECT_ID = os.environ['WD_PROJECT_ID']
WD_URL = os.environ['WD_URL'] 
WD_COLLECTION_ID = os.environ['WD_COLLECTION_ID']

#Creds related to watsonx.ai
WX_API_KEY = os.environ['WX_API_KEY']
WX_URL = os.environ['WX_URL']  
WX_PROJECT_ID = os.environ['WX_PROJECT_ID']

#Creds related to Milvus
milvus_host = os.environ['milvus_host']
milvus_port = os.environ['milvus_port']
milvus_password = os.environ['milvus_password']

creds = {
    "url": WX_URL,
    "apikey": WX_API_KEY 
}

cert="""-----BEGIN CERTIFICATE-----
MIIDzzCCAregAwIBAgIUHvv3+lYxL4ZyBS6R9qD0D9pqfaIwDQYJKoZIhvcNAQEL
BQAwdzELMAkGA1UEBhMCR0IxDzANBgNVBAgMBkxvbmRvbjESMBAGA1UEBwwJWW9y
ayBSb2FkMRswGQYDVQQKDBJDbGllbnQgRW5naW5lZXJpbmcxEjAQBgNVBAsMCUFT
IGFuZCBQVzESMBAGA1UEAwwJbG9jYWxob3N0MB4XDTIzMDgxMDE1MDIwMVoXDTMz
MDgwNzE1MDIwMVowdzELMAkGA1UEBhMCR0IxDzANBgNVBAgMBkxvbmRvbjESMBAG
A1UEBwwJWW9yayBSb2FkMRswGQYDVQQKDBJDbGllbnQgRW5naW5lZXJpbmcxEjAQ
BgNVBAsMCUFTIGFuZCBQVzESMBAGA1UEAwwJbG9jYWxob3N0MIIBIjANBgkqhkiG
9w0BAQEFAAOCAQ8AMIIBCgKCAQEAw5GJ9I0yB+FD53ro7tQnPWlMfMfO9jOojztA
EIyVFgFhoZ+CZJH+3y1e2GZm7a3wIbQS6f0Y1rZGMktAq+8UPASMSarVraiWYsrL
4znFboNFRJ2wInnPlYJis6lbCffahHzE+ye3Mx6zeSQAijImCRtaCCwZzD93kVFB
MDFHQGAEwga5plAgHhkfpXrqrzVRq1idNiojj0PRSofhb0ywWbGyjTlbC7u6odcH
as78+S6SbXHM5AqAqfTMRPZKrRmphEDYYGNG+VBfUuVI6vqd3fS7xA0AImZ7j/CW
QbFdh9TLXl+D5dVToykIgFdjtkez93ORG1HYskrZnVlGObgOnwIDAQABo1MwUTAd
BgNVHQ4EFgQUZEW3JzZOej4jLgbKcmn/t9IYQ58wHwYDVR0jBBgwFoAUZEW3JzZO
ej4jLgbKcmn/t9IYQ58wDwYDVR0TAQH/BAUwAwEB/zANBgkqhkiG9w0BAQsFAAOC
AQEAZIwIRF7Wdx/QuseV13ALfZRjHWkFHaYLgUjXW+rIyCUEr1Iu421PF/CEJKMb
kQ3T+DGDBPjrWlTxQFAJoVpvsbVeaM6qRsqHe1z9xJ4tHYYUKwdeAJl5lnrGD027
HPP0qAUvm+D2NepMOJyomktB8J8TOS+2KWpot0HZtteFP4S53Lo7+tOu9374fF/2
eg/QZkZzKaiQhcnFir7etyQBBFvo4gXXHgo884hYA8DltGpA3zlIIkTKeftafjQ+
jyAnDpq+rQ3hfKMhjeC1ATausae6td6VRP55ZfOrM4t+DEbrmh/WGM3NzzMjf91M
b8a2Cp2o7BLIPi8LwWfkQM+4dQ==
-----END CERTIFICATE-----"""

with open("cert-milvus.pem", "w") as file:
    file.write(cert)


def get_mime_type(filepath):
    _, extension = os.path.splitext(filepath)
    mime_type_map = {
      ".json": "application/json",
      ".doc": "application/msword",
      ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
      ".pdf": "application/pdf",
      ".html": "text/html",
      ".xhtml": "application/xhtml+xml",}
    return mime_type_map.get(extension.lower(), None)


##==========================Watson Discovery Sample================================
def wd_auth(WD_PROJECT_ID=WD_PROJECT_ID, WD_API_KEY=WD_API_KEY, WD_URL=WD_URL):
    authenticator = IAMAuthenticator(WD_API_KEY) 
    discovery = DiscoveryV2(
            version='2019-04-30',
            authenticator=authenticator
        )
    discovery.set_service_url(WD_URL)

    collections = discovery.list_collections(project_id=WD_PROJECT_ID).get_result()
    collection_list = list(pd.DataFrame(collections['collections'])['collection_id'])
    return discovery, collection_list
   

def load_docs(filepath, WD_PROJECT_ID=WD_PROJECT_ID,):
    discovery, collection_list = wd_auth(WD_PROJECT_ID)
    collection_id = collection_list[0]
    filename = os.path.basename(filepath)
    mime_type = get_mime_type(filename)
    with open(filepath,'rb') as fileinfo:
        response = discovery.add_document(
            project_id=WD_PROJECT_ID,
            collection_id=collection_id,
            file=fileinfo,
            filename=filename,
            file_content_type=mime_type
        ).get_result()
        output = json.dumps(response, indent=2)
    return output


def query_docs(keyword, WD_PROJECT_ID=WD_PROJECT_ID,  WD_COLLECTION_ID = WD_COLLECTION_ID):
    discovery, collection_list = wd_auth()
    collection_list_final = [WD_COLLECTION_ID]
    query_result = discovery.query(
                project_id=WD_PROJECT_ID,
                collection_ids=collection_list_final,
                passages={'characters':2000},
                natural_language_query=keyword).get_result(),
    try:
        passage = query_result[0]['results'][0]['text'][0] #get whole text
        #passage = query_result[0]['results'][0]['document_passages'][0]['passage_text'] #get n characters of passage
        passage = "  ".join([line.strip() for line in passage.split("\n") if line.strip() != ""])
    except:
        passage = "no information found"
    return passage


##====================================milvus=======================================
print("=== start connecting to Milvus ===")
connections.connect("default", host=milvus_host,
                    port=milvus_port, secure=True, server_pem_path="cert-milvus.pem",
                    server_name="localhost",user="root",
                    password=milvus_password)


def create_collection(
    milvus_connection_alias: str = "default",
    collection_name: str = "ggf_collection"
    ) -> None:
    # Defining the default collection schema
    idx = FieldSchema(
        name = "id",
        description = "Embedding ID",
        dtype = DataType.INT64,
        is_primary = True,
        auto_id = True,
    )
    embedding_vector = FieldSchema(
        name = "embedding_vector",
        description = "Embedding vector",
        dtype = DataType.FLOAT_VECTOR,
        dim = 384,
    )
    embedding_raw = FieldSchema(
        name = "embedding_raw",
        description = "Embedding raw value",
        dtype = DataType.VARCHAR,
        max_length = 65535,
    )
    document_id = FieldSchema(
        name = "document_id",
        description = "Document ID",
        dtype = DataType.VARCHAR,
        max_length = 256
    )
    metadata = FieldSchema(
        name = "metadata_json",
        description = "Metadata in JSON format",
        dtype = DataType.VARCHAR,
        max_length = 65535
    )
    default_schema = CollectionSchema(
        fields = [
            idx,
            embedding_vector,
            embedding_raw,
            document_id,
            metadata
        ],
        description = "Default collection schema",
        enable_dynamic_field = True
    )
    logging.debug("Collection schema defined.")

    # Creating the default collection
    Collection(
        name = collection_name,
        schema = default_schema,
        using = milvus_connection_alias,
        shards_num = 2,
    )
    
def embed_pdf_text(
    document_id: str,
    file_path: str,
    milvus_connection_alias: str = "default",
    collection_name: str = "collection",
    hf_model_id: str = 'sentence-transformers/all-MiniLM-L6-v2'
    ):
    # Loading text from pdf document
    loader = PyPDFLoader(file_path)
    text_splitter = CharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 100
    )
    docs = loader.load_and_split(
        text_splitter = text_splitter
    )

    # Embedding text in 'data' variable
    model = SentenceTransformer(hf_model_id)
    data = [
        [model.encode(doc.page_content) for doc in docs],
        [doc.page_content for doc in docs],
        [document_id for doc in docs],
        ["{}" for doc in docs]
    ]
    logging.debug("Text was successfully embedded from PDF {}.".format(file_path))

    # store the data in Milvus collection
    collection = Collection(
        name = collection_name,
        using = milvus_connection_alias
    )
    collection.insert(data)

def build_vector_index(
    milvus_connection_alias: str = "default",
    collection_name: str = "collection"
):
    # Parameters of the index being created
    index_params = {
        "metric_type":"L2",
        "index_type":"IVF_FLAT",
        "params":{"nlist":1024}
        }
    
    collection = Collection(
        name = collection_name,
        using = milvus_connection_alias
    )

    # Create an index from the embeddings vectors
    collection.create_index(
        field_name = "embedding_vector",
        index_params = index_params
    )

def build_vector_index(
    milvus_connection_alias: str = "techzone_connection",
    collection_name: str = "default_collection"
):
    # Parameters of the index being created
    index_params = {
        "metric_type":"L2",
        "index_type":"IVF_FLAT",
        "params":{"nlist":1024}
        }
    
    collection = Collection(
        name = collection_name,
        using = milvus_connection_alias
    )

    # Create an index from the embeddings vectors
    collection.create_index(
        field_name = "embedding_vector",
        index_params = index_params
    )

def similarity_search(
    user_question: str,
    limit=3,
    milvus_connection_alias: str = "default",
    collection_name: str = "workhsop_collection",
    hf_model_id: str = 'sentence-transformers/all-MiniLM-L6-v2'
    ) -> list:

    # Search parameters
    search_params = {
        "metric_type": "L2", 
        "offset": 0, 
        "ignore_growing": False, 
        "params": {"nprobe": 10}
    }

    collection = Collection(
        name = collection_name,
        using = milvus_connection_alias
    )
    collection.load()
    logging.debug("Collection loaded.")

    # Embedding model
    model = SentenceTransformer(hf_model_id)
    logging.debug("Embedding model loaded.")

    # Search the index for the 3 closest vectors
    results = collection.search(
        data = [model.encode(user_question)],
        anns_field = "embedding_vector",
        param = search_params,
        limit = limit,
        expr = None,
        output_field = ['title'],
        consistency_level = "Strong"
    )

    # Retrieving the text associated with the results ids
    results_text = collection.query(
        expr = "id in {}".format(results[0].ids), 
        output_fields = ["id", "embedding_raw", "document_id", "metadata_json"],
        consistency_level="Strong"
    )
    collection.release()
    logging.debug("Text chunks succesfully retrieved.")

    return results_text


##==================================watsonx.ai===================================== 
def send_to_watsonxai(prompt, creds=creds, project_id=WX_PROJECT_ID,
                    model_name='meta-llama/llama-3-70b-instruct', #'mistralai/mixtral-8x7b-instruct-v01',', #'meta-llama/llama-2-13b-chat', #
                    decoding_method="greedy",
                    max_new_tokens=300,
                    min_new_tokens=1,
                    temperature=0,
                    repetition_penalty=1.0,
                    stop_sequences=[],
                    ):
    '''
   helper function for sending prompts and params to Watsonx.ai
    
    Args:  
        prompts:list list of text prompts
        decoding:str Watsonx.ai parameter "sample" or "greedy"
        max_new_tok:int Watsonx.ai parameter for max new tokens/response returned
        temperature:float Watsonx.ai parameter for temperature (range 0>2)
        repetition_penalty:float Watsonx.ai parameter for repetition penalty (range 1.0 to 2.0)

    Returns: None
        prints response
    '''

    assert not any(map(lambda prompt: len(prompt) < 1, prompt)), "make sure none of the prompts in the inputs prompts are empty"

    # Instantiate parameters for text generation
    model_params = {
        GenParams.DECODING_METHOD: decoding_method,
        GenParams.MIN_NEW_TOKENS: min_new_tokens,
        GenParams.MAX_NEW_TOKENS: max_new_tokens,
        GenParams.RANDOM_SEED: 42,
        GenParams.TEMPERATURE: temperature,
        GenParams.REPETITION_PENALTY: repetition_penalty,
        GenParams.STOP_SEQUENCES: stop_sequences
    }

    # Instantiate a model proxy object to send your requests
    model = Model(
        model_id=model_name,
        params=model_params,
        credentials=creds,
        project_id=project_id)
    
    
    output = model.generate_text(prompt)
    return output


def send_to_watsonxai_stream(prompt, creds=creds, project_id=WX_PROJECT_ID,
                    model_name='meta-llama/llama-3-70b-instruct', #'mistralai/mixtral-8x7b-instruct-v01',', #'meta-llama/llama-2-13b-chat', #
                    decoding_method="greedy",
                    max_new_tokens=300,
                    min_new_tokens=1,
                    temperature=0,
                    repetition_penalty=1.0,
                    stop_sequences=[],
                    ):
    '''
   helper function for sending prompts and params to Watsonx.ai
    
    Args:  
        prompts:list list of text prompts
        decoding:str Watsonx.ai parameter "sample" or "greedy"
        max_new_tok:int Watsonx.ai parameter for max new tokens/response returned
        temperature:float Watsonx.ai parameter for temperature (range 0>2)
        repetition_penalty:float Watsonx.ai parameter for repetition penalty (range 1.0 to 2.0)

    Returns: None
        prints response
    '''

    assert not any(map(lambda prompt: len(prompt) < 1, prompt)), "make sure none of the prompts in the inputs prompts are empty"

    # Instantiate parameters for text generation
    model_params = {
        GenParams.DECODING_METHOD: decoding_method,
        GenParams.MIN_NEW_TOKENS: min_new_tokens,
        GenParams.MAX_NEW_TOKENS: max_new_tokens,
        GenParams.RANDOM_SEED: 42,
        GenParams.TEMPERATURE: temperature,
        GenParams.REPETITION_PENALTY: repetition_penalty,
        GenParams.STOP_SEQUENCES: stop_sequences
    }

    # Instantiate a model proxy object to send your requests
    model = Model(
        model_id=model_name,
        params=model_params,
        credentials=creds,
        project_id=project_id)
    
    output = model.generate_text_stream(prompt)
    # output = model.generate_text(prompt) # This is for not streaming
    for chunk in output:
        yield chunk
   


def query_wxai(user_question, db_selection, llm_model, streaming=False):
    print(user_question)
    start_time = time.time()

    if  db_selection == 'wd':
        passage = query_docs(user_question)
        print(passage)
    else:
        collection_name = "collection"
        passage = similarity_search(user_question, milvus_connection_alias="default", collection_name=collection_name, limit=3)
        print(passage)
    
    eta_retrieve = time.time() - start_time
    print(db_selection, " eta_retrieve: ", eta_retrieve)

    prompt = f"""You are a helpful, polite and honest assistant. Always answer as best you can in a helpful way, while staying safe. Your answers must not contain harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Make sure that your response is socially impartial and positive.
     Context:{passage}
     Question:{user_question}
     Please understand the context and answer questions based only on the information provided. Answer questions clearly, completely, informatively.
     Identify and extract URLs mentioned in context if they relate to the question. Don't include unrelated URLs in your answer.
     Give answers in sequence if necessary or provide a clear and concise list. If a question doesn't make sense or is factually incoherent, explain why rather than answering something that is not true.
     If you don't know the answer to a question, please do not provide false information. If the context has nothing to do with the question, just answer you don't know. Answer only based on context.\nGive the Answer in the same language as the Question.
     For example, if the Question is in English, then answer in English; If the Question is in Mandarin, then write the Answer in Mandarin.
     Answer:"""

    print("streaming =", streaming)

    if streaming:
        return send_to_watsonxai_stream(prompt, model_name=llm_model, creds=creds, project_id=WX_PROJECT_ID)

    else:
        result = send_to_watsonxai(prompt, model_name=llm_model, creds=creds, project_id=WX_PROJECT_ID)
        eta_wx = time.time() - start_time
        print(llm_model, " eta_wx: ", eta_wx-eta_retrieve)
        return result, eta_retrieve, eta_wx-eta_retrieve
         


    
