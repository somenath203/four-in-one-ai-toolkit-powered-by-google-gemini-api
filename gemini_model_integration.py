from dotenv import load_dotenv
import os 
import google.generativeai as genai


load_dotenv()


google_gemini_api_key = os.getenv('GOOGLE_GEMINI_API_KEY')


genai.configure(api_key=google_gemini_api_key)


def load_gemini_model():
    
    gemini_model = genai.GenerativeModel('gemini-pro')

    return gemini_model


def change_role_in_streamlit_app(role):

    if role == 'model':

        return 'assistant'
    
    else:

        return role
    

def load_gemini_pro_vision_model(prompt, image):

    gemini_model = genai.GenerativeModel('gemini-pro-vision')

    response = gemini_model.generate_content([prompt, image])

    return response.text


def load_gemini_embedding_model(input_text):

    gemini_model = genai.embed_content(model='models/embedding-001', content=input_text, task_type='retrieval_document')

    return gemini_model['embedding']


def load_gemini_question_answer_model(user_question):

    gemini_model = genai.GenerativeModel('gemini-pro')

    response_from_model = gemini_model.generate_content(user_question)

    return response_from_model.text   