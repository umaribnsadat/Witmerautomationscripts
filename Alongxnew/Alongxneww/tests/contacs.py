import csv

# Data to write to CSV
data = [
    ['Name', 'PhoneNumber', 'Message'],
    ['John Doe', '+91 9182919517', 'Hello John! This is a test message.'],
    ['Jane Doe', '+911234567891', 'Hi Jane! Hope you\'re doing well.']
]

# Create and write to the CSV file
with open('contactsnew.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("contactss.csv file created successfully!")
