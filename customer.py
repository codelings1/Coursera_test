import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1", port = 3306)
cursor = conn.cursor()

query = "SHOW DATABASES";
cursor.execute(query);

results = cursor.fetchall();

print results
