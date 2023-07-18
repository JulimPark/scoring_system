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


end_color = st.select_slider(
    '학습 범위를 선택하세요',
    options=['고등선행', '고1','고2','고3/재수'],
    value='고1')
st.write('You selected wavelengths', end_color)


st.title('학습 :blue[컨텐츠]')
def set_mark(curri):
    try:
        resource = supabase2.table('exam_address').select('*').eq('학년',curri).execute()
        df = pd.DataFrame(resource.data)
        
        add_list = df.주소.to_list()
        content_list = df.내용.to_list()
        
        for i in range(len(add_list)):
            pdf_display = F'<iframe src="{add_list[i]}" width="100%" height="800px"></iframe>'
            with st.expander(content_list[i]):
                st.subheader(f'{content_list[i]} - {curri}')
                st.markdown(pdf_display, unsafe_allow_html=True)
    except:
        with st.expander(curri):
            st.write(f'{curri}에 대한 컨텐츠가 없습니다.')

if end_color == '고등선행':
    set_mark('고3/재수')
elif end_color == '고1':
    set_mark('고1')
elif end_color == '고2':
    set_mark('고2')
elif end_color == '고3/재수':
    set_mark('고3/재수')
else:
    st.write('선택 범위의 자료가 없습니다.')
