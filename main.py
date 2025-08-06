import streamlit as st

st.title("🌷Begonia bagh")
st.markdown("**🌸🌸🪷🪷Best begonia flower gifted to you.Wishing you gook luck,everyday.🪷🪷🌸🌸**")
tab1,tab2,tab3,tab4 = st.tabs(["Red","White","Purple","Green"])
with tab1:
    st.image("1.jpg",width=500)
    st.image("2.png", width=500)
    st.image("3.png", width=500)

with tab2:
    st.image("7.png",width=500)
    st.image("8.png", width=500)
    st.image("9.png", width=500)


with tab3:
    st.image("4.png",width=500)
    st.image("5.png", width=500)
    st.image("6.png", width=500)

with tab4:
    st.image("10.png",width=500)
    st.image("11.png", width=500)
    st.image("12.png", width=500)
st.markdown("&nbsp;" * 700 + " *Bye Serendipity*", unsafe_allow_html=True)


