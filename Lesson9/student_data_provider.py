from sqlalchemy import create_engine
from sqlalchemy import text


class StudentDataProvider:
    def __init__(self, connection_string):
        self.__createConnection(connection_string)

    def __createConnection(self, connection_string):
        self.__db = create_engine(connection_string)
        self.__conn = self.__db.connect()

    def get_students(self):
        query = text("select * from student")
        return self.__conn.execute(query).fetchall()

    def get_student(self, user_id):
        query = text("select * from student where user_id = :user_id")
        return self.__conn.execute(query, {"user_id": user_id}).fetchone()

    def create_student(self, student):
        query = text("""INSERT INTO public.student (
                        user_id, level, education_form, subject_id) 
                        VALUES (:user_id, :level,
                        :education_form, :subject_id)""")
        self.__conn.execute(query, student)

    def update_student(self, student):
        query = text("""UPDATE public.student
                        SET user_id=:user_id, level=:level, 
                        education_form=:education_form, 
                        subject_id=:subject_id 
                        WHERE user_id=3000""")
        self.__conn.execute(query, student)

    def delete_student(self, user_id):
        self.__conn.execute(text("""DELETE FROM public.student
                                 WHERE user_id=3000"""), {"user_id": user_id})
