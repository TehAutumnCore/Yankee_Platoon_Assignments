import requests
from django.conf import settings
import os

BASE_URL = "https://store.steampowered.com/api"
API_KEY = settings.STEAM_WEB_API_KEY

def get_action_games():
    print("Starting Steam API call")
    url = f"{BASE_URL}/featuredcategories"
    response = requests.get(url)
    
    if response.ok:
        data = response.json()
        action_games = []
        
        # Get games from specials section
        for item in data.get('specials', {}).get('items', []):
            # For now, let's assume all these games are action games
            # We can refine this later with another API call to get detailed genres
            game_data = {
                'title': item.get('name'),
                'price': float(item.get('final_price', 0)) / 100,  # Convert cents to euros/dollars
                'description': f"A featured game on Steam", # We'll get real descriptions later
                'genre': 'Action',  # Default to Action for now
                'image_url': item.get('large_capsule_image'),
                'steam_app_id': str(item.get('id')),
                'sale': item.get('discounted', False)
            }
            action_games.append(game_data)
            print(f"Added game: {game_data['title']}")
        
        # Take only the first 5 games for testing
        return action_games[:5]
    return []