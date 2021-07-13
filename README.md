# A_Hitchhikers_Bucket_List 

An application I completed while consolidating my knowledge of using python to create full-stack applications. The app is 
thematically based on Douglas Adams Hitchhikers Guide to the Galaxy.  

The application is written primarily in Python with Jinja used for front-end HTML templating. Flask is used to run the server 
and routes are written according the RESTful principles. The database is relaional and handled using PSQL.

In order to run this application please:

1. Fork this repository
2. Navigate to the application folder
3. Instal flask with the command - pip install Flask
3. If you do not have psql installed please:
   intall Brew Package Manager - /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   and then symlink psql - brew link --force libpq ail
4. Create the database with command - createdb hitchhike_manager
5. Run the database with command - psql -d hitchhike_manager -f db/hitchhike_manager.sql
6. Initialize the server with command - flask run
7. In you web browser navigate to http://localhost:5000
