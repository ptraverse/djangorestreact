# SWU

#### aka Python + Django + Node + Bower

Python/Django backend with a javascripty frontend.

Maybe Adding Electron at the end FTW!

#### Why

Launching a chromebrowser to run a v8 to communicate with a django WSGI server!? Yes it is overengineering.

But Python is FAST and awesome. And JS still has the best front end. And it should be easier than it sounds.

#### Build

Install Python, NodeJS, and Bower Modules
`npm install`

Run Latest Migrations, Update Modules -> python backend/manage.py migrate
`npm update`

Activate the environment, start the django server, start the nodeJs server
`npm start`

Tests (haha)
`npm test`

Give yourself an Admin -> python backend/manage.py createsuperuser
`npm run createsuperuser`