# lib/models/student.py
from models.__init__ import CURSOR, CONN

class Student:

   
    all = {}
    
    def __init__(self, name, age, email, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        
    def __repr__(self):
        return f"<Student {self.id}: {self.name}, {self.age}, {self.email}>"

#name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
   # age property
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            raise ValueError("Age must be an integer")
            
    #email property
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and "@" in email:
            self._email = email
        else:
            raise ValueError("Email must be written Correctly") 
           
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            email TEXT )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS students;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO students (name, age, email)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.age, self.email))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, age, email):
        student = cls(name, age, email)
        student.save()
        return student

    def update(self):
        sql = """
            UPDATE students
            SET name = ?, age = ?, email = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age, self.email, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM students
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        student = cls.all.get(row[0])
        if student:
            student.name = row[1]
            student.age = row[2]
            student.email = row[3]
        else:
            student = cls(row[1], row[2], row[3])
            student.id = row[0]
            cls.all[student.id] = student
        return student

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM students
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM students
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    #Return student object corresponding to first table row matching specified name
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM students
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_email(cls, email):
        sql = """
            SELECT *
            FROM students
            WHERE email = ?
        """
        row = CURSOR.execute(sql, (email,)).fetchone()
        return cls.instance_from_db(row) if row else None





    
    
