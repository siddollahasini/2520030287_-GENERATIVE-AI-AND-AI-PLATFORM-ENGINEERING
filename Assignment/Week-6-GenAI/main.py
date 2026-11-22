
import json
import csv
import urllib.request
import urllib.error
import time

# Load golden questions
with open("golden_set.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

model = "llama3.2"

results = []

print("WEEK 6 - BASELINE EVALUATION")
print("-" * 40)

for item in questions:
    question = item["question"]
    expected = item["expected_answer"]

    print("\nQuestion:", question)

    data = {
        "model": model,
        "prompt": question,
        "stream": False
    }

    request = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        start_time = time.time()

        with urllib.request.urlopen(request, timeout=120) as response:
            output = json.loads(response.read().decode("utf-8"))

        latency = round(time.time() - start_time, 2)
        generated = output.get("response", "").strip()

        print("Generated Answer:", generated)
        print("Response Time:", latency, "seconds")

        results.append({
            "question_id": item["id"],
            "question": question,
            "expected_answer": expected,
            "generated_answer": generated,
            "response_time_seconds": latency
        })

    except Exception as error:
        print("Error:", error)

# Save baseline results
with open("baseline_results.csv", "w", newline="", encoding="utf-8") as file:
    columns = [
        "question_id",
        "question",
        "expected_answer",
        "generated_answer",
        "response_time_seconds"
    ]

    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(results)

print("\nBaseline evaluation completed.")
print("Results saved in baseline_results.csv")
print("Successful responses:", len(results), "/", len(questions))
