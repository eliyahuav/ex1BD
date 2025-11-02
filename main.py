import sqlite3
import pandas as pd

def q1():
    return """
    SELECT *
    FROM (
        SELECT *
        FROM City
        ORDER BY id ASC
        LIMIT 5
    )
    UNION ALL
    SELECT *
    FROM (
        SELECT *
        FROM City
        ORDER BY id DESC
        LIMIT 5
    )
    ORDER BY id ASC;
    """



# def q2():
#     return """
#     SELECT *
#     FROM Country
#     """
#
# def q3():
#     return """
#     SELECT *
#     FROM Country
#     """
#
# def q4():
#     return """
#     SELECT *
#     FROM Country
#     """
#
# def q5():
#     return """
#     SELECT *
#     FROM Country
#     """
#
# def q6():
#     return """
#     SELECT *
#     FROM Country
#     """

def main():
    con = sqlite3.connect(r"C:\Users\1\Documents\שנה ד\big data\tar1\World.db3")

    for i in range(1, 25):
        func_name = f"q{i}"
        if func_name in globals():
            quer = globals()[func_name]()
            print("="*45 + "\n" + "Question: " + str(i) + "\n" + "The query:" + "\n" + quer)
            df = pd.read_sql_query(quer, con)
            print(df.head(10))

    con.close()



if __name__ == "__main__":
    main()
