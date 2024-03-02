import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def FuncPlot():
    def custom_function(x):
        z = np.zeros_like(x)
        z[x < 0] = (1 + x[x < 0] + x[x < 0]**2) / (1 + x[x < 0]**2)
        z[(x >= 0) & (x < 1)] = np.sqrt(1 + (5 * x[(x >= 0) & (x < 1)] / (1 + x[(x >= 0) & (x < 1)]**3)))
        z[x >= 1] = 5 * np.abs(0.7 * np.cos(x[x >= 1]) + np.sin(x[x >= 1]))
        return z

    x_values = np.linspace(-2, 2, 400)
    y_values = (1 + (x_values + 5)**(1 / 3)) / (1 + np.sqrt(2 + x_values + x_values**2))
    z_values = custom_function(x_values)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(x_values, y_values, label='y = (1 + (x + 5)^(1/3)) / (1 + √(2 + x + x^2))')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Function y(x)')
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(x_values, z_values, label='z(x)')
    plt.xlabel('x')
    plt.ylabel('z')
    plt.title('Function z(x)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def SurfacePlot():
    # Define the function
    def custom_function(x, y):
        return 7 * np.exp(0.5 * x - 1) * x ** 3 - 4 * y ** 4

    # Generate data
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = custom_function(x, y)

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the surface
    surf = ax.plot_surface(x, y, z, cmap='viridis')

    # Add labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Surface Plot of z = 7e^(0.5x-1)*x^3 - 4y^4')

    # Add a color bar
    fig.colorbar(surf)

    plt.show()

def PolarisPlot():
    # Define parameters
    a = 2  # Constant a
    l = 1  # Constant l

    # Create polar grid
    theta = np.linspace(1, 2 * np.pi, 500)  # Angles for the polar plot

    # Calculate radius for both branches of the Conchoid
    radius1 = a / np.sin(theta) + l
    radius2 = a / np.sin(theta) - l

    # Create polar plot
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

    # Plot both branches with different colors
    ax.plot(theta, radius1, color='blue', label='Branch 1')
    ax.plot(theta, radius2, color='red', label='Branch 2')

    # Set limits to avoid truncation
    ax.set_rlim(0, max(radius1.max(), radius2.max()) + 0.5)

    # Customize plot
    ax.set_title('Conchoid P = (a/(sin(θ)) ± l')
    ax.set_label('P')
    ax.legend()

    # Show the plot
    plt.show()


def SurfaceSecondOrder():

    # Define constants
    a = 2  # radius along x-axis
    b = 1  # radius along y-axis

    # Generate data
    theta = np.linspace(0, 2 * np.pi, 100)
    z = np.linspace(-1, 1, 100)
    theta, z = np.meshgrid(theta, z)
    x = a * np.cos(theta)
    y = b * np.sin(theta)

    # Create 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the surface
    ax.plot_surface(x, y, z, alpha=0.5)

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Elliptical Cylinder')

    # Show plot
    plt.show()

def PlotChart():
    # Define the years and countries
    years = [1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000]
    countries = ['Germany', 'France', 'United Kingdom', 'Italy']

    # Define the data for each country
    data = {
        'Germany': [18.5, 23.5, 25, 26.5, 29, 31, 34, 35, 37, 38.5],
        'France': [20, 20, 20, 19.5, 19, 21, 23, 25, 26.5, 27.5],
        'United Kingdom': [16.5, 18.5, 20, 20.5, 22.5, 24, 25, 25.5, 26, 26.5],
        'Italy': [15, 16.5, 17, 18, 18.5, 20, 22, 24, 24.5, 25]
    }

    # Set the width of the bars
    bar_width = 0.2

    # Set the position of each bar on the x-axis
    r1 = np.arange(len(years))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]
    r4 = [x + bar_width for x in r3]

    # Plot the bars
    plt.bar(r1, data['Germany'], color='b', width=bar_width, edgecolor='grey', label='Germany')
    plt.bar(r2, data['France'], color='r', width=bar_width, edgecolor='grey', label='France')
    plt.bar(r3, data['United Kingdom'], color='g', width=bar_width, edgecolor='grey', label='United Kingdom')
    plt.bar(r4, data['Italy'], color='y', width=bar_width, edgecolor='grey', label='Italy')

    # Add xticks on the middle of the group bars
    plt.xlabel('Year', fontweight='bold')
    plt.xticks([r + bar_width for r in range(len(years))], years)

    # Add y label
    plt.ylabel('Bilion people in world economy', fontweight='bold')

    # Add title
    plt.title('Average count of people in world economy')

    # Add legend
    plt.legend()

    # Show plot
    plt.show()

def Plot3DChart():
    # Define the years and countries
    years = [1900, 1913, 1929, 1938, 1950, 1960, 1970, 1980, 1990, 2000]
    countries = ['Germany', 'France', 'United Kingdom', 'Italy']

    # Define the data for each country
    data = {
        'Germany': [18.5, 23.5, 25, 26.5, 29, 31, 34, 35, 37, 38.5],
        'France': [20, 20, 20, 19.5, 19, 21, 23, 25, 26.5, 27.5],
        'United Kingdom': [16.5, 18.5, 20, 20.5, 22.5, 24, 25, 25.5, 26, 26.5],
        'Italy': [15, 16.5, 17, 18, 18.5, 20, 22, 24, 24.5, 25]
    }

    # Set the positions of the bars
    xpos = np.arange(len(years))
    ypos = np.arange(len(countries))

    # Create meshgrid for x and y positions
    xpos, ypos = np.meshgrid(xpos, ypos, indexing="ij")

    # Flatten the arrays
    xpos = xpos.ravel()
    ypos = ypos.ravel()

    # Set the height of the bars
    zpos = np.zeros_like(xpos)

    # Set the width of the bars
    dx = dy = 0.5

    # Flatten the data values
    data_values = []
    for country in countries:
        data_values.extend(data[country])

    # Plot the 3D bars
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    ax.bar3d(xpos, ypos, zpos, dx, dy, data_values)

    # Set labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Country')
    ax.set_zlabel('Billion people')
    ax.set_xticks(np.arange(len(years)))
    ax.set_xticklabels(years)
    ax.set_yticks(np.arange(len(countries)))
    ax.set_yticklabels(countries)
    ax.set_title('Count of people in world economy')
    plt.show()


def main():
    FuncPlot()
    SurfacePlot()
    PolarisPlot()
    SurfaceSecondOrder()
    PlotChart()
    Plot3DChart()

if __name__ == "__main__":
    main()