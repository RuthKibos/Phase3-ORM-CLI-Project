from models.__init__ import CURSOR, CONN

class Course:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, name, department, credits, id=None):
        self.id = id
        self.name = name
        self.department = department
        self.credits = credits

    def __repr__(self):
        return f"<Course {self.id}: {self.name}, {self.department}, {self.credits}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, department):
        if isinstance(department, str) and len(department):
            self._department = department
        else:
            raise ValueError("Department must be a non-empty string")

    @property
    def credits(self):
        return self._credits

    @credits.setter
    def credits(self, credits):
        if isinstance(credits, int) and credits > 0:
            self._credits = credits
        else:
            raise ValueError("Credits must be a positive integer")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Course instances """
        sql = """
            CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            credits INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Course instances """
        sql = """
            DROP TABLE IF EXISTS courses;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, department, and credits values of the current Course object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key """
        sql = """
            INSERT INTO courses (name, department, credits)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.department, self.credits))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Course instance."""
        sql = """
            UPDATE courses
            SET name = ?, department = ?, credits = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.department, self.credits, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Course instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM courses
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, department, credits):
        """ Initialize a new Course instance and save the object to the database """
        course = cls(name, department, credits)
        course.save()
        return course

    @classmethod
    def instance_from_db(cls, row):
        """Return a Course object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        course = cls.all.get(row[0])
        if course:
            # ensure attributes match row values in case local instance was modified
            course.name = row[1]
            course.department = row[2]
            course.credits = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            course = cls(row[1], row[2], row[3])
            course.id = row[0]
            cls.all[course.id] = course
        return course

    @classmethod
    def get_all(cls):
        """Return a list containing one Course object per table row"""
        sql = """
            SELECT *
            FROM courses
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Course object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM courses
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Course object corresponding to the first table row matching the specified name"""
        sql = """
            SELECT *
            FROM courses
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def students(self):
        """Return list of students associated with the current course"""
        from models.student import Student
        sql = """
            SELECT students.* FROM students
            JOIN enrollments ON students.id = enrollments.student_id
            WHERE enrollments.course_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Student.instance_from_db(row) for row in rows]