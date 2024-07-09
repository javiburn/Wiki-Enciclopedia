# Wiki Encyclopedia

This is a Django-based project to create a Wikipedia-like online encyclopedia where users can view, search, create, edit, and browse encyclopedia entries written in Markdown.

## Table of Contents
- [Background](#background)
- [Features](#features)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [License](#license)

## Background
Wikipedia is a free online encyclopedia with numerous entries on various topics. Each entry can be viewed by visiting its dedicated page. Writing all entries in HTML can be tedious, so we use Markdown to make it easier to write and edit entries. This project converts Markdown content into HTML for display.

## Features
1. **Entry Page**: View an encyclopedia entry by visiting `/wiki/TITLE`. If the entry exists, its content is displayed; otherwise, an error page is shown.
2. **Index Page**: Displays a clickable list of all encyclopedia entries.
3. **Search**: Users can search for entries. If a match is found, the user is redirected to the entry page. If not, a list of partial matches is shown.
4. **New Page**: Users can create new encyclopedia entries.
5. **Edit Page**: Users can edit existing entries.
6. **Random Page**: Users can view a random encyclopedia entry.
7. **Markdown to HTML Conversion**: Converts Markdown content to HTML for display.

## Getting Started
1. **Download the Project**: Download the project from [this link](https://cdn.cs50.net/web/2020/spring/projects/1/wiki.zip) and unzip it.
2. **Install Dependencies**: Ensure you have Python and Django installed. Install the required packages:
    ```bash
    pip install django markdown2
    ```
3. **Run the Server**: Navigate to the project directory and start the Django server:
    ```bash
    python manage.py runserver
    ```
4. **Access the Application**: Open your web browser and go to `http://127.0.0.1:8000`.

## Project Structure
The project contains a Django project called `wiki` with a single app called `encyclopedia`.

- **encyclopedia/urls.py**: Defines URL routes.
- **encyclopedia/util.py**: Contains utility functions for interacting with encyclopedia entries.
    - `list_entries()`: Returns a list of all entry names.
    - `save_entry(title, content)`: Saves an entry with the given title and Markdown content.
    - `get_entry(title)`: Retrieves the entry with the given title.
- **encyclopedia/views.py**: Defines views for the application.
    - `index`: Displays the index page with all entries.
    - `entry_page`: Displays a specific entry.
    - `search`: Handles search functionality.
    - `new_page`: Allows users to create new entries.
    - `edit_page`: Allows users to edit existing entries.
    - `random_page`: Redirects to a random entry.
- **encyclopedia/templates/encyclopedia**: Contains HTML templates for the application.
    - `index.html`: Template for the index page.
    - `entry.html`: Template for displaying an entry.
    - `new_page.html`: Template for creating a new entry.
    - `edit_page.html`: Template for editing an entry.
    - `layout.html`: Base layout template.

## Usage
1. **View Entries**: Click on an entry title on the index page to view its content.
2. **Search Entries**: Use the search bar to find entries. Exact matches redirect to the entry page, while partial matches show a list of results.
3. **Create New Entry**: Click "Create New Page" in the sidebar, enter a title and Markdown content, and save the entry.
4. **Edit Entry**: Click "Edit" on an entry page, modify the content, and save the changes.
5. **Random Entry**: Click "Random Page" to view a random entry.

## License
MIT License

2024 Javier Sarabia

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
