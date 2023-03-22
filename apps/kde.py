import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def app():

    # define the kernel function

    # Set page header
    st.title("Visualize KDE")

    # Sidebar buttons for interactive parameter
    mean = st.sidebar.slider("Mean", min_value=-100.0,
                             max_value=500.0, value=0.0, step=0.1)
    std = st.sidebar.slider("Standard Deviation", min_value=0.1,
                            max_value=50.0, value=1.0, step=0.1)
    st.sidebar.write(
        "Choose smaller size of sample data to visualise clear estimation graphs")
    sample_size = st.sidebar.number_input('Sample dta Size', min_value=1,
                                          max_value=10000, value=5, step=2)
    show_normalised = st.sidebar.checkbox("Normalised Estimation", value=False)
    mykde = st.sidebar.checkbox("MyKDE", value=True)
    snskde = st.sidebar.checkbox("Seaborn KDE", value=False)

    # hist = st.sidebar.checkbox("Histogram", value=False)

    # sample data
    np.random.seed(40)
    data = np.random.normal(mean, std, sample_size)

    def kernel(x):
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

    # define the KDE function

    def kde(data, x_grid, bandwidth=1.0):
        n = len(data)
        result = np.zeros_like(x_grid)
        fig = plt.figure()
        for point in data:
            res = kernel((x_grid - point) / bandwidth)
            plt.plot(
                x_grid, res, marker='o', markersize=2)
            result += res

        r = result / (n * bandwidth)

        if show_normalised:
            plt.plot(x_grid, r, label="Estimation")

        else:
            plt.plot(x_grid, result, label="Estimation"
                     )

        plt.legend()
        st.plotly_chart(fig, theme='streamlit', use_container_width=True)
        return r

    # create the x grid for the plot
    x_grid = np.linspace(min(data) - 1, max(data) + 1, 100)

    # compute the KDE
    density = kde(data, x_grid)

    # plot the KDE
    fig = plt.figure()

    if mykde:
        plt.plot(x_grid, density, label='MyKDE', markersize=20)
    if snskde:
        sns.kdeplot(data, label='Seaborn', markersize=20)

    plt.legend()
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)
