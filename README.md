# CSV Data Validation and Storage System

![CSV Data Validation and Storage System](screenshot.png)

The CSV Data Validation and Storage System is a web application developed using Django, a Python web framework. It allows users to upload CSV files, validate the data, store the valid entries in a database, and perform various operations on the stored data.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## Installation
To run the CSV Data Validation and Storage System locally, follow these steps:

1. Clone the repository from GitHub:
   ```shell
   git clone https://github.com/your-username/csv-data-validation.git
   ```
   
2. Change to the project directory:
   ```shell
   cd csv-data-validation
   ```

3. Create a virtual environment (optional but recommended):
   ```shell
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```shell
   python manage.py migrate
   ```

6. Start the development server:
   ```shell
   python manage.py runserver
   ```

7. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Usage
The CSV Data Validation and Storage System provides the following functionality:

1. Upload CSV File: Users can upload a CSV file containing user data using the provided form. The system will validate each row of data for completeness, uniqueness, and data type conformity.

2. Summary Report: After uploading a CSV file, a summary report will be displayed showing the total number of data rows, successfully uploaded rows, duplicate rows, invalid rows, and incomplete rows.

3. Duplicate Rows: If duplicate rows are found in the uploaded CSV file, they will be displayed in a separate table along with the reason for duplication.

4. Invalid Rows: If any rows in the CSV file contain invalid data, they will be listed in a separate table along with the reason for the invalidity.

5. List Users: Users can view a list of all stored users. The list can be filtered based on name, email, phone number, gender, and address.

6. Delete User: Users can delete individual users from the system by clicking the "Delete" button next to each user entry in the list.

## Features
The CSV Data Validation and Storage System offers the following features:

- User-friendly web interface for uploading and managing CSV data.
- CSV data validation to ensure data completeness and conformity.
- Storage of valid user data in a database for easy retrieval and management.
- Summary report displaying statistics of the uploaded data, including duplicates and invalid entries.
- Filtering of user data based on various attributes.
- Secure user authentication and authorization.
- Responsive and intuitive design using Bootstrap CSS framework.
- Scalable and extensible architecture for future enhancements.

## Screenshots
Here are some screenshots of the CSV Data Validation and Storage System:

1. Upload CSV File Form:
   ![Upload CSV File Form](screenshots/upload_csv.png)

2. Summary Report:
   ![Summary Report](screenshots/summary_report.png)

3. Duplicate Rows:
   ![Duplicate Rows](screenshots/duplicate_rows.png)

4. Invalid Rows:
   ![Invalid Rows](screenshots/invalid_rows.png)

5. List Users:
   ![List Users](screenshots/list_users.png)

## Contributing
Contributions to the CSV Data Validation

 and Storage System are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository. If you'd like to contribute code, you can fork the repository, make your changes, and submit a pull request.

When contributing to this project, please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md).

## License
The CSV Data Validation and Storage System is open-source software licensed under the [MIT License](LICENSE).