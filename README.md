# TechHub Bot
### The Official Bot for the Towson University CIS TechHub Discord.

## Functionalities:

1. Reacts to check-in messages from Lab Admins for their scheduled shifts.
2. Responds to "!help" commands from students in the student_text channel by indicating whether a Lab Admin is on duty or not.
   * If a Lab Admin is not found in one of the online_lab_admin voice channels, the student receives a message stating: 
     > "Hi @%USERNAME%! There are currently no Lab Admins on duty. Please check the !schedule for hours of availability."
   * If a Lab Admin is found in one of the online_lab_admin voice channels, the student receives a message stating: 
     > "Hi @%USERNAME%! Please join the student_waiting_queue. @%LABADMIN% will be with you shortly."
3. Responds to "!schedule" commands from students in the student_text channel by displaying the semester's Lab Admin schedule.
4. Responds to "!techhub" commands from students in the student_text channel by displaying a link to the TechHub website.

## Requirements:
- [Python](https://www.python.org/downloads/)
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [dotenv](https://pypi.org/project/python-dotenv/)
