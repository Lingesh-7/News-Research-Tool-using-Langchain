from dotenv import load_dotenv
import os
import streamlit as st
import pickle
import time
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
# from langchain.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


load_dotenv()

llm=ChatGroq(
    temperature= 0.7,
    model='llama3-8b-8192',
    groq_api_key=os.environ['api_key'],

)

st.title("News Research Tool 📈")

st.sidebar.title("News Article URLS")


urls=[]
for i in range(3):
    url=st.sidebar.text_input(f"URL {i}")
    urls.append(url)
process_url_clicked=st.sidebar.button("Process URL")


main_placefolder=st.empty()


if process_url_clicked:
    #LOAD DATA
    main_placefolder.text("Data Loading..Started...!")
    loader=UnstructuredURLLoader(urls=urls)
    data=loader.load()

    #SPILLITING DATA
    main_placefolder.text("SPLITTING DATA!")
    text_splitter=RecursiveCharacterTextSplitter(separators=['\n\n','\n','.',','],chunk_size=1000)
    docs=text_splitter.split_documents(data)

    #CREATE EMBEDDINGS
    main_placefolder.text("CREATE EMBEDDInG!")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # lightweight and good quality
    vector_index = FAISS.from_documents(docs, embeddings)
    time.sleep(2)
    file_path=r'LangChain\News_reseacher_tools\project\app\n_vector_index.pkl'

    with open(file_path,"wb") as f:
        pickle.dump(vector_index,f)


query=main_placefolder.text_input('Question: ')
if query:
    try:
        file_path=r'LangChain\News_reseacher_tools\project\app\n_vector_index.pkl'
        with open(file_path,'rb') as f:
            vector_store=pickle.load(f)
    except Exception as e:
        print(e)

    chain=RetrievalQAWithSourcesChain.from_llm(llm=llm,retriever=vector_store.as_retriever())
    result=chain({'question':query},return_only_outputs=True)
    print(result)
    answer=result['answer']
    st.header('Answer')
    st.write(answer)

    sources=result['sources']
    if sources:
        st.subheader("Sources:")
        st.write(sources)
        # for source in sources:
            