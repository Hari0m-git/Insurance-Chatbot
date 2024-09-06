#1
# import streamlit as st
# import os
# from langchain_ai21 import ChatAI21, AI21Embeddings
# from langchain_community.vectorstores import Chroma
# from langchain.prompts import PromptTemplate
# from ai21 import AI21Client
# from ai21.models.chat import ChatMessage
# from dotenv import load_dotenv

# # Load environment variables from the .env file
# load_dotenv()

# # Initialize the AI21 embeddings
# api_key = os.getenv("AI21_API_KEY")
# if not api_key:
#     st.error("AI21_API_KEY environment variable is not set.")
#     st.stop()

# embedding = AI21Embeddings(api_key=api_key)

# # Load or create the vector database
# db_folder = 'db'
# vectordb = None

# # # Check if the vector database exists
# # if os.path.exists(os.path.join(db_folder, 'index')):
# #     vectordb = Chroma(persist_directory=db_folder, embedding_function=embedding)
# #     st.write("Vector database loaded successfully.")
# # else:
# #     st.error("No existing vector database found. Please create one first.")
# #     st.stop()

# import os


# # Check for any expected file in the db_folder
# if any(os.path.isfile(os.path.join(db_folder, f)) for f in os.listdir(db_folder)):
#     vectordb = Chroma(persist_directory=db_folder, embedding_function=embedding)
#     st.write("Vector database loaded successfully.")
# else:
#     st.error("No existing vector database found. Please create one first.")


# # Define the improved prompt template
# PROMPT_TEMPLATE = """
# You are an AI assistant specialized in explaining insurance policies. Your task is to answer the user's question based on the following context from an insurance policy:

# {context}

# Question: {question}

# Please provide a clear, concise, and easy-to-understand answer. Follow these guidelines:
# 1. Limit your response to the most important points to ensure clarity and brevity.
# 2. Identify the key conditions or points relevant to the question.
# 2. Use Headings and Subheadings wherever possible. 
# 3. If a term is complex, provide a simple explanation in parentheses.
# 4. Use bullet points only when needed. Explain each point briefly.
# 5. If the context doesn't fully answer the question, mention this and provide the most relevant information available.

# Remember, your goal is to help an insurance expert understand the key points of the policy.
# """
# prompt = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["context", "question"])

# # Initialize the AI21 client
# client = AI21Client(api_key=api_key)

# # Streamlit app layout
# st.title("Insurance Chatbot")
# st.write("Ask any questions related to the insurance policies.")

# # Memory to store previous interactions
# if "history" not in st.session_state:
#     st.session_state.history = []

# def get_relevant_context(question, k=5):
#     results = vectordb.similarity_search(question, k=k)
#     context = "\n".join([doc.page_content for doc in results])
#     return context

# def answer_question(question):
#     context = get_relevant_context(question)
#     full_prompt = prompt.format(context=context, question=question)
    
#     messages = [
#         ChatMessage(role="system", content="You are an AI assistant specialized in insurance policies. Answer questions as best as you can based only on the provided context."),
#         ChatMessage(role="user", content=full_prompt)
#     ]
    
#     response = client.chat.completions.create(
#         model="jamba-1.5-mini",
#         messages=messages,
#         max_tokens=500,
#         timeout=30  # Set a 30-second timeout
#     )
    
#     return response.choices[0].message.content

# # Chatbot interaction
# user_input = st.text_input("Your question:")
# if user_input:
#     response = answer_question(user_input)
#     st.session_state.history.append({"question": user_input, "answer": response})

# # Display conversation history
# if st.session_state.history:
#     for i, interaction in enumerate(st.session_state.history):
#         st.write(f"**You:** {interaction['question']}")
#         st.write(f"**InsureBot:** {interaction['answer']}")

# #To run: streamlit run insurance_chatbot.py

# #2
# #Works Perfectly
# import streamlit as st
# import os
# from langchain_ai21 import ChatAI21, AI21Embeddings
# from langchain_community.vectorstores import Chroma
# from langchain.prompts import PromptTemplate
# from ai21 import AI21Client
# from ai21.models.chat import ChatMessage
# from dotenv import load_dotenv

