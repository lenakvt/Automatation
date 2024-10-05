from student_data_provider import StudentDataProvider

connection_string = "postgresql://postgres:LFLM2024@localhost:5432/postgres"
student_db = StudentDataProvider(connection_string)


def test_create_student():
    start_length = len(student_db.get_students())
    student = {
        "user_id": 3000,
        "level": 'Beginner',
        "education_form": 'personal',
        "subject_id": 1
    }
    student_db.create_student(student)
    end_length = len(student_db.get_students())

    assert end_length - start_length == 1

    student_db.delete_student(3000)


def test_update_student():
    student = {
        "user_id": 3000,
        "level": 'Beginner',
        "education_form": 'personal',
        "subject_id": 1
    }

    student_db.create_student(student)
    assert student_db.get_student(3000).level == 'Beginner'

    student['level'] = 'Upper-Intermediate'
    student_db.update_student(student)
    assert student_db.get_student(3000).level == 'Upper-Intermediate'

    student_db.delete_student(3000)


def test_delete_student():
    start_length = len(student_db.get_students())

    student = {
        "user_id": 3000,
        "level": 'Beginner',
        "education_form": 'personal',
        "subject_id": 1
    }

    student_db.create_student(student)
    student_db.delete_student(3000)

    end_length = len(student_db.get_students())

    assert end_length - start_length == 0
