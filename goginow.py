from googleapiclient.discovery import build
from google.oauth2 import service_account
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

SERVICE_ACCOUNT_FILE = 'keys_google.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1il7oqRQnY2We5kAAEcTGFbtVySGIxnDmUVdtOja3iF8'

service = build('sheets', 'v4', credentials=creds, cache_discovery=False)

sheet = service.spreadsheets()
International_title = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="해외육류!A:A").execute()

International_values = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="해외육류!A2:C").execute()
International_title_values = International_title.get('values',[])
values = International_values.get('values',[])

st.title('식스맵 프로젝트')

st.write('''
●컨셉 : 고기의 모든 곳을 모아놓은 식스 맵이라는 지도를 찾기 위해, 전국의 농가와 미트 러버들이 고기를 판매하고 구매하며 정보를 공유하는 신세계

●설명 : 국내 지역 및 전 세계 나라 기반 육류 소개 및 온라인 판매

●배경 : 
1. 육류 상품은 넘쳐나지만, 방향성을 상실한 풍요 속의 빈곤 속에서 자신만의 고기를 찾을 수 있는 나침반 필요
2. 타사 온라인 정육 사이트와 차별성 필요
3. 추후 지역 농가의 소개 및 홍보 창구 역할을 수행함으로써 지역 농가 활성이라는 사회적 메세지 전달
4. 육그램이 육류 업계에서 남기고자 하는 이상적 의미 정립 및 방향성 확립
'''
)

np_values = np.array(values)

df = pd.DataFrame(np_values, columns=['나라','지역','부위'])

st.table(df)

#st.write(np_values)
#st.write(np_values.dtype)

print(np_values)


'''
st.write('Below is a DataFrame : ', data_frame)

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write('below is a air condition graph',df,c)
'''

