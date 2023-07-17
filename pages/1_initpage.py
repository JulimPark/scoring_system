import streamlit as st

# username = st.session_state.user2

# st.title(f'{username} 님의 정답입력기')

@st.cache_resource
def init_connection():
    url = st.secrets["supabase_url"]
    key = st.secrets["supabase_key"]
    return create_client(url, key)

supabase = init_connection()


response2= supabase.table('student_list').select('*').execute()
df = pd.DataFrame(response2.data)
df
