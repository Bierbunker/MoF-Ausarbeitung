import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

def count_x_in_brackets(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        count = 0
        in_brackets = False
        for char in content:
            if char == '[':
                in_brackets = True
            elif char == ']':
                in_brackets = False
            elif char == 'x' and in_brackets:
                count += 1
        return count

def visualize_progress(count, max_count=100):
    fig, ax = plt.subplots(figsize=(12, 2)) 

    # Load the image
    img = mpimg.imread('resources/progress_background.png')

    # Scale progress to image width
    progress_scaled = int((count/max_count) * img.shape[1])

    # Create a mask based on progress
    mask = np.ones_like(img)
    mask[:, progress_scaled:] = 0

    # Apply the mask: this could also be done with np.where
    img_masked = np.copy(img)
    img_masked[mask == 0] = 1

    # Show the image
    ax.imshow(img_masked, aspect='auto', extent=[0, max_count, 0, 1])

    ax.set_xlim(0, max_count) # Set limits of x-axis
    ax.axis('off') # Hide axes

    # Adding a title and percentage inside the progress bar
    title = "Progress MoF-Ausarbeitung"
    percentage = (count/max_count) * 100
    percentage_text = f'{percentage:.2f}%'

    plt.title(title, fontsize=16, fontweight='bold', color='black')
    ax.text(max_count/2, 0.5, percentage_text, ha='center', va='center', fontsize=12, fontweight='bold', color='black')

    # Save the figure
    fig.savefig('resources/progress.png', bbox_inches='tight', pad_inches=0)
    plt.close(fig)


# Get the path of the current file
current_file_path = os.path.realpath(__file__)
# Get the directory containing the current file
base_dir = os.path.dirname(current_file_path)
# Construct the path to the todo.md file
todo_file_path = os.path.join(base_dir, 'todo.md')

# Count the number of 'x's inside brackets in the file
count = count_x_in_brackets(todo_file_path)

# Create directory named 'resources' if it does not exist
os.makedirs(os.path.join(base_dir, 'resources'), exist_ok=True)

# Visualize the progress
visualize_progress(count)
