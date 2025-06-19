import streamlit as st

st.title('오늘은 신나는 금요일!')
st.header('오늘은 Streamlit 배우는 날~')
st.subheader('Streamlit으로 만들어 보는 내 사이트!')

my_site = st.text_input('오늘 내가 만들어보고 싶은 사이트는?')  # input 값을 활용하기 위해선 변수에 담아줘야함
print(my_site)      # 내 터미널에 출력됨
st.write(my_site)   # 웹사이트에 출력됨

if st.button(f'{my_site} 접속하기'):
    st.success(f"{my_site}로 접속중😘", icon='✅')


