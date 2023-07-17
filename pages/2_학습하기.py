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
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',}
        headers = {'User-Agent':'Chrome/66.0.3359.181'}
      
        
        # PDF 파일을 요청합니다.
        response = requests.get(url)
        
        # PDF 파일을 BytesIO 객체에 저장합니다.
        pdf_bytes = BytesIO(response.content)
        
        # # PDF 파일을 엽니다.
        # pdf_file = open('pdf_file.pdf', 'wb')
        
        # # BytesIO 객체에서 PDF 파일에 데이터를 씁니다.
        # pdf_file.write(pdf_bytes.getvalue())
        
        # # PDF 파일을 닫습니다.
        # pdf_file.close()

        st.write(req.content)
        base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')        
        pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="950" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except HTTPError as e:
        err = e.read()
        code = e.getcode()
        st.write(err)
        st.write(code)
    

view_data('testbuck')
