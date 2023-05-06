import json
import matplotlib.pyplot as plt

# The JSON string
data = "{\"Problem Solving Skills\":\"10\", \"Friendliness\": \"9\", \"Professionalism\": \"10\",\"Understandability\":\"10\", \"Tips\":[\"Excellent job!\", \"Keep up the good work!\"] }"

# Parse the JSON into a dictionary
parsed_data = json.loads(data)

# Extract the scalar values and store them in a dictionary
scalar_data = {}
for key in parsed_data:
    if key != "Tips":
        scalar_data[key] = int(parsed_data[key])

# Create a bar chart for the scalar values
fig, ax = plt.subplots()
ax.bar(scalar_data.keys(), scalar_data.values())
ax.set_ylim(0, 10)
ax.set_ylabel('Score')
ax.set_title('Performance Ratings')
plt.show()

# Print the list of tips
print("Tips:")
for tip in parsed_data["Tips"]:
    print("- " + tip)
