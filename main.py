import streamlit as st
from supabase import create_client, Client
import pandas as pd

@st.cache_resource
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)

supabase = init_connection()

def main_page1():
    user1 = st.session_state.user1
    user2 = st.session_state.user2
    user3 = st.session_state.user3
    
    title1 = f"<h1 style='text-align: center; color: #47DF9C;'>수학클리닉 🞧 {user1}</h1>"
    title2 = f"<h2 style='text-align: center; color: #ffffff;'>{user2}님, 반갑습니다!</h1>"
    title3 = f"<h6 style='text-align: center; color: #4DDBFE;'>🡴 왼쪽상단 SideBar에서 메뉴를 선택하세요</h1>"
    st.markdown(f"{title1}", unsafe_allow_html=True)
    st.divider()
    st.markdown(f"{title2}", unsafe_allow_html=True)
    st.markdown(f"{title3}", unsafe_allow_html=True)
    st.write('   ')
    st.write('   ')
    st.write('   ')
    st.write('   ')
    st.write('   ')
    st.write('   ')
    st.write('   ')
    st.write('   ')
    st.write('   ')
    st.write('   ')
    st.write('   ')
    st.write('   ')
    with st.expander('최근 학습 현황'):
        
        df = take_exam_data_load(user2)
        if not (df.empty) :
            st.subheader(f':blue[{user2}]님이 응시한 시험 결과')
            df1 = df.loc[:,['응시일','점수','시험고유번호','시험명','틀린문항']]
            df1 = df1.sort_values(by=['응시일'],ascending=False)
        
            st.dataframe(df1)
            df2 = df1.loc[:,['응시일','점수']]
            df2.index = pd.DatetimeIndex(df2['응시일'])
            df2 = df1.loc[:,['점수']]
        else:
            st.subheader(':red[시험 결과] 데이터가 없습니다.')
    with st.container():
        if not (df.empty) :
            title4 = f"<h3 style='text-align: center; color: #4DDBFE;'>simple score chart</h1>"
            st.markdown(title4,unsafe_allow_html=True)
            st.bar_chart(df2)
            

    with st.expander('최근 학습 영상'):
        st.video('https://youtu.be/HnJEE9-UDO8')
        st.video('https://youtu.be/RULttXMytd8')
    
    
    st.divider()
    title5= f"<h3 style='text-align: center; color: gray;'>수학클리닉 🞧 {user1}</h1>"
    st.markdown(f"{title5}", unsafe_allow_html=True)

@st.cache_data
def data_load(user1):

    response1= supabase.table('student_list').select('*').eq('학생소속',user1).execute()
    df = pd.DataFrame(response1.data)
    college = df.학생소속.to_list()
    student_list = df.학생이름.to_list()
    
    return df, college, student_list


@st.cache_data
def take_exam_data_load(user2):

    response2= supabase.table('take_exam').select('*').eq('학생이름',user2).execute()
    df1 = pd.DataFrame(response2.data)
    
    return df1




def login_auth():
    global user2,user1, user3

    user1 = st.session_state.user1
    user2 = st.session_state.user2
    user3 = st.session_state.user3
    df,college, student_list = data_load(user1)
    
    if user1 in college:
        if user2 in student_list:
            
            if len(df[(df['학생소속']==user1)&(df['학생이름']==user2)&(df['학생HP']==user3)].loc[:,])==1:
                main_page1()
            else:
                st.write('암호가 다릅니다.')
        else:
            st.write('등록된 사용자가 아닙니다.')
    else:
        st.write('등록된 단체가 아닙니다.')

def change_pass():
    user1 = st.session_state.user1
    user2 = st.session_state.user2
    user3 = st.session_state.user3
    
    pass1 = st.session_state.pass11
    pass2 = st.session_state.pass22
    pass3 = st.session_state.pass33
    
    if (user3 == pass1) :
        if (user3 != pass3)&(pass2==pass3):
            data = {'학생이름':user2,'학생소속':user1,'학생HP':pass3}
            supabase.table('student_list').update(data).eq('id',ident).execute()
            temphead = st.subheader('비밀번호가 변경되었습니다.')
            time.sleep(2)
            temphead.empty()
            main_page1()
        else:
            st.subheader('기존 비밀번호와 새로운 비밀번호가 일치합니다.')
            reset_pass()
            
    else:
        st.subheader('기존 비밀번호를 잘못 입력하였습니다.')
        reset_pass()

def reset_pass():
    global ident
    user1 = st.session_state.user1
    user2 = st.session_state.user2
    user3 = st.session_state.user3
    df,college, student_list = data_load(user1)
    
    df2 = df[(df['학생소속']==user1)&(df['학생이름']==user2)&(df['학생HP']==user3)].loc[:,]
    df3 = df2.loc[:'id']
    ident = df3.iat[0,0]
    
    if len(df[(df['학생소속']==user1)&(df['학생이름']==user2)&(df['학생HP']==user3)].loc[:,])==1:
       with st.form(key='pass_change'):
           st.text_input('기존 비밀번호를 입력하세요',type='password',key='pass11')
           st.text_input('새로운 비밀번호를 입력하세요',type='password',key='pass22')
           st.text_input('새로운 비밀번호를 한 번 더 입력하세요',type='password',key='pass33')
           st.form_submit_button('변경',on_click=change_pass)
            
    else:
        st.subheader('먼저 로그인을 한 뒤, 다시 시도 하세요.')

with st.expander(':red[로그인 하기] & :blue[비밀번호 변경]'):
    with st.form(key='college_save'):
        st.text_input('학원명을 입력하세요.',key='user1',value='필요와충분')
        st.text_input('학생명을 입력하세요.',key='user2')
        st.text_input('암호를 입력하세요.',type='password',key='user3')
        submit_button = st.form_submit_button(label='로그인',on_click=login_auth)
        reset_button = st.form_submit_button(label='비밀번호 변경',on_click=reset_pass)








