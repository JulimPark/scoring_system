import streamlit as st
import base64
from supabase import create_client
from urllib import request
from io import BytesIO
import fitz


# ## 온라인 게시용 수파 접속
@st.cache_resource
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)

supabase = init_connection()


st.title('학습 :blue[컨텐츠]')
def view_data(bucket_name):
    res = supabase.storage.from_(bucket_name).list()
    for i in range(len(res)):
        dict_data = res[i]['name']
        data_source = supabase.storage.from_(bucket_name).get_public_url(dict_data)
        with st.expander(dict_data[:-4]):
            st.header(dict_data[:-4])            
            open_pdf(bucket_name,dict_data,data_source)
image_list = []
def open_pdf(bucket_name,dict_data,url):
    # # try:
    #     # pdf_buffer = BytesIO()
    #     res = supabase.storage.from_(bucket_name).download(dict_data)
    #     with open('temp.pdf','wb') as f:
    #         f.write(res)
    #         doc = fitz.open(f)
    #     # doc = fitz.open(res)
    
    #     for page in doc:
    #         img = page.get_pixmap()
    #         image_list.append(img)

    #     for i in range(len(image_list)):
    #         st.image(image_list[i])
        res = supabase.storage.from_(bucket_name).download(dict_data)
        
        base64_pdf = base64.b64encode(res).decode('utf-8')        

        
        # st.markdown(f'<embed src="https://drive.google.com/viewerng/viewer?embedded=true&url={url}" width="400" height="400">', unsafe_allow_html=True)
    
        # pdf_display = f'<a href="{url}"></a>'
        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="480" height="720" type="application/pdf" scrolling="yes"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    

view_data('testbuck')
