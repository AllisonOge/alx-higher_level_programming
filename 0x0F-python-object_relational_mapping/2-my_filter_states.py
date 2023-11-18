#!/usr/bin/python3
"""
module for filtering database query using MySQLdb
"""
import sys
import MySQLdb


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    st_name = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=user, passwd=passwd,
                           db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * from states WHERE name=%s
                   ORDER BY id ASC""", (st_name,))
    query_row = cur.fetchone()
    print(query_row)

    cur.close()
    conn.close()
