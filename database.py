import sqlite3
conn = sqlite3.connect("database.db")
c = conn.cursor()

# Created the table for user
c.execute("""
	CREATE TABLE IF NOT EXISTS User(
	id Integer PRIMARY KEY AUTOINCREMENT,
	username Text UNIQUE NOT NULL ,
	created_at Text NOT NULL)
""")
	
#  Created the table for task
c.execute("""
	CREATE TABLE IF NOT EXISTS Tasks(
	id Integer PRIMARY KEY AUTOINCREMENT,
	user_id Integer NOT NULL,
	title Text NOT NULL,
	status Text DEFAULT 'pending',
	priority Text DEFAULT 'low',
	due_date Text NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users (id))
""")

conn.commit()
conn.close()