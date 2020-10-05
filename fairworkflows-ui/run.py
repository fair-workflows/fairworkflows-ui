import streamlit as st
from fairworkflows import FairWorkflow

st.title('Demo fairworkflows interface')

description = None
workflow = None
if description is None:
    st.text('Create a new FAIR workflow')
    description = st.text_input('description', 'Add a description...')
    workflow = FairWorkflow(description=description)
else:
    st.text(str(workflow))
