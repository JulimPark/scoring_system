import streamlit as st
import base64
from supabase import create_client
import urllib
from urllib.error import URLError, HTTPError
import requests
from pathlib import Path
from io import BytesIO

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
            open_pdf(data_source)

def open_pdf(url):
    try:
                
        
        # PDF를 읽습니다.
        response = requests.get(url)
        pdf_bytes = response.content
        
        # PDF를 BytesIO 객체에 저장합니다.
        pdf_buffer = BytesIO()
        pdf_buffer.write(pdf_bytes)
        
        st.write(pdf_buffer.getvalue())
        # st.write(req.content)
        base64_pdf = base64.b64encode(pdf_buffer.getvalue()).decode('utf-8')        
        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="950" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
        
    except HTTPError as e:
        err = e.read()
        code = e.getcode()
        st.write(err)
        st.write(code)
    

view_data('testbuck')
