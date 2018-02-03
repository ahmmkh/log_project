import psycopg2
postfix = ["views", "views", "%"]
postfix_msg = ["the most popular three articles of all time",
               "the most popular article authors of all time",
               "On which days did more than 1%% of requests lead to errors"]
QUERY_1 = ("SELECT "
           "articles.title, "
           "COUNT(log.path) "
           "FROM "
           "log "
           "INNER JOIN articles ON CONCAT('/article/', articles.slug)"
           " = log.path "
           "GROUP BY "
           "articles.title "
           "ORDER BY "
           "COUNT(log.path) DESC "
           "LIMIT "
           "3")
QUERY_2 = ("SELECT "
           "authors.name, "
           "COUNT(log.path) "
           "FROM "
           "log "
           "INNER JOIN articles ON CONCAT('/article/', articles.slug)"
           " = log.path "
           "INNER JOIN authors ON articles.author = authors.id "
           "GROUP BY "
           "authors.name "
           "ORDER BY "
           "COUNT(log.path) DESC")
QUERY_3 = ("SELECT "
           "normal.day, "
           "ROUND(((err.errors + 0.0) / (normal.pass_code+0.0))*100 , 2) as"
           " perc "
           "FROM "
           "( "
           "SELECT "
           "DATE(time) as day, "
           "COUNT(DATE(time)) as errors "
           "FROM "
           "log "
           "WHERE "
           "status = '404 NOT FOUND' "
           "GROUP BY "
           "DATE(time) "
           "ORDER BY "
           "DATE(time) DESC "
           ") err "
           "INNER JOIN ( "
           "SELECT "
           "DATE(time) as day, "
           "COUNT(DATE(time)) as pass_code "
           "FROM "
           "log "
           "WHERE "
           "status = '200 OK' "
           "GROUP BY "
           " DATE(time) "
           "ORDER BY "
           "DATE(time) DESC "
           ") normal ON err.day = normal.day "
           "WHERE "
           "ROUND(((err.errors + 0.0) / (normal.pass_code+0.0))*100 , 2) > 1")


def connect():
    """ Connect To the database  """
    try:
        db = psycopg2.connect("dbname=news")
        cur = db.cursor()
        return db, cur
    except ValueError:
        print("there is an error while connecting")


def get_query(query):
    """ get the query data in array of tuples """
    db, cur = connect()
    cur.execute(query)
    data = cur.fetchall()
    return data


def print_data(data, pf, f):
    """print data got from queries"""
    f.write("--- "+postfix_msg[pf]+" ---\n\n")
    for record in data:
        f.write(str(record[0])+"____"+str(record[1])+" "+postfix[pf]+"\n")
    f.write("\n ------------------ \n\n")


if __name__ == '__main__':
    queries = [QUERY_1, QUERY_2, QUERY_3]
    with open("report.txt", "w+") as f:
        for i in xrange(len(queries)):
            print_data(get_query(queries[i]), i, f)
