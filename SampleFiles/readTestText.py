# Read the contents of the file
with open("SampleFiles/test.txt", "r") as file:  # Open the file in read mode ("r")
    contents = file.read() # Read the entire contents of the file in one string

# Print the contents
print(contents)