# ContactSite(Under Construction)


The website contains real time contact sharing with administrator.<br />
<b>Before cloning the repository, follow the below steps sincerely otherwise you will catch in trouble.</b>
<ul>
<li>Activate your virtual environment.</li>
<li>Your environment must have django installed. If not, then hit the command <i>python3 -m pip install django</i> </li>
<li>Install docker by following link https://www.docker.com/get-started</li>
<li>Install redis server by hitting the command- python3 -m pip install channels_redis</li>


</ul>

<b>After setting up above installation which hardly took 10-15 minutes of time, 
<ul>
<li>Initialize the redis server by following command-</b></li>
<i>sudo docker run -p 6379:6379 -d redis:5</i>
<li>Migrate the database by hitting command-</li>
<i>python3 manage.py migrate</i>

<li>Start the ASGI server by hitting command-</li>
<i>python3 manage.py runserver</i>

</ul>
<br />
<h3>After the server run successfully</h3>
<b>Go to </b>http://127.0.0.1:8000/chat/
<br />
<b>Open other browser in private mode and goto</b>
http://127.0.0.1:8000/admin_dashboard/
<p> and logged in using username = 'admin' and password = 'admin'</p>
