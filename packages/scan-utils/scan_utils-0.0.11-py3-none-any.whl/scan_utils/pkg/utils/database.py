import pymysql
import psycopg2


class MysqlDB:
    def __init__(self, db_info):
        self.db_info = db_info
        self.conn = self.connect()

    def connect(self):
        conn = pymysql.connect(host=self.db_info["host"],
                               port=int(self.db_info["port"]),
                               user=self.db_info["user"],
                               password=self.db_info["passwd"],
                               database=self.db_info["db_name"],
                               charset="utf8"
                               )
        return conn

    def exec_sql(self, sql, fetch="Many", num=0):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        if fetch == "Many":
            return cursor.fetchall()
        elif fetch == "One":
            return cursor.fetchone()
        else:
            return cursor.fetchmany(num)


class PostgreDB:
    def __init__(self, db_info):
        self.db_info = db_info
        self.conn = self.connect()

    def connect(self):
        conn = psycopg2.connect(
            database=self.db_info["db_name"],
            user=self.db_info["db_user"],
            password=self.db_info["passwd"],
            host=self.db_info["host"],
            port=self.db_info["port"],
        )
        return conn

    def exec_sql(self, sql, fetch="Many", num=0):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        if fetch == "Many":
            return cursor.fetchall()
        elif fetch == "One":
            return cursor.fetchone()
        else:
            return cursor.fetchmany(num)

    def get_meta_info(self):
        result = {
            "dbs": []
        }

        for i in self.exec_sql("SELECT datname FROM pg_database;"):
            result["dbs"].append(i[0])

        result["dbs"] = sorted(result["dbs"])
        return result
