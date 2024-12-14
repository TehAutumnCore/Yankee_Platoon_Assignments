# Documentation

Overview: 
A Netflix UI meets Steam and Twitch for gamers to discover, organize, and manage their game library. Users can browse through games categorized by genre or popularity using the steam API to view game details with relevant information such as the image, description, release date, developer, publisher price and will show relevant live streams of that game using the Twitch API. Users will also have a personalized profile where they can organize their game library and leave reviews

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
- requests
- requests_oauthlib

## API Keys IN .ENV
### How to get Django secret key: 
<!-- Django_Secret_key(.env) -->
python manage.py shell
- DJANGO_SECRET_KEY 
 from django.core.management.utils import get_random_secret_key
 new_key = get_random_secret_key()
 new_key
- STEAM_WEB_API_KEY


# Applications

## Users App
This application will handle the User authentication and account management
### Features 
- User Registration
- Login/LogOut
- Token Based Authentication
- \user Profiles (TBD)
- \Relationship with user-owned games and reviews (TBD)


## Game App
- CRUD for games (ability to create, update, and delete custom game entries)
- Game details, including title description images, videos and price
- Categorization of games by genre popularity or release date
- Integration with the Twitch API to display live streams related to games
- search and filter functionality for games

## Library App
- CRUD for user game Libraries( add, remove, and update, and delete games in a user's library)
- Automatically import games from a public steam library? (TBD)
- Categorize games in the library by genre, completion status, or other criteria
-Manage relationships between users and their games (many to many relationship)


## Reviews App 
- CRUD for user reviews (create,read,update, delete)
-user can leave a review or rating for a game
- display all reviews for a specific game
- filter reviews by user or rating score
- Associate reviews with users and games 








------------------------------------------------------------------------------------------------------------------------------

 ## Frontend
 - Run application: npm run dev

 ### Installs
 - axios
 - react-router-dom 
 - bootstrap/tailwind?



-link the backend to front end


Token/UserAuthentication is today's goal:
 https://github.com/Code-Platoon-Assignments/Django_auth 
 https://github.com/Code-Platoon-Curriculum/curriculum/tree/main/07-Django/CheatSheets
 https://github.com/Code-Platoon-Curriculum/yankee_demos_and_notes/blob/main/07-Django/8-review/user_app/views.py
 Full Stack Auth: https://www.youtube.com/watch?v=19LB0mkCgfI&list=PLu0CiQ7bzwES91fzg7uQLWTvW1upYUeru&index=1



# Figma
 - https://www.figma.com/design/xUBx7Si5GxCRa4Bje8XWar/Game-Management-Proj?node-id=0-1&p=f&t=24nmK5cvGzijor7S-0

Plugin - Builder.io 