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
resource = supabase2.table('exam_address').select('*').eq('학년','고3/재수').execute()
df = pd.DataFrame(resource.data)

add_list = df.주소.to_list()
content_list = df.내용.to_list()

for i in range(len(add_list)):
    pdf_display = F'<iframe src="{add_list[i]}" width="100%" height="800px"></iframe>'
    with st.expander(content_list[i]):
        st.subheader(content_list[i])
        st.markdown(pdf_display, unsafe_allow_html=True)
