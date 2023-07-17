import streamlit as st
import base64
from supabase import create_client
import pandas as pd


# ## 온라인 게시용 수파 접속
@st.cache_resource
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)

supabase = init_connection()


st.title('학습 :blue[컨텐츠]')
response1= supabase.table('exam_address').select('*').eq('학년','고3/재수').execute()
st.dataframe(respnse1)
st.markdown(f'<iframe src="https://docs.google.com/viewer?url={data_source}&embedded=true" width="100%" height="800px">', unsafe_allow_html=True)
        open_pdf(bucket_name,dict_data,data_source)

def open_pdf(bucket_name,dict_data,url):
    
        res = supabase.storage.from_(bucket_name).download(dict_data)
        
        base64_pdf = base64.b64encode(res).decode('utf-8')        

        
        st.markdown(f'<iframe src="https://docs.google.com/viewer?url={url}&embedded=true" width="100%" height="800px">', unsafe_allow_html=True)
        # st.markdown(f'<iframe src="{url}/preview#toolbar=0" width="100%" height="800px">', unsafe_allow_html=True)
    

    

view_data('testbuck')
