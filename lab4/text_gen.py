from ollama import generate

MODEL = "llama3"

while True:
    prompt = input("Введіть запит (або 'exit'): ")

    if prompt.lower() == "exit":
        print("Завершення програми.")
        break

    response = generate(MODEL, prompt)
    print("\nРезультат:\n", response['response'], "\n")