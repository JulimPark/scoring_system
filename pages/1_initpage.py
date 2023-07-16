import streamlit as st

# username = st.session_state.user2

# st.title(f'{username} 님의 정답입력기')

import pandas as pd
from supabase import create_client, Client

url: str = "https://uctmfeyuzyigljzvslth.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVjdG1mZXl1enlpZ2xqenZzbHRoIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODkyNzEzNDEsImV4cCI6MjAwNDg0NzM0MX0.WEHXEB2U0PEAG7Pl_3pe8kPLb2MPWG_zrMCvgbMik8U"
supabase: Client = create_client(url, key)


response2= supabase.table('student_list').select('*').execute()
df = pd.DataFrame(response2.data)
df