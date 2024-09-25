import numpy as np
import matplotlib.pyplot as plt
import os
from IPython.display import clear_output
 
# Function to compute the Mandelbrot set
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n
 
# Generate the Mandelbrot set for a grid of complex numbers
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    mandelbrot_image = np.zeros((height, width))
   
    total_points = width * height
    progress_interval = total_points // 100  # Update progress every 1%
    progress_counter = 0
 
    for i in range(width):
        for j in range(height):
            c = r1[i] + r2[j] * 1j
            mandelbrot_image[j, i] = mandelbrot(c, max_iter)
 
            # Count the number of points processed
            progress_counter += 1
 
            # Print progress every 1%
            if progress_counter % progress_interval == 0:
                progress_percentage = (progress_counter / total_points) * 100
                clear_output(wait=True)
                print(f"\rProgress: {progress_percentage:.2f}%", end="", flush=True)
 
    return mandelbrot_image

def save_mandelbrot_image(xmin, xmax, ymin, ymax, width, height, max_iter, name):
    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    
    # Construct the filename based on the parameters
    filename = (f"images/img_xmin{xmin}_xmax{xmax}_ymin{ymin}_ymax{ymax}_{name}.png"
                .replace('.', '_')  # Replace periods to avoid issues in filenames
                .replace('-', 'm')  # Replace minus signs for clarity
                .replace(' ', '_')) # Replace spaces with underscores

    # Save the image
    
    plt.figure(figsize=(10, 10))
    plt.imshow(mandelbrot_image, cmap='twilight_shifted', extent=[xmin, xmax, ymin, ymax], origin = 'lower')
    plt.colorbar()
    plt.title(f"{name}")
    plt.savefig(filename, dpi=300)
    plt.show()
    
    print(f"Image saved as {filename}")

def save_mandelbrot_image_1(xmin, xmax, ymin, ymax, width, height, max_iter):
    mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 10))
    cax = ax.imshow(mandelbrot_image, cmap='twilight_shifted', extent=[xmin, xmax, ymin, ymax], origin = 'upper')
    fig.colorbar(cax)
    ax.set_title("Full Mandelbrot Set")

    # Save the figure
    filename = (f"mandelbrot_xmin{xmin}_xmax{xmax}_ymin{ymin}_ymax{ymax}.svg"
                .replace('.', '_')  # Replace periods to avoid issues in filenames
                .replace('-', 'm')  # Replace minus signs for clarity
                .replace(' ', '_')) # Replace spaces with underscores

    plt.savefig(filename, dpi=300, format='svg')  # Save as SVG
    plt.close()

    print(f"Image saved as {filename}")

# Parameters to view the whole Mandelbrot set
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 4000, 4000  # Higher resolution for detailed view
max_iter = 512


if __name__ == '__main__':
 
    # Parameters for the Mandelbrot set
    #xmin, xmax, ymin, ymax = -2,1,-1.5,1.5 # Zoomed-in region
    width, height = 2000, 2000  # High resolution
    max_iter = 256

    regions = [[-2, 1, -1.5, 1.5, "Full Mandelbrot Image"],
               [-1.5,-1,-0.5,0, "Main Bulb"],
               [0.25,0.75,-0.75,-0.25, "Elephant Valley"],
               [-0.775, -0.755, 0.125, 0.145, "The Needle"],
               [-0.745, -0.725, 0.105, 0.125, "Triple Spiral"],
               [-0.1015, -0.1010, 0.6330, 0.6335, "Deep Zoom (Small Bulb)"],
               [-0.82, -0.78, 0.18, 0.22, "Spiral Arms"]]
    
    
    # Generate and display the Mandelbrot set with a progress tracker
    for xmin, xmax, ymin, ymax, name in regions:
        save_mandelbrot_image(xmin, xmax, ymin, ymax, width, height, max_iter, name)

#save_mandelbrot_image(xmin, xmax, ymin, ymax, width, height, max_iter, "Full Mandelbrot Image") 
