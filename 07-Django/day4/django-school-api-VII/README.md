# School API VII

By the end of this assignment you will have a fully serviceable CRUD API with user authentication capabilities that will allow School staff to easily manage students and scholastic equipment.

## A Students

Build an API endpoint of `http://127.0.0.1:8000/api/v1/students/3/` with the name of `a_students`, that will return a students inside the the database in the following format or a 404 Response:

```json
{
  "name": "Francisco R. Avila",
  "student_email": "francisco@school.com",
  "personal_email": "francisco@gmail.com",
  "locker_number": 1,
  "locker_combination": "12-12-12",
  "good_student": true,
  "subjects": [
    {
      "subject_name": "Python",
      "professor": "Professor Adam",
      "students": 6,
      "grade_average": 54.05
    }
  ]
}
```

## A Subjects

Build an API endpoint of `http://127.0.0.1:8000/api/v1/subjects/python/` with the name of `a_subjects`, that will return a subjects inside the the database in the following format or a 404 Response:

```json
{
  "subject_name": "Python",
  "professor": "Professor Adam",
  "students": 6,
  "grade_average": 54.05
}
```

## Running Tests

Delete all the test files inside of each individual application. Add the `tests` folder inside of this repository to your projects ROOT directory.

```bash
  python manage.py test tests
```

- `.` means a test passed
- `E` means an unhandled error populated on a test
- `F` means a test completely failed to run

## Considerations

Consider utilizing django shortcuts for querying the database and automatically returning a 404 response if the query returns None.

## Tasks

- Update app urls.py files with url patterns and paths
- Create APIViews for GET requests that will Respond with the correct serialized data
- Ensure url paths contain the proper url pattern, Class Based View (as_view()), and name
