import gzip
import json

reviews = []

# Unzips the file and saves json to f
with gzip.open("goodreads_reviews_spoiler_raw.json.gz", "rt", encoding="utf-8") as f:
    for i, line in enumerate(f):
        review = json.loads(line)
        reviews.append(review)

        if len(reviews) == 3:
            break

for i in reviews:
    print(i)
# NOTES FOR DATA EXTRACTION
# Stream through the json file instead of completely loading everything since its HUGE
# First attempt, do a mix of 8000 non spoiler to 2000 poilers
# Get this by stratified sampling, where we create two seperate pools or spoilers and non-spoilers
# Then we fill them with the values in the JSON and once non-spoilers reach 8000 and spoilers reach 2000 we stop
# Each pool should be ["(REVIEW)", x] with x being either 1 or 0, refering to spoiler or non-spoiler

# Dataset contains explicit (view spoiler) (hide spoiler) in reviews with spoilers, so we need to remove that else the model will train on that
# Since data has book_id we can avoid capturing multiple reviews on the same book else the model will train on book specific information (Data leakage consideration)