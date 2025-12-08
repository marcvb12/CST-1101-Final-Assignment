#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Get test score from user
score = int(input("Enter your test score: "))

# Determine letter grade
if score >= 90:
    print("Your grade is A")
elif score >= 80:
    print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
else:
    print("Your grade is F")


# In[ ]:


# Get scores from user
teamA = int(input("Enter score for Team A: "))
teamB = int(input("Enter score for Team B: "))

# Determine winner
if teamA > teamB:
    print("Team A wins!")
elif teamB > teamA:
    print("Team B wins!")
else:
    print("TIE")


# In[ ]:


# Get RGB values from user
red = int(input("Enter red color value: "))
blue = int(input("Enter blue color value: "))
green = int(input("Enter green color value: "))

# Validate red
if red < 0:
    red = 0
elif red > 255:
    red = 255

# Validate blue
if blue < 0:
    blue = 0
elif blue > 255:
    blue = 255

# Validate green
if green < 0:
    green = 0
elif green > 255:
    green = 255

# Display valid RGB values
print("Valid RGB values:")
print(f"Red: {red}")
print(f"Blue: {blue}")
print(f"Green: {green}")


# In[ ]:


# Get military time from user
militaryTime = int(input("Enter military time (0-2359): "))

# Extract hours and minutes
hour = militaryTime // 100  # Integer division
minutes = militaryTime % 100  # Modulo to get remainder

# Convert to civilian time
if militaryTime == 0:
    print("12:00 AM (Midnight)")
elif militaryTime == 1200:
    print("12:00 PM (Noon)")
elif militaryTime < 1200:
    # AM times
    if hour == 0:
        displayHour = 12
    else:
        displayHour = hour
    print(f"{displayHour}:{minutes:02d} AM")
else:
    # PM times
    if hour == 12:
        displayHour = 12
    else:
        displayHour = hour - 12
    print(f"{displayHour}:{minutes:02d} PM")


# In[ ]:


print("This is the output of your script.")

input("Press Enter to exit...")

