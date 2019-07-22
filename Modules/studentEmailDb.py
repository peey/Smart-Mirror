"""
Usage:

from emails import dict as emails

print(emails['roll number']) # note that roll number is a string sinc it may contain the letter M

Sample Output: {"email": "...", "name": "..."}
"""

import csv

dict = {}

with open('emails.csv', newline='') as file:
    rows = csv.reader(file, delimiter=',')
    for row in rows:
        if(row[2] != ""):
            dict[row[0]] = {"email": row[2], "name": row[1].title()}
