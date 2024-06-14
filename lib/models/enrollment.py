from models.__init__ import CURSOR, CONN

class Enrollment:

# Dictionary of objects saved to the database.
    all={}

    def __init__(self, student_id, course_id, id=None):
        self.id = id
        self.student_id = student_id
        self.course_id = course_id

    def __repr__(self):
        return f"<Enrollment {self.id}: Student ID {self.student_id}, Course ID {self.course_id}>"
    
    #student id property
    @property
    def student_id(self):
        return self._student_id
    
    def student_id(self, student_id):
        if isinstance(student_id, int):
            self._student_id = student_id
        else:
            raise ValueError("student_id must be an interger")
    
    #course_id property   
    @property
    def course_id(self):
        return self._course_id
    
    def course_id(self, course_id):
        if isinstance(course_id, int):
            self._course_id = course_id
        else:
            raise ValueError("course_id must be an interger")

    # Create the enrollments table if it doesn't already exist    
    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS enrollments (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
        DROP TABLE IF EXISTS enrollments;
    """
        CURSOR.execute(sql)
        CONN.commit()
    
    # Insert a new row into the enrollments table with the current object's data
    def save(self):
        sql = """
        INSERT INTO enrollments (student_id, course_id)
        VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.student_id, self.course_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

   # Delete the row that matches the current enrollment object from the enrollments table
    def delete(self):
        sql = """
    DELETE FROM enrollments
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    # Initialize a new enrollment object and save it to the database
    @classmethod
    def create(cls, student_id, course_id):
        enrollment = cls(student_id, course_id)
        enrollment.save()
        return enrollment
    
    def update(self):
        sql = """
            UPDATE enrollments
            SET student_id = ?, course_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.student_id, self.course_id))
        CONN.commit()

    # Create an enrollment object from a database row
    @classmethod
    # Check the dictionary for  existing instance using the row's primary key
    def instance_from_db(cls, row):
        enrollment = cls.all.get(row[0])
        if enrollment:
    # ensure attributes match row values
            enrollment.student_id = row[1]
            enrollment.course_id = row[2]
        else:
    # not in dictionary, create new instance and add to dictionary
            enrollment = cls(row[1], row[2])
            enrollment.id = row[0]
            cls.all[enrollment.id] = enrollment
        return enrollment
    
    # Return a list of all Enrollment objects in the enrollments table
    @classmethod
    def get_all(cls):
        sql = """
        SELECT * FROM enrollments
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
     # Return the Enrollment object with the specified id, if it exists
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM enrollments
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    # Return a list of Enrollment objects for the specified student_id
    @classmethod
    def find_by_student_id(cls, student_id):
        sql = """
            SELECT *
            FROM enrollments
            WHERE student_id = ?
        """
        rows = CURSOR.execute(sql, (student_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    # Return a list of Enrollment objects for the specified course_id
    @classmethod
    def find_by_course_id(cls, course_id):
        sql = """
            SELECT *
            FROM enrollments
            WHERE course_id = ?
        """
        rows = CURSOR.execute(sql, (course_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]








