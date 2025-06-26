import psycopg
import psycopg_pool
from pydantic import BaseModel

class DbEndpoint(BaseModel):
    """ データベース接続情報 """
    dbname: str
    user: str
    password: str
    host: str
    port: int = 5432

    def getEndpointString(self) -> str:
        return f"dbname={self.dbname} user={self.user} password={self.password} host={self.host} port={self.port}"

# シンプルな接続例
def connect_db(config: DbEndpoint):
    # データベース接続情報を文字列に変換
    with psycopg.connect(conninfo=config.getEndpointString()) as conn:
        # カーソルを作成
        with conn.cursor() as cur:
            # セレクトクエリを実行
            cur.execute("SELECT * FROM sample_table;")
            for record in cur:
                print(record)
            conn.commit()

# コネクションプールを使用した例
# https://www.psycopg.org/psycopg3/docs/advanced/pool.html
# https://www.psycopg.org/psycopg3/docs/api/pool.html#psycopg_pool.ConnectionPool
def connect_db_pool(config: DbEndpoint):
    # データベース接続情報を文字列に変換
    with psycopg_pool.ConnectionPool(conninfo=config.getEndpointString(), min_size=1, max_size=3) as pool:
        # pool.wait()
        with pool.getconn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM sample_table;")
                for record in cur:
                    print(record)

# 非同期コネクションプールを使用した例
# https://www.psycopg.org/psycopg3/docs/advanced/pool.html#psycopg_pool.AsyncConnectionPool
async def connect_db_async_pool(config: DbEndpoint):
    # データベース接続情報を文字列に変換
    async with psycopg_pool.AsyncConnectionPool(conninfo=config.getEndpointString(), min_size=1, max_size=3) as pool:
        async with pool.connection() as conn:
            async with conn.cursor() as cur:
                await cur.execute("SELECT * FROM sample_table;")
                async for record in cur:
                    print(record)