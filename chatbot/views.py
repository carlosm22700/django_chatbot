from django.shortcuts import render
from django.http import JsonResponse
import openai
import os
from transformers import pipeline

# Create your views here.

# This line is for debugging. Print the value of the API key to console.
print("API Key from env:", os.environ.get('OPENAI_API_KEY'))

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


# def ask_huggingface_model(message):
#     generator = pipeline('text-generation', model='gpt2-medium')

#     # Generate responses
#     responses = generator(f"{message}\n\n", max_length=100,
#                           num_return_sequences=1, temperature=0.5)

#     # Extract the text from the first response and remove the prompt from the output
#     answer = responses[0]['generated_text'].strip().replace(
#         message, '').strip()

#     return answer


def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
