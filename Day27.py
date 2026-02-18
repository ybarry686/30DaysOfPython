"""
Python with MongoDB:
    MongoDB: A NoSQL Database
        - Stores data in a JSON like document, making it very flexible and scalable
Python with SQLite:
    - After importing sqlite module you need to establish a database connection
"""

"""
Database Class:
    - Initialize/Setup: Ensure all required tables and indexes exist 
    - CREATE, READ, UPDATE, DELETE: Basic CRUD
    - Search/Filter: A way to find specific records by ID or Unique Title
        - Search using Unique Name'name TEXT Unique'
    - Count: Way to see how many records are in a table without loading all the data into memory
        - SELECT Count (*) FROM table_name
    - Exists Check: A boolean check to see if a specific entry is already there
        - check using Unique Name
        - Useful for validation before inserting/updating
        - Would basically be a helper function that will be reused/called in multple of functions
    - Bulk Insert: A method for adding a large list of items at once (using executemany)
        - Significantly faster that calling a single insert function 100 times.
        - Most likely will have the data in a datastructure

"""
import sqlite3 # import module

class MovieDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        self.setup_tables()
    
    def setup_tables(self):
        query = """
                    CREATE TABLE IF NOT EXISTS movies(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT UNIQUE,
                        director TEXT,
                        release_year INTEGER,
                        movie_rating REAL
                    )
                    """
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor() 
                
                cur.execute(query)
        except sqlite3.Error as e:
            print(f"Error Setting Up Table: {e}")
            return False
    
    def clear_database(self):
        try:
            with sqlite3.connect(self.db_path)  as con:
                cur = con.cursor()
                
                # Clear all rows in the database
                cur.execute("DELETE FROM movies")
                
                # Optional: Resets the ID counter back to 0
                cur.execute("DELETE FROM sqlite_sequence WHERE name=='movies'")
            return True
        
        except sqlite3.Error as e:
            print(f"Error Clearing All Rows: {e}")
            return False

    def add_one(self, movie_name, director, release_year, movie_rating):
        query = """
                INSERT OR IGNORE INTO movies(
                    name, 
                    director, 
                    release_year, 
                    movie_rating) 
                VALUES (?, ?, ?, ?)
                """
        data = (movie_name, director, release_year, movie_rating) # Stores variables into tuple
        
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                cur.execute(query, data)

                # Checks if a row was actually inserted
                if cur.rowcount > 0:
                    return True
                else:
                    return False # Means the movie already existed
        
        except sqlite3.Error as e:
            print(f"Error Inserting Row: {e}")
            return False

    def add_many(self, movie_names):
        if not movie_names:
            print(f"Function requires a list input!")
            return False
        
        query = """
                INSERT OR IGNORE INTO movies(
                    name,
                    director,
                    release_year,
                    movie_rating) 
                VALUES (?, ?, ?, ?) 
                """
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                
                # Take this SQL template (query) and run it for every value in list (movie_names) 
                cur.executemany(query, movie_names)

                print(f"Insertion was successful! Rows Affected: {cur.rowcount}")
                return True
        except sqlite3.Error as e:
            print(f"Error trying to insert multiple items: {e}")
            return False
    
    def update_rating(self, movie_name, new_rating):
        query = "UPDATE movies SET movie_rating = ? WHERE name = ?"
        data = (new_rating, movie_name)

        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                cur.execute(query, data)
                
                if cur.rowcount > 0:
                    return True
                else:
                    print(f"This movie ({movie_name}) isnt in the database")
                    return False
        
        except sqlite3.Error as e:
            print(f"Error Updating Row: {e}")
            return False

    def get_all(self):
        query = "SELECT * FROM movies"
        
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                cur.execute(query)

                rows = cur.fetchall() #returns a list of all rows
                return rows # return a list of tuples
        
        except sqlite3.Error as e:
            print(f"Error Fetching Fata: {e}")
            return []
        
    def find_by_title(self, movie_name):
        query = "SELECT * FROM movies WHERE name = ?"
        data = (movie_name,)

        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                cur.execute(query, data)
                res = cur.fetchone()
                
                if res is None:
                    print(f"{movie_name} was not found in the database")
                    return res
                
                return res
        
        except sqlite3.Error as e:
            print(f"Error Finding Movie: {e}")
            return None
        
    def check_exists(self, movie_name):
        query = "SELECT 1 FROM movies WHERE name = ? LIMIT 1"
        data = (movie_name,) 
        
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                cur.execute(query, data)
                res = cur.fetchone()
                
                if res is None:
                    return False
                
                return True
        
        except sqlite3.Error as e:
            print(f"Error Finding Movie: {e}")
            return None
     
    def get_count(self):
        query = "SELECT Count (*) FROM movies"
        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                cur.execute(query)

                res = cur.fetchone()
            return res
        
        except sqlite3.Error as e:
            print(f"Error Finding Database Count: {e}")
            return None
        
    def delete_record(self, movie_name):
        if self.check_exists(movie_name) == False:
            print("Movie is not in database")
            return False
        
        select_query = "SELECT * FROM movies WHERE name = ?"
        delete_query = "DELETE FROM movies WHERE name = ?"
        data = (movie_name,)

        try:
            with sqlite3.connect(self.db_path) as con:
                cur = con.cursor()
                
                cur.execute(select_query, data)
                record_to_delete = cur.fetchone()

                cur.execute(delete_query, data)

                print(f"The record we have deleted is: {record_to_delete}")
                return True
        except sqlite3.Error as e:
            print(f"Error deleting record: {e}")
            return False

