import streamlit as st
import numpy as np
from matplotlib import pyplot as plt
# import seaborn as sns
import plotly.figure_factory as ff


# Set page title
st.set_page_config(page_title="Interactive Normal Distribution")

# Set page header
st.title("Interactive Normal Distribution")

# Generate random sample data
np.random.seed(42)
original_data = np.random.normal(0, 1, 10000)

# Set default values for mean and standard deviation
default_mean = 1.0
default_std = 2.0

# Create sliders for mean and standard deviation
# mean = st.slider("Mean", value=float(default_mean),
#                  min_value=-5.0, max_value=5.0, step=0.1)
# std = st.slider("Standard Deviation", value=float(
#     default_std), min_value=0.5, max_value=5.0, step=0.1)

# Create sliders for the mean and standard deviation in the sidebar
mean = st.sidebar.slider("Mean", min_value=-10.0,
                         max_value=10.0, value=default_mean, step=0.1)
std = st.sidebar.slider("Standard Deviation", min_value=0.1,
                        max_value=5.0, value=default_std, step=0.1)
rug = st.sidebar.checkbox("Rug Plot", value=False)
curve = st.sidebar.checkbox("PDF urve", value=False)
hist = st.sidebar.checkbox("Histogram", value=True)
bin_size = st.sidebar.number_input('Bin Size', min_value=0.1,
                                   max_value=10.0, value=0.5, step=0.1, )
# Calculate the PDF of the normal distribution for the given mean and standard deviation
# x = np.linspace(-5, 5, 1000)
# pdf = norm.pdf(x, mean, std)
sample_data = np.random.normal(mean, std, 10000)
fig = ff.create_distplot(
    [original_data, sample_data], group_labels=['Original data', 'Changed'], bin_size=bin_size, show_curve=curve, show_rug=rug, show_hist=hist)
fig.update_xaxes(range=[-10, 10])
fig.update_yaxes(range=[0, 0.5])
fig.update_layout(
    autosize=False,
    width=1000,
    height=800,)
# Plot!
st.plotly_chart(fig, theme=None, )
# Plot the normal distribution
# st.line_chart({"x": x, "pdf": pdf})
# Show descriptive statistics for the sample data
st.subheader("Descriptive Statistics for Sample Data")
st.write("Mean:", np.mean(sample_data))
st.write("Standard Deviation:", np.std(sample_data))
st.write("Minimum:", np.min(sample_data))
st.write("Maximum:", np.max(sample_data))
