import requests
from datetime import datetime

APP_ID = 'ef3d0872'
API_KEY = '93bcd99eea4e5f7d1d08659c79fe7622'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

exercise_url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
exercise_input = input('What did you do today? ')
exercise_params = {
    'query': exercise_input,

}

response = requests.post(headers=headers, url=exercise_url, json=exercise_params)
result = response.json()['exercises']


sheety_api = "https://api.sheety.co/d94938767e674b079fe4e62bad71b9bb/dennis'sWorkouts/workouts"
headers1 = {
    'Authorization': 'Bearer fjfosjfo2ui8974hru297-a[ofjna;fuio'
}
today = datetime.now()

for exercise in result:
    
    sheety_params ={
        'workout': {
            'date': f"{today.strftime('%d/%m/%Y')}",
            'time': f"{today.strftime('%H:%M:%S')}",
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }

    response = requests.post(url=sheety_api, json=sheety_params, headers=headers1)
    print(response.text)
