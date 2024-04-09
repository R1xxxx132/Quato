import aiosqlite
import disnake

class ModerationDataBase:
    
    def __init__(self):
        self.name = "./src/databases/moderation.db"

    async def create_table(self):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = '''CREATE TABLE IF NOT EXISTS users (
                server_id INTEGER,
                user_id INTEGER,
                warns INTEGER
            )'''
            await cursor.execute(query)
            await db.commit()

    async def get_user(self, user: disnake.User):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'SELECT * FROM users WHERE server_id = ? AND user_id = ?'
            await cursor.execute(query, (user.guild.id, user.id))
            return await cursor.fetchone()

    async def add_user(self, user: disnake.User):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'INSERT INTO users (server_id, user_id, warns) VALUES (?, ?, ?)'
            await cursor.execute(query, (user.guild.id, user.id, 0))
            await db.commit()
    
    async def remove_user(self, user: disnake.User):
        async with aiosqlite.connect(self.name) as db:
            cursor = await db.cursor()
            query = 'DELETE FROM users WHERE server_id = ? AND user_id = ?'
            await cursor.execute(query, (user.guild.id, user.id))
            await db.commit()