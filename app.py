import streamlit as st
from multiapp import MultiApp
from apps import kde, normal  # import your app modules here

app = MultiApp()

st.markdown("""
# Statistics Visualize.
""")

# Add all your application here

app.add_app("Normal Distribution", normal.app)
app.add_app("KDE", kde.app)
# The main app
app.run()
