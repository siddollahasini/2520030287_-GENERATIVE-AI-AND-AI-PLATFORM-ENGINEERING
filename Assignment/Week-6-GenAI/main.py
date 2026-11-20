
import json
import csv
import requests
from datetime import datetime

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"
INPUT_FILE = "golden_set.json"
OUTPUT_FILE = "baseline_results.csv"


def get_llm_answer(question):
    payload = {
        "model": MODEL_NAME,
        "prompt": question,
        "stream": False,
        "options": {"temperature": 0}
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )
    response.raise_for_status()
    return response.json().get("response", "").strip()


def calculate_score(answer, expected_keywords):
    answer = answer.lower()
    matched = []
    missing = []

    for keyword in expected_keywords:
        if keyword.lower() in answer:
            matched.append(keyword)
        else:
            missing.append(keyword)

    score = (
        len(matched) / len(expected_keywords) * 100
        if expected_keywords else 0
    )

    return round(score, 2), matched, missing


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        golden_questions = json.load(file)

    print("\n======================================")
    print("GOLDEN QUESTION SET")
    print("======================================")
    print("Total Questions:", len(golden_questions))
    print("Model:", MODEL_NAME)

    results = []
    total_score = 0
    successful_questions = 0

    print("\nBASELINE RUN STARTED")

    for index, item in enumerate(golden_questions, start=1):
        question_id = item["id"]
        question = item["question"]
        expected_answer = item["expected_answer"]
        keywords = item["keywords"]
        source = item["source"]

        print("\n--------------------------------------")
        print(f"Question {index}: {question_id}")
        print("Question:", question)

        try:
            answer = get_llm_answer(question)
            score, matched, missing = calculate_score(
                answer, keywords
            )

            status = "PASS" if score >= 60 else "REVIEW"

            total_score += score
            successful_questions += 1

            print("LLM Answer:", answer)
            print("Expected Answer:", expected_answer)
            print("Matched Keywords:", matched)
            print("Missing Keywords:", missing)
            print("Score:", score, "%")
            print("Status:", status)

            results.append({
                "Question_ID": question_id,
                "Question": question,
                "Expected_Answer": expected_answer,
                "LLM_Answer": answer,
                "Matched_Keywords": ", ".join(matched),
                "Missing_Keywords": ", ".join(missing),
                "Score": score,
                "Status": status,
                "Source": source,
                "Model": MODEL_NAME,
                "Release": "v0.1"
            })

        except Exception as error:
            print("Error:", error)

            results.append({
                "Question_ID": question_id,
                "Question": question,
                "Expected_Answer": expected_answer,
                "LLM_Answer": "",
                "Matched_Keywords": "",
                "Missing_Keywords": ", ".join(keywords),
                "Score": 0,
                "Status": "ERROR",
                "Source": source,
                "Model": MODEL_NAME,
                "Release": "v0.1"
            })

    fieldnames = [
        "Question_ID", "Question", "Expected_Answer",
        "LLM_Answer", "Matched_Keywords", "Missing_Keywords",
        "Score", "Status", "Source", "Model", "Release"
    ]

    with open(
        OUTPUT_FILE, "w", newline="", encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    average_score = (
        total_score / successful_questions
        if successful_questions else 0
    )

    passed = sum(r["Status"] == "PASS" for r in results)
    review = sum(r["Status"] == "REVIEW" for r in results)
    errors = sum(r["Status"] == "ERROR" for r in results)

    print("\n======================================")
    print("BASELINE EVALUATION SUMMARY")
    print("======================================")
    print("Release Version: v0.1")
    print("Model:", MODEL_NAME)
    print("Total Questions:", len(golden_questions))
    print("Successful Responses:", successful_questions)
    print("Passed Questions:", passed)
    print("Questions for Review:", review)
    print("Failed Requests:", errors)
    print("Average Keyword Coverage:", round(average_score, 2), "%")
    print("Evaluation Date:", datetime.now())
    print("\nResults saved to:", OUTPUT_FILE)
    print("\nBASELINE RUN COMPLETED!")
    print("Release v0.1 created successfully.")


if __name__ == "__main__":
    main()
