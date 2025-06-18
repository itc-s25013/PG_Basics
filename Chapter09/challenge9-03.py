import csv

movies = [
    ["Top Gun", "Risky Business", "Minority Report"],
    ["Titanic", "The Revenant", "inception"],
    ["Training Day", "Man on Fire", "Flight"]
]

with open("movies.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in movies:
        writer.writerow(row)
