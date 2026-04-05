# evaluation/evaluator.py

import json
from main import run_query


def load_test_cases(path="evaluation/test_cases.json"):
    with open(path, "r") as f:
        return json.load(f)


def evaluate():
    test_cases = load_test_cases()

    correct = 0
    total = len(test_cases)

    for i, case in enumerate(test_cases):
        question = case["question"]
        expected = case["expected_answer"]

        print(f"\nTest {i+1}: {question}")

        answer, docs = run_query(question)

        print("Answer:", answer)
        print("Expected:", expected)

        # Simple check (can improve later)
        if expected.lower() in answer.lower():
            print("Result: PASS")
            correct += 1
        else:
            print("Result: FAIL")

    accuracy = correct / total
    print(f"\nFinal Accuracy: {accuracy * 100:.2f}%")