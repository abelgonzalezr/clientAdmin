# Client and Address Management App

This Django application allows you to manage clients and their addresses for company X.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/abelgonzalezr/clientAdmin
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser (admin) account:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create your superuser account. Use the following credentials for the initial admin account:

   - Username: admin
   - Password: admin

## Usage

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Open your web browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to access the admin interface.

3. Log in using the admin credentials you created earlier.

4. You can now manage clients and their addresses through the admin interface.

## Additional Notes

- Make sure you have Python and Django installed on your system.
- The application uses SQLite as the default database. 

