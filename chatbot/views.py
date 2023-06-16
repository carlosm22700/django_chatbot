from django.shortcuts import render
from django.http import JsonResponse
import openai
import os


openai.api_key = os.environ.get('OPENAI_API_KEY')


def ask_openai(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()
    return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
