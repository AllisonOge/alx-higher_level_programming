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
    try:
        conn = MySQLdb.connect(host="localhost", port=3306,
                               user=user, passwd=passwd,
                               db=db_name, charset="utf8")
        cur = conn.cursor()
        cur.execute("""SELECT cities.name FROM cities
                    JOIN states ON cities.state_id = states.id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC""", (st_name, ))
        query_rows = cur.fetchall()
        print(", ".join([query[0] for query in query_rows]))
        cur.close()
        conn.close()
    except MySQLdb.Error:
        pass
