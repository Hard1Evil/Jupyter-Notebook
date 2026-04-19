from ollama import chat

messages = []

print("Чат-бот запущено! Напишіть 'exit' для виходу.\n")

while True:
    user_input = input("Ти: ")
    
    if user_input.lower() == "exit":
        print("Чат завершено.")
        break

    # додаємо написане повідомлення 
    messages.append({
        'role': 'user',
        'content': user_input,
    })

    # відповідь моделі
    response = chat('llama3', messages=messages)

    bot_reply = response['message']['content']

    # додаємо відповідь моделі в історію
    messages.append({
        'role': 'assistant',
        'content': bot_reply,
    })

    print("Бот:", bot_reply)