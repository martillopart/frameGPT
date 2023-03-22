import cv2
import os
import numpy as np
os.chdir('C:/Users/korla/OneDrive/Escriptori/Startup/frameGPT/encoder')

# Read the video file
cap = cv2.VideoCapture('person01_handwaving_d2_uncomp.avi')

# Get the frame rate
fps = cap.get(cv2.CAP_PROP_FPS)

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, fps, (160, 120), False)

def matrix_to_string(matrix):
# Initialize an empty string to store the output
    output = ""
    
    # Iterate through the rows of the matrix
    for i, row in enumerate(matrix):
        # Iterate through the elements of each row
        for j, element in enumerate(row):
            # Append the element to the output string
            output += str(element)
    
            # Add a space separator unless this is the last element in the row
            if j < len(row) - 1:
                output += " "
    
        # Add an underscore separator between rows unless this is the last row
        if i < len(matrix) - 1:
            output += " _ "
        
    # Call the matrix_to_string function with your matrix argument
    return output

result = ""

# Read the first 10 frames of the video and convert them to grayscale
for i in range(625):
    
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Resize the frame to 160 x 120
    #resized_frame = cv2.resize(gray_frame, (160, 120))

    # Write the frame to the output video file
    #out.write(resized_frame)
    out.write(gray_frame)

    # Convert the frame to a matrix of pixel values
    #pixel_matrix = np.matrix(resized_frame.tolist())
    pixel_matrix = np.matrix(gray_frame.tolist())
    
    # Convert each element of the pixel matrix to an 8 digit binary number
    binary_matrix = np.vectorize(lambda x: format(x, '08b'))(pixel_matrix)
    
    #to_text = np.delete(binary_matrix, np.s_[3:119], axis=0)

    # # Delete column 2
    #to_text_this = np.delete(to_text, np.s_[3:159], axis=1)
    
    result += matrix_to_string(binary_matrix).replace("[", "").replace("]", "").replace("'", "") + " / "
         
    
filename = "person01_handwaving_d2_uncomp.txt"  # Replace this with the desired filename

with open(filename, "w") as f:
    f.write(result)

print(result)

# Release the video capture and writer objects
cap.release()
out.release()
