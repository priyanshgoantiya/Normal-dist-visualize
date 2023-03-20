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
sample_data = np.random.normal(0, 1, 5000)

# Set default values for mean and standard deviation
default_mean = np.mean(sample_data)
default_std = np.std(sample_data)

# Create sliders for mean and standard deviation
mean = st.slider("Mean", value=float(default_mean),
                 min_value=-5.0, max_value=5.0, step=0.1)
std = st.slider("Standard Deviation", value=float(
    default_std), min_value=0.5, max_value=5.0, step=0.1)

# Calculate the PDF of the normal distribution for the given mean and standard deviation
# x = np.linspace(-5, 5, 1000)
# pdf = norm.pdf(x, mean, std)
sample_data = np.random.normal(mean, std, 5000)
fig = ff.create_distplot(
    [sample_data], group_labels=['Normal data'], bin_size=0.5)
fig.update_xaxes(range=[-10, 10])
fig.update_yaxes(range=[0, 0.5])
fig.update_layout(
    autosize=False,
    width=1000,
    height=600,)
# Plot!
st.plotly_chart(fig, use_container_width=True, theme=None)
# Plot the normal distribution
# st.line_chart({"x": x, "pdf": pdf})

# Show descriptive statistics for the sample data
st.subheader("Descriptive Statistics for Sample Data")
st.write("Mean:", np.mean(sample_data))
st.write("Standard Deviation:", np.std(sample_data))
st.write("Minimum:", np.min(sample_data))
st.write("Maximum:", np.max(sample_data))
