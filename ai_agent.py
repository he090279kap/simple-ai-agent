import openai
import config  # Файл с API-ключом

def chat_with_ai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Ошибка: {e}"

if __name__ == "__main__":
    print("🤖 AI Agent запущен! Напишите 'exit' для выхода.")
    while True:
        user_input = input("Вы: ")
        if user_input.lower() == "exit":
            print("👋 До свидания!")
            break
        response = chat_with_ai(user_input)
        print(f"🤖 AI: {response}")
