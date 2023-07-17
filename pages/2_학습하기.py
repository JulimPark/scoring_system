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

supabase2 = init_connection()



st.title('학습 :blue[컨텐츠]')
resource = supabase2.table('take_exam').select('*').execute()
df = pd.DataFrame(resource.data)
st.dataframe(df)