# # Set page configuration at the top
# st.set_page_config(page_title="Insurance Chatbot", page_icon=":robot_face:", layout="wide")

# # Load environment variables from the .env file
# load_dotenv()

# # Initialize the AI21 embeddings
# api_key = os.getenv("AI21_API_KEY")
# if not api_key:
#     st.error("AI21_API_KEY environment variable is not set.")
#     st.stop()

# embedding = AI21Embeddings(api_key=api_key)

# # Load or create the vector database
# db_folder = 'db'
# vectordb = None

# # Check for any expected file in the db_folder
# if any(os.path.isfile(os.path.join(db_folder, f)) for f in os.listdir(db_folder)):
#     vectordb = Chroma(persist_directory=db_folder, embedding_function=embedding)
#     st.success("Vector database loaded successfully.")
# else:
#     st.error("No existing vector database found. Please create one first.")
#     st.stop()

# # Define the improved prompt template
# # PROMPT_TEMPLATE = """
# # You are an AI assistant specialized in explaining insurance policies. Your task is to answer the user's question based on the following context from an insurance policy:

# # {context}

# # Question: {question}

# # Please provide a clear, concise, and easy-to-understand answer. Follow these guidelines:
# # 1. Limit your response to the most important points to ensure clarity and brevity.
# # 2. Identify the key conditions or points relevant to the question.
# # 3. Use Headings and Subheadings wherever possible. 
# # 4. If a term is complex, provide a simple explanation in parentheses.
# # 5. Use bullet points only when needed. Explain each point briefly.
# # 6. If the context doesn't fully answer the question, mention this and provide the most relevant information available.

# # Remember, your goal is to help an insurance expert understand the key points of the policy.
# # """

# PROMPT_TEMPLATE = """
# You are an AI assistant specialized in explaining insurance policies. Your task is to answer the user's question based on the following context from an insurance policy:

# {context}

# Question: {question}

# Please provide a detailed yet concise answer by following these guidelines:

# 1. **Relevant Details**: Include all critical and relevant points directly related to the question.
# 2. **Clarity**: Use simple language and avoid jargon where possible. If complex terms are necessary, provide a brief explanation in parentheses.
# 3. **Key Information**: Focus on the main points, but ensure no important information is left out.
# 4. **Structure**: Use bullet points or numbered lists only when necessary for clarity. Keep the response structured with headings and subheadings.
# 5. **Length**: Ensure the response is informative but avoid unnecessary elaboration. The goal is to provide a clear, complete, and concise answer.
# 6. **Truthfulness**: If the context doesn't fully answer the question, mention this and provide the most relevant information available.

# Keep the response accurate and easy to understand.
# """


# prompt = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["context", "question"])

# # Initialize the AI21 client
# client = AI21Client(api_key=api_key)

# # Streamlit app layout
# st.title("Insurance Chatbot 💼")
# st.markdown("### Ask any questions related to the insurance policies below:")

# # Memory to store previous interactions
# if "history" not in st.session_state:
#     st.session_state.history = []

# def get_relevant_context(question, k=5):
#     results = vectordb.similarity_search(question, k=k)
#     context = "\n".join([doc.page_content for doc in results])
#     return context

# def answer_question(question):
#     context = get_relevant_context(question)
#     full_prompt = prompt.format(context=context, question=question)
    
#     messages = [
#         ChatMessage(role="system", content="You are an AI assistant specialized in insurance policies. Answer questions as best as you can based only on the provided context."),
#         ChatMessage(role="user", content=full_prompt)
#     ]
    
#     response = client.chat.completions.create(
#         model="jamba-1.5-mini",
#         messages=messages,
#         max_tokens=500,
#         temperature = 0,
#         timeout=30  # Set a 30-second timeout
#     )
    
#     return response.choices[0].message.content

# # Chatbot interaction
# user_input = st.text_input("Your question:")
# if user_input:
#     with st.spinner("Thinking..."):
#         response = answer_question(user_input)
#     st.session_state.history.append({"question": user_input, "answer": response})

