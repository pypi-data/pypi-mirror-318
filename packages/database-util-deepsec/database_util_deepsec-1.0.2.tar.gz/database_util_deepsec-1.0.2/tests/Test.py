from src.database_util import MysqlUtil

config = {
    'user': 'root',
    'password': 'reiking123',
    'host': '8.140.58.220',
    'port': '3306'
}

mysql_connector = MysqlUtil(config)

mysql_connector.close()
