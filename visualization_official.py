import json
import matplotlib.pyplot as plt

# The JSON string

with open('assessment.json') as user_file:
  file_contents = user_file.read()

#"{"Problem Solving Skills":"10", "Friendliness": "9", "Professionalism": "10",
# "Understandability":"10", "Tips":["Excellent job! You handled the situation p
# rofessionally and effectively.", "Continue to provide clear and concise instruc
# tions to ensure the customer feels confident in the process."]}"
#Eliminate the first and the last ""

data = file_contents.replace('\\', '')
data = data[1:-1]

parsed_data = json.loads(data)
# Extract the scalar values and store them in a dictionary
scalar_data = {}
for key in parsed_data:
    print(key)
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
