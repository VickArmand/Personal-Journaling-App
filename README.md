# PERSONAL JOURNALING APPLICATION

## Project Description

<p>This project consists of a mobile application and a backend service for personal journaling. Users are be able to write journal entries, categorize them, and view a summary of their entries.<br>
The mobile application is built using React Native while the backend service is built using Django Rest(Python Framework).<br>
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
<li>User registration and authentication (session-based).</li>
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

#### Backend Service

<ul>
<b>First make sure you have Python and MySQL installed in your machine</b>
<li>Start the sql service in your machine</li>
<li>Create a database named <b>Journalsappdb</b></li>
<li>Create a virtual environment for the backend using the following command:
<code>python -m venv env</code></li>
<li>Activate the virtual environment using the following command:
<code>source env/bin/activate</code> - <b>Linux</b>
<code>env\Scripts\activate</code> - <b>Windows</b></li>
<li>Add the required dependencies in the virtual environment using the following command:
<code>pip install -r requirements.txt</code>
<li>Add tables to the database using <code>python manage.py makemigrations</code> and <code>python manage.py migrate</code></li>
<li>Execute the backend using the following command:
<code>python manage.py runserver</code></li>
</ul>

#### Mobile Application

<ul>
<li>Navigate to the mobile directory on your command prompt</li>
<li>Run <code>npm install</code> to add the required node modules in your machine</li>
<li>Run <code>npm start</code> and select which platform to execute the application on</li>
</ul>

## API

#### Authentication

<ul>
<li><b>Sign Up: </b><code>/users/register</code></li>
<li><b>Sign In: </b><code>/users/login</code></li>
<li><b>Sign Out: </b><code>/users/logout</code></li>
</ul>

#### Show Journals and Categories:

<ul>
<li><code>/categories</code></li>
<li><code>/journals</code></li>
</ul>

#### Find a journal and a category:

<ul>
<li><code>/category/:id</code>
</li>
<li><code>/journal/:id</code></li>
</ul>

#### Create a journal and a category:

<ul>
<li><code>/category/add/</code></li>
<li><code>/journal/add/</code></li>
</ul>

#### Edit an existing journal and a category:

<ul>
<li><code>/category/edit/:id</code>
</li>
<li><code>/journal/edit/:id</code></li></ul>

#### Delete a journal and a category:

<ul><li><code>/category/delete/:id</code>
</li><li><code>/journal/delete/:id</code></li></ul>

#### Journals summary

<ul><li><code>/journals/summary</code>
</li></ul>
