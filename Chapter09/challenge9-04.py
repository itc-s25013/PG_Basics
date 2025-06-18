import csv

movies = [
    ["トップガン", "卒業白書", "マイノリティ・リポート"],
    ["タイタニック", "レヴェナント", "インセプション"],
    ["トレーニングデイ", "マイ・ボディーガード", "フライト"]
]

with open("movies_ja.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in movies:
        writer.writerow(row)

