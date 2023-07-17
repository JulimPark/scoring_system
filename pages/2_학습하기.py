import streamlit as st
import base64
from supabase import create_client
import requests
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
            open_pdf(bucket_name,dict_data,data_source)

def open_pdf(bucket_name,dict_data,url):
    # try:
        # pdf_buffer = BytesIO()
        # res = supabase.storage.from_(bucket_name).download(dict_data)
        # pdf_buffer.write(res)
        
        res = supabase.storage.from_(bucket_name).download(dict_data)
        
        base64_pdf = base64.b64encode(res).decode('utf-8')        
            
        pdf_display = F'<iframe src={url} width="480" height="720" type="application/pdf"></iframe>'
        # pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="480" height="720" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
        
    # except HTTPError as e:
    #     err = e.read()
    #     code = e.getcode()
    #     st.write(err)
    #     st.write(code)
    

view_data('testbuck')
