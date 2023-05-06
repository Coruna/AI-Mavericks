import json
import matplotlib.pyplot as plt

# The JSON string

with open('assessment.json') as user_file:
  file_contents = user_file.read()

print(file_contents)
data = json.loads(file_contents)
# Extract the scalar values and store them in a dictionary
scalar_data = {}
for key in data:
    if key != "Tips":
        scalar_data[key] = int(data[key])

# Create a bar chart for the scalar values
fig, ax = plt.subplots()
ax.bar(scalar_data.keys(), scalar_data.values())
ax.set_ylim(0, 10)
ax.set_ylabel('Score')
ax.set_title('Performance Ratings')
plt.show()

# Print the list of tips
print("Tips:")
for tip in data["Tips"]:
    print("- " + tip)