# # Display conversation history with improved UI
# st.markdown("---")
# if st.session_state.history:
#     for i, interaction in enumerate(st.session_state.history):
#         st.write(f"**You:** {interaction['question']}")
#         st.markdown(f"**InsureBot:**\n{interaction['answer']}")
#         st.markdown("---")


# #To run: streamlit run insurance_chatbot.py

#3
import streamlit as st
import os
from langchain_ai21 import ChatAI21, AI21Embeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from ai21 import AI21Client
from ai21.models.chat import ChatMessage
from dotenv import load_dotenv

# Set page configuration at the top
st.set_page_config(page_title="Insurance Chatbot", page_icon=":robot_face:", layout="wide")

# Load environment variables from the .env file
load_dotenv()

# Initialize the AI21 embeddings
api_key = os.getenv("AI21_API_KEY")
if not api_key:
    st.error("AI21_API_KEY environment variable is not set.")
    st.stop()

embedding = AI21Embeddings(api_key=api_key)

# Load or create the vector database
db_folder = 'db'
vectordb = None

# Check for any expected file in the db_folder
if any(os.path.isfile(os.path.join(db_folder, f)) for f in os.listdir(db_folder)):
    vectordb = Chroma(persist_directory=db_folder, embedding_function=embedding)
    st.success("Vector database loaded successfully.")
else:
    st.error("No existing vector database found. Please create one first.")
    st.stop()

# Define the improved prompt template
PROMPT_TEMPLATE = """
You are an AI assistant specialized in explaining insurance policies. Your task is to answer the user's question based on the following context from an insurance policy:

{context}

Question: {question}

Please provide a detailed yet concise answer by following these guidelines:

1. **Relevant Details**: Include all critical and relevant points directly related to the question.
2. **Clarity**: Use simple language and avoid jargon where possible. If complex terms are necessary, provide a brief explanation in parentheses.
3. **Key Information**: Focus on the main points, but ensure no important information is left out.
4. **Structure**: Use bullet points or numbered lists only when necessary for clarity. Keep the response structured with headings and subheadings.
5. **Length**: Ensure the response is informative but avoid unnecessary elaboration. The goal is to provide a clear, complete, and concise answer.
6. **Truthfulness**: If the context doesn't fully answer the question, mention this and provide the most relevant information available.

Keep the response accurate and easy to understand.
"""

prompt = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["context", "question"])

# Initialize the AI21 client
client = AI21Client(api_key=api_key)

# Streamlit app layout
st.title("Insurance Chatbot 💼")
st.markdown("### Ask any questions related to the insurance policies below:")

# Memory to store previous interactions
if "history" not in st.session_state:
    st.session_state.history = []

def get_relevant_context(question, k=5):
    results = vectordb.similarity_search(question, k=k)
    context = "\n".join([doc.page_content for doc in results])
    sources = "\n".join([f"Source: {doc.metadata['source']}" for doc in results])
    return context, sources

def answer_question(question):
    context, sources = get_relevant_context(question)
    full_prompt = prompt.format(context=context, question=question)
    
    messages = [
        ChatMessage(role="system", content="You are an AI assistant specialized in insurance policies. Answer questions as best as you can based only on the provided context."),
        ChatMessage(role="user", content=full_prompt)
    ]
    
    response = client.chat.completions.create(
        model="jamba-1.5-mini",
        messages=messages,
        max_tokens=2048,
        temperature=0.1,
        timeout=30  # Set a 30-second timeout
    )
    
    final_response = response.choices[0].message.content + "\n\n" + sources
    return final_response

# Chatbot interaction
user_input = st.text_input("Your question:")
if user_input:
    with st.spinner("Thinking..."):
        response = answer_question(user_input)
    st.session_state.history.append({"question": user_input, "answer": response})

# Display conversation history with improved UI
st.markdown("---")
if st.session_state.history:
    for i, interaction in enumerate(st.session_state.history):
        st.write(f"**You:** {interaction['question']}")
        st.markdown(f"**InsureBot:**\n{interaction['answer']}")
        st.markdown("---")

#To run: streamlit run insurance_chatbot.py
