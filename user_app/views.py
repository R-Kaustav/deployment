from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def UserProjectHomePage(request):
    return render(request,'user_app/UserProjectHomePage.html',)


def weatherintegration(request):
    return render(request,'user_app/weatherintegration.html')


from django.http import JsonResponse

from django.shortcuts import render
from django.http import JsonResponse
import requests

API_KEY = 'e77153ac7e627cd798e837deadcb64dd'

def weatherintegration(request):
    return render(request, 'user_app/weatherintegration.html')

def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        if not city:
            return JsonResponse({'error': 'City not provided'}, status=400)

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            return JsonResponse(response.json())
        elif response.status_code == 404:
            return JsonResponse({'error': 'City not found'}, status=404)
        else:
            return JsonResponse({'error': 'Failed to fetch weather data'}, status=response.status_code)

    return JsonResponse({'error': 'Invalid request'}, status=400)



# views.py
from django.http import JsonResponse
from django.shortcuts import render
import google.generativeai as ai

# Configure the API
GOOGLE_API_KEY = 'AIzaSyBHGTutXxMVqKsJq9EmowT2Uo5EJ_E2rlI'
ai.configure(api_key=GOOGLE_API_KEY)
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        if user_message.lower() == 'bye':
            return JsonResponse({'response': 'Goodbye!'})
        response = chat.send_message(user_message)
        return JsonResponse({'response': response.text})
    return render(request, 'user_app/chatbot.html')



#
# import openai
# from django.http import JsonResponse
# from django.shortcuts import render
# from django.conf import settings
# from django.conf import settings
#
# import openai
# from django.http import JsonResponse
# from django.shortcuts import render
#
# def chatbot_view(request):
#     if request.method == 'POST':
#         user_input = request.POST.get('message')
#
#         if user_input:
#             try:
#                 openai.api_key = settings.OPENAI_API_KEY  # Access the API key from settingws
#
#                 # ... rest of your chatbot logic using the OpenAI API ...
#
#                 return JsonResponse({'response': bot_response})
#
#             except openai.error.OpenAIError as e:
#                 # Handle OpenAI API errors
#                 return JsonResponse({'error': f"OpenAI error: {e.message}"}, status=500)
#             except Exception as e:
#                 # Handle other exceptions
#                 return JsonResponse({'error': f"Something we wrong: {str(e)}"}, status=500)
#         else:
#             return JsonResponse({'error': 'Message is empty'}, status=400)
#
#     return render(request, 'user_app/chatbot.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FeedbackForm
from .models import Feedback

# Existing feedback form view
def feedback_form_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save feedback to the database
            return redirect('thank_you')  # Redirect to a thank you page or success message
    else:
        form = FeedbackForm()

    return render(request, 'user_app/feedback_form.html', {'form': form})

# New view to handle form submission (redirects to thank you page)
def submit_feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save feedback to the database
            return redirect('user_app:thank_you')  # Redirect to thank you page or success message
    return redirect('user_app:feedback_form')  # If POST is not valid, return to form


from django.shortcuts import render, redirect
from datetime import datetime

# In-memory storage for plants and growth records
plants = []
growth_records = []

def plant_tracker(request):
    if request.method == 'POST':
        if 'add_plant' in request.POST:  # Handle Add Plant form
            name = request.POST['name']
            species = request.POST['species']
            planted_date = request.POST['planted_date']
            last_watered_date = request.POST['last_watered_date']
            # Append new plant to plants list
            plants.append({
                'id': len(plants) + 1,
                'name': name,
                'species': species,
                'planted_date': planted_date,
                'last_watered_date': last_watered_date,
            })
        elif 'add_growth_record' in request.POST:  # Handle Add Growth Record form
            plant_id = int(request.POST['plant_id'])
            date = request.POST['date']
            height_cm = float(request.POST['height_cm'])
            notes = request.POST.get('notes', '')
            # Append new growth record to growth_records list
            growth_records.append({
                'id': len(growth_records) + 1,
                'plant_id': plant_id,
                'date': date,
                'height_cm': height_cm,
                'notes': notes,
            })
        return redirect('plant_tracker')

    # Prepare data for template
    for plant in plants:
        # Fetch related growth records for each plant
        plant['growth_records'] = [record for record in growth_records if record['plant_id'] == plant['id']]

    # Debugging: Output plants and growth records to the console to verify they exist
    print(f"Plants: {plants}")
    print(f"Growth Records: {growth_records}")

    return render(request, 'plants/plant_tracker.html', {'plants': plants})
