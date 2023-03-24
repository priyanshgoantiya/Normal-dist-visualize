import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def app():

    # define the kernel function

    # Set page header
    st.title(
        "Visualize [Kernel Density Estimation](https://en.wikipedia.org/wiki/Kernel_density_estimation)")

    # Normal distributed data
    sample_data = st.sidebar.selectbox(
        'Sample Data Type', ('Normal', 'Bimodal'), key='sample data')

    if sample_data == 'Normal':
        # Sidebar buttons for interactive parameter
        mean = st.sidebar.slider("Mean", min_value=-100.0,
                                 max_value=500.0, value=0.0, step=0.1)
        std = st.sidebar.slider("Standard Deviation", min_value=0.1,
                                max_value=50.0, value=1.0, step=0.1)
    else:
        # Sidebar buttons for interactive parameter
        std = st.sidebar.slider("Common Standard Deviation", min_value=0.1,
                                max_value=50.0, value=1.0, step=0.1)
        mean1 = st.sidebar.slider("Mean 1", min_value=-100.0,
                                  max_value=500.0, value=0.0, step=0.1)
        mean2 = st.sidebar.slider("Mean 2", min_value=mean1+2*std,
                                  max_value=500.0, value=0.0, step=0.1)

    st.sidebar.write(
        "Choose smaller size of sample data to visualise clear estimation graphs")
    sample_size = st.sidebar.number_input('Sample dta Size', min_value=1,
                                          max_value=10000, value=5, step=2)

    show_un = st.sidebar.checkbox("Estimation", value=True)
    show_normalised = st.sidebar.checkbox("Normalised Estimation", value=False)

    st.sidebar.markdown("---")
    mykde = st.sidebar.checkbox("MyKDE", value=True)
    if mykde:
        st.sidebar.write(
            """MyKDE is using [Gaussian Kermel](https://en.wikipedia.org/wiki/Kernel_(statistics)#Kernel_functions_in_common_use)""")
        bw_method = st.sidebar.selectbox(
            "Choose Bandwidth Method", ['scott', 'silverman', 'other'], )
        h = None
        if bw_method == 'other':
            h = st.sidebar.number_input('Enter Bandwidth', min_value=0.1,
                                        max_value=10000.0, value=1.0, step=0.5)
    snskde = st.sidebar.checkbox("Seaborn KDE", value=False)

    if snskde:
        bw_method_sns = st.sidebar.selectbox(
            "Choose Bandwidth Method", ['scott', 'silverman', 'other'], key="Seaborn BW_method")

        if bw_method_sns == 'other':
            bw_method_sns = st.sidebar.number_input(
                'Enter Bandwidth', min_value=0.1, max_value=10000.0, value=1.0, step=0.5, key="Seaborn BW")
    # hist = st.sidebar.checkbox("Histogram", value=False)

    # sample data
    np.random.seed(40)
    if sample_data == 'Normal':
        data = np.random.normal(mean, std, sample_size)
    else:
        st.write("### Bimodal : \nA mixture of two normal distributions with equal standard deviations is **bimodal** only if their means differ by at least twice the common standard deviation.")
        data = np.concatenate([np.random.normal(
            mean1, std, sample_size//2), np.random.normal(mean2, std, sample_size//2)])

    def kernel(x):
        return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

    # define the KDE function
    def kde(data, x_grid, bandwidth=1.0, bw_method='scott'):
        n = len(data)
        st.write("Shape of Data :", data.shape)
        if bw_method == 'scott':
            h = 1.059 * np.std(data) * n ** (-1/5)
        elif bw_method == 'silverman':
            h = 0.9 * \
                np.min([np.std(data), np.percentile(
                    np.abs(data - np.median(data)), 50)]) * len(data) ** (-1/5)
        else:
            h = bandwidth
        result = np.zeros_like(x_grid)
        fig = plt.figure()
        for point in data:
            res = kernel((x_grid - point) / h)
            plt.plot(
                x_grid, res)
            result += res

        r = result / (n * h)

        if show_normalised:
            plt.plot(x_grid, r, linestyle='--', color='green',
                     label='Normalised Estimation')
        if show_un:
            plt.plot(x_grid, result, linestyle='-.',
                     color='red', label='Estimation')

        plt.legend()
        st.plotly_chart(fig, theme='streamlit', use_container_width=True)
        return r

    # create the x grid for the plot
    x_grid = np.linspace(min(data) - 1, max(data) + 1, 100)

    # compute the KDE
    density = kde(data, x_grid, bandwidth=h, bw_method=bw_method)

    # plot the KDE
    fig = plt.figure()

    if mykde:
        plt.plot(x_grid, density, label='MyKDE', markersize=20)
    if snskde:
        sns.kdeplot(data, label='Seaborn', markersize=20,
                    bw_method=bw_method_sns)

    plt.legend()
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)
