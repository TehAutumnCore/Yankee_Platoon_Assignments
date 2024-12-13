# Documentation

## Backend
- Run Server: python manage.py runserver
### Design Links
- TLDRAW: https://www.tldraw.com/r/yqfLU5tQwFDD8CLtt-Yf9?d=v-3921.-1404.4834.2500.page
- Google Doc: https://docs.google.com/document/d/1nveAsm-VF83PyCnX_b5QLmactWHrVh3T-Ccsy8QkR6c/edit?tab=t.0
- Draw SQL:https://drawsql.app/teams/franciscos-team-2-1/diagrams/full-stack-personal-project-game-inventory-management-system

### API Integration
- Steam Web API Documentation: https://steamcommunity.com/dev
- game(steam): https://store.steampowered.com/app/730/CounterStrike_2/
- Twitch API Documentation: https://dev.twitch.tv/docs/api/
- game(twitch): https://www.twitch.tv/directory/category/counter-strike

### Installs
- Django
- Psychopg[binary] (allows django to talk to postgresql)
- djangorestframework (allows use of Response, APIView, TokenAuthentication)
- django-cors-headers (allows backend to communicate with front end)
- python-dotenv
- 

### Django_Secret_key(.env)
python manage.py shell
- from django.core.management.utils import get_random_secret_key
 new_key = get_random_secret_key()
 new_key



 ## Frontend
 - Run application: npm run dev

 ### Installs
 - axios
 - react-router-dom 
 - bootstrap/tailwind?



 Config React router
 link the backend to front end