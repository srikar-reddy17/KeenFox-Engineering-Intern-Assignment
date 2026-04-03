import json
import time
import os
from scraper import get_competitor_data
from analyzer import analyze_competitor
from recommender import generate_recommendations
from utils import compute_diff


def main():
    print("Running Competitive Intelligence System...\n")

    raw_data = get_competitor_data()

    previous_data = {}
    if os.path.exists("outputs/report.json"):
        with open("outputs/report.json") as f:
            previous_data = json.load(f).get("competitor_insights", {})

    all_insights = {}

    for name, data in raw_data.items():
        combined = str(data)

        if name in previous_data and previous_data[name] == combined:
            print(f"Skipping {name}, no change")
            all_insights[name] = previous_data[name]
        else:
            print(f"Updating {name}...")
            insights = analyze_competitor(name, combined)
            all_insights[name] = insights
            time.sleep(2)

    print("\nGenerating recommendations...\n")

    recommendations = generate_recommendations({
        "previous": previous_data,
        "current": all_insights
    })

    diff = compute_diff("outputs/report.json", all_insights)

    os.makedirs("outputs", exist_ok=True)

    final_output = {
        "diff": diff,
        "competitor_insights": all_insights,
        "recommendations": recommendations
    }

    with open("outputs/report.json", "w") as f:
        json.dump(final_output, f, indent=4)

    print("Done. Check outputs/report.json")


if __name__ == "__main__":
    main()