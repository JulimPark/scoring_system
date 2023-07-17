import streamlit as st
import base64
from supabase import create_client
import pandas as pd


# ## 온라인 게시용 수파 접속
@st.cache_data
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)

supabase = init_connection()


st.title('학습 :blue[컨텐츠]')
response2= supabase.table('take_exam').select('*').execute()
st.dataframe(respnse2)
response1= supabase.table('exam_address').select('*').execute()
st.dataframe(respnse1)
st.markdown(f'<iframe src="https://docs.google.com/viewer?url={data_source}&embedded=true" width="100%" height="800px">', unsafe_allow_html=True)
        
