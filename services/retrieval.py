import json

with open("data/shl_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)


def search_assessments(query):

    query = query.lower()

    results = []

    for item in catalog:

        score = 0

        for skill in item["skills"]:

            if skill.lower() in query:
                score += 1

        if score > 0:

            results.append({
                "name": item["name"],
                "url": item["url"],
                "test_type": item["test_type"],
                "score": score
            })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results[:10]