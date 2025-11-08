#Eliyahu Aviya 208586339
#Esther Benzaquen 207956673

import sqlite3
import pandas as pd

def q1():
    return """
    SELECT *
    FROM City
    """
def q2():
    return """
    SELECT *
    FROM Country
    """
def q3():
    return """
    SELECT *
    FROM Country
    WHERE Continent IN ('Asia')
    """
def q4():
    return """
    SELECT *
    FROM Country
    WHERE Continent NOT IN ('Asia')
    """
def q5():
    return """
    SELECT *
    FROM Country
    WHERE Continent NOT IN ('Asia', 'Europe');
    """
def q6():
    return """
    SELECT *
    FROM City
    WHERE Name LIKE 'H%'
    """
def q7():
    return """
    SELECT *
    FROM Country
    WHERE Name NOT LIKE '%e%'
    """
def q8():
    return """
    SELECT *
    FROM City
    WHERE CountryCode NOT IN ('GBR');
    """
def q9():
    return """
    SELECT *
    FROM City
    WHERE CountryCode IN ('LBR', 'DOM', 'TKL');
    """
def q10():
    return """
    SELECT *
    FROM Country
    WHERE IndepYear IN (1970, 1981, 1991);
    """
def q11():
    return """
    SELECT *
    FROM Country
    WHERE IndepYear = 1980 AND  IndepYear = 1991;
    """
def q12():
    return """
    SELECT *
    FROM Country
    WHERE IndepYear BETWEEN 1980 AND 1991
    """
def q13():
    return """
    SELECT *
    FROM Country
    WHERE Continent IN('North America') AND  IndepYear > 1902;
    """
def q14():
    return """
    SELECT *
    FROM Country
    WHERE Continent IN('North America') OR  IndepYear > 1901;
    """
def q15():
    return """
    SELECT *
    FROM City
    WHERE Population > 4000000;
    """
def q16():
    return """
    SELECT *
    FROM City
    WHERE Population > 3000000 AND CountryCode IN('CHN') ;
    """
def q17():
    return """
    SELECT *
    FROM City
    WHERE Population BETWEEN 220000 AND 270000;
    """
def q18():
    return """
    SELECT *
    FROM Country
    ORDER BY GNP DESC
    LIMIT 11;
    """
def q19():
    return """
    SELECT *
    FROM Country
    ORDER BY GNP DESC
    LIMIT 11,8;
    """
def q20():
    return """
    SELECT *
    FROM Country
    ORDER BY GNP ASC
    LIMIT 10;
    """
def q21():
    return """
    SELECT DISTINCT *
    FROM CountryLanguage
    ORDER BY Language ASC;
    """
def q22():
    return """
    SELECT *
    FROM Country
    ORDER BY IndepYear ASC, Name DESC;
    """
def q23():
    return """
    SELECT *
    FROM Country
    ORDER BY LifeExpectancy DESC;
    """
def q24():
    return """
    SELECT 
        Name AS 'Country Name',
        CONCAT(Continent, ' (', Region, ')') AS 'Continent and Region'
    FROM Country
    ORDER BY Name ASC;
    """


def main():
    con = sqlite3.connect(r"World.db3")
    output_file = "query_results.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("Eliyahu Aviya 208586339\nEsther Benzaquen 207956673 \n")

        for i in range(1, 25):
            func_name = f"q{i}"
            if func_name in globals():
                query = globals()[func_name]()

                print("=" * 45)
                print(f"Question: {i}")
                print("The query:\n", query)

                f.write("=" * 45 + "\n")
                f.write(f"Question: {i}\n")
                f.write("The query:\n" + query + "\n")

                df = pd.read_sql_query(query, con)
                total_rows = df.shape[0]

                print("\nNum of rows:", total_rows)
                f.write(f"\nNum of rows: {total_rows}\n")

                print("\nThe results:")
                f.write("\nThe results:\n")

                if total_rows <= 10:
                    display_df = df
                else:
                    first5 = df.head(5)
                    last5 = df.tail(5)
                    display_df = pd.concat([first5, last5], ignore_index=True)

                print(display_df)
                f.write(display_df.to_string(index=False))
                f.write("\n\n")

    con.close()


if __name__ == "__main__":
    main()
