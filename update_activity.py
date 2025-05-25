import datetime
import os

# Define the file to update
activity_file = "activity_log.txt"

# Get current timestamp
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Update or create the activity file with a timestamp
with open(activity_file, "a") as f:
    f.write(f"Activity update at {current_time}\n")

# Configure Git
os.system('git config --global user.name "Tenneti02"')
os.system('git config --global user.email "stenneti3@gitam.in"')

# Stage, commit, and push changes
os.system(f'git add {activity_file}')
os.system(f'git commit -m "Daily activity update: {current_time}"')
os.system("git push origin main")