# PERSONAL JOURNALING APPLICATION

## Project Description
<p>This project consists of a mobile application and a backend service for personal journaling. Users are be able to write journal entries, categorize them, and view a summary of their entries.<br>
The mobile application is built using React Native while the backend  service is built using Django(Python Framework).<br>
The relational database used is MySQL.</p>

## Features
#### Mobile Application
<ol>
<li>User Authentication
<ul><li>Allow users to sign up and log in.</li></ul>
</li>
<li>Journal Entry Management
<ul>
<li>Add new journal entries with a title, content, category, and date.</li>
<li>Edit and delete existing entries</li>
</ul>
</li>
<li>Journal View
<ul><li>Allow users to view a list of all their journal entries.</li></ul>
</li>
<li>Categorization
<ul><li>Users should be able to categorize their entries e.g. Personal, Work, Travel, etc.</li></ul>
</li>
<li>Summary View
<ul><li>Display a summary of journal entries over a selected period i.e. daily, weekly, monthly.</li></ul>
</li>
<li>Settings
<ul><li>Allow users to update their username and password.</li></ul>
</li>
</ol>

#### Backend Service
<ol>
<li>User Management
<ul>
<li>User registration and authentication (JWT or session-based).</li>
<li>Profile management.</li></ul>
</li>
<li>Journal Entry Management
<ul><li>CRUD operations for journal entries.</li>
<li>Categorization of entries.</li></ul>
</li>
<li>Data Summary
<ul><li>Endpoints to fetch summary data for given periods.</li></ul>
</li>
<li>Security
<ul><li>Ensure all endpoints are secure and accessible only by authenticated users.</li></ul>
</li>
</ol>

## Execution
<ul>
<b>First make sure you have Python installed in your machine</b>
<li>Create a virtual environment for the backend using the following command:
<code>python -m venv env</code></li>
<li>Activate the virtual environment using the following command:
<code>source env/bin/activate</code> - <b>Linux</b>
<code>env\Scripts\activate</code> - <b>Windows</b></li>
<li>Add the required dependencies in the virtual environment using the following command:
<code>pip install -r requirements.txt</code>
<li>Execute the backend using the following command:
<code>python manage.py runserver</code></li>
</ul>

## API

#### Authentication
<ul>
<li><b>Sign Up: </b><code>http://127.0.0.1:8000/users/register</code></li>
<li><b>Sign In: </b><code>http://127.0.0.1:8000/users/login</code></li>
<li><b>Sign Out: </b><code>http://127.0.0.1:8000/users/logout</code></li>
</ul>

#### Show Journals and Categories:
<ul>
<li><code>http://127.0.0.1:8000/categories</code></li>
<li><code>http://127.0.0.1:8000/journals</code></li>
</ul>

#### Find a journal and a category:
<ul>
<li><code>http://127.0.0.1:8000/category/:id</code>
</li>
<li><code>http://127.0.0.1:8000/journal/:id</code></li>
</ul>

#### Create a journal and a category:
<ul>
<li><code>http://127.0.0.1:8000/category/add/</code></li>
<li><code>http://127.0.0.1:8000/journal/add/</code></li>
</ul>

#### Edit an existing journal and a category:
<ul>
<li><code>http://127.0.0.1:8000/category/edit/:id</code>
</li>
<li><code>http://127.0.0.1:8000/journal/edit/:id</code></li></ul>

#### Delete a journal and a category:
<ul><li><code>http://127.0.0.1:8000/category/delete/:id</code>
</li><li><code>http://127.0.0.1:8000/journal/delete/:id</code></li></ul>

#### Journals summary
<ul><li><code>http://127.0.0.1:8000/journals/summary</code>
</li></ul>