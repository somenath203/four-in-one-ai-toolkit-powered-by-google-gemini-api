import streamlit as st 
from streamlit_option_menu import option_menu
from PIL import Image

from gemini_model_integration import load_gemini_model, change_role_in_streamlit_app, load_gemini_pro_vision_model, load_gemini_embedding_model, load_gemini_question_answer_model


st.set_page_config(
    page_title='4 in 1 AI Toolkit',
    page_icon='🧠',
    layout='centered'
)


with st.sidebar:

    title_and_pages = option_menu('4 in 1 AI Toolkit', 
                                options=['Chatbot', 
                                         'Image Caption Generator', 
                                         'Embed Text', 
                                         'QnA Bot'], 
                                menu_icon='robot', icons=['chat-dots-fill', 'image-fill', 'textarea-t', 'patch-question-fill'],
                                default_index=0) 
    


if title_and_pages == 'Chatbot':


    model = load_gemini_model()


    if "chat_session" not in st.session_state:


        st.session_state.chat_session = model.start_chat(history=[])
    

    st.title('🤖 ChatBot')


    for message in st.session_state.chat_session.history:

        with st.chat_message(change_role_in_streamlit_app(message.role)):

            st.markdown(message.parts[0].text)

    
    user_prompt_input = st.chat_input('Ask Gemini Pro...')

    if user_prompt_input:

        st.chat_message(change_role_in_streamlit_app("user")).markdown(user_prompt_input)


        response_from_gemini = st.session_state.chat_session.send_message(user_prompt_input)

        with st.chat_message('assistant'):
            
            st.markdown(response_from_gemini.text)



elif title_and_pages == 'Image Caption Generator':
     

     st.title('📷 Image Caption Generator')

     image_input_from_user = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])

     
     if st.button("Generate Caption"):
         
        if not image_input_from_user:

            st.error('Please enter an image')

        else:

            image = Image.open(image_input_from_user)

            col1, col2 = st.columns(2) 

            with col1:
             
                image_resize = image.resize((800, 500))

                st.image(image_resize)


            with col2:
            
                default_prompt = "generate a short caption of the image"

                caption_of_image_geneated_by_gemini_model = load_gemini_pro_vision_model(default_prompt, image)

                st.info(caption_of_image_geneated_by_gemini_model)



elif title_and_pages == 'Embed Text':

    st.title('📖 Text Embedding')

    
    input_text = st.text_area(label='Enter Your Text', placeholder='enter text here and press "Get Embeddings" to get the embeddings...')


    if st.button("Get Embeddings"):

        if not input_text:

            st.error('Please enter something in the textarea.')

        else:

            response = load_gemini_embedding_model(input_text)

            st.markdown(response)



elif title_and_pages == 'QnA Bot':

    st.title('🙋 QnA Bot')


    input_text = st.text_area(label='Enter Your Question', placeholder='enter your question here and press "Get Answer" button to get answer from gemini model...')


    if st.button("Get Answer"):

        if not input_text:

            st.error('Please enter something in the textarea.')

        else:

            response = load_gemini_question_answer_model(input_text)

            st.markdown(response)