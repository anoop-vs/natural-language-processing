import streamlit as st

# success
st.success("Success")
 
# success
st.info("Information")
 

# success
st.warning("Warning")
 
# success
st.error("Error")
 
# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)