db = MovieDatabase('movie.db')

db.add_one("Interstellar", "Christopher Nolan", 2014, 9.5)
db.add_one("Aftersun", "Bob Dylan", 2018, 8.0)
db.add_one("Inception", "Christopher Nolan", 2011, 9.6)
db.add_one("Tangled", "Amy Cheer", 2016, 10)
db.add_one("Get Out", "Dan Jones", 2020, 8.9)
print(db.get_all())

print('-----------------------------')

db.update_rating("Interstellar", 9.6)
db.update_rating("Aftersun", 8.7)
db.update_rating("Inception", 9.2)
db.update_rating("Doo Doo", 7.5)
print(db.get_all())

print('-----------------------------')

print(db.find_by_title("Interstellar"))
print(db.find_by_title("Get Out"))
print(db.find_by_title("Tangled"))
print(db.find_by_title("Angle"))


print('-----------------------------')

print(db.get_count())

print('-----------------------------')

print(db.check_exists("Interstellar"))
print(db.check_exists("Get Out"))
print(db.check_exists("Tangled"))
print(db.check_exists("Angle"))

print('-----------------------------')

db.delete_record("Interstellar")
db.delete_record("Get Out")
print(db.get_all())

print('-----------------------------')
movie_data = [
    ("Inception", "Christopher Nolan", 2010, 8.8),
    ("The Godfather", "Francis Ford Coppola", 1972, 9.2),
    ("Pulp Fiction", "Quentin Tarantino", 1994, 8.9),
    ("Spirited Away", "Hayao Miyazaki", 2001, 8.6),
    ("Parasite", "Bong Joon-ho", 2019, 8.5),
    ("The Dark Knight", "Christopher Nolan", 2008, 9.0),
    ("The Matrix", "Lana Wachowski", 1999, 8.7),
    ("Schindler's List", "Steven Spielberg", 1993, 9.0),
    ("Seven Samurai", "Akira Kurosawa", 1954, 8.6),
    ("Goodfellas", "Martin Scorsese", 1990, 8.7)
]
db.add_many(movie_data)
print(db.get_all())

"""
Changes for Future Reference:
    - The Singleton Connection Pattern
        - Instead of opening an closing a a connection inside each function (expensive)
          you should insteas open the connection once in __init__ and close it when the object is 
          destroyed.
        - Or use a Context Manager
    - Decoupling Logic from Display
        - A database class should never print()
        - Should only return data or raise an Exception
    - Standard Formatting
        - Use Docstrings to explain each function
        - Do type hinting with function signatures
            - Ex: def add_one(self, name: str, rating: float) -> bool:
    - Always Use Row Factory
        - Instead of having to remember which SQL column is named what you can just
          type the database name and the column name regardless of where it is to retrieve data
            - Without Row Factory Ex: print(f"Director: {res[2]}") --> must remember that its on column 2
            - With Row Factory Ex: print(f"Director: {res['Director]}") 
"""