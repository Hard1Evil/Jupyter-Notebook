from ollama import chat

path = input("Введіть шлях до зображення: ")

response = chat(
    model='llama3',
    messages=[
        {
            'role': 'user',
            'content': 'Що зображено на цьому фото?',
            'images': [path],
        }
    ],
)

print("\nВідповідь:\n", response['message']['content'])