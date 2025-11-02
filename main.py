import sqlite3
import pandas as pd

def q1():
    return """
    SELECT *
    FROM City
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
    con = sqlite3.connect(r"World.db3")

    for i in range(1, 25):
        func_name = f"q{i}"
        if func_name in globals():

            quer = globals()[func_name]()


            print("=" * 45)
            print(f"Question: {i}")
            print("The query:\n", quer)

            # Execute query and get DataFrame
            df = pd.read_sql_query(quer, con)

            total_rows = df.shape[0]
            # Print total number of rows
            print("\nNum of rows:", total_rows)


            print("\nThe results:")


            if total_rows <= 10:
                # If the table is small, just print it all
                display_df = df
            else:
                # Combine first 5 and last 5 rows with a separator row
                first5 = df.head(5)
                last5 = df.tail(5)

                display_df = pd.concat([first5, last5], ignore_index=True)

            print(display_df)


    con.close()



if __name__ == "__main__":
    main()
