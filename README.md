TownHall
========
Townhall API and initial front-end implementation.

Wiki: https://github.com/TownHall/TownHall/wiki

---------------

To get the project running locally, execute the following steps:
1) Get startscript.sh
2) Execute: . ./startscript.sh
3) Decide where you are keeping your static files in your directory tree and edit 
     TownHall/TownHall/settings.py line 105 
   and
     TownHall/server.txt line 7
   accordingly
4) Update the name of your server in 
     TownHall/server.txt line 2
5) startscript.sh automatically starts the gunicorn server as a background process. Make sure to restart the server 
   to include any changes you've made:
     jobs
     kill %< the number of the of the job running the gunicorn server > 
     sudo service nginx restart
     gunicorn -b 0.0.0.0:8000 TownHall.wsgi:application &

----------------     
     
Alternatively, if you clone/pull/checkout the github files first, simply do steps 3-5, comment lines 31-32 and run 
     . ./startscript.sh
