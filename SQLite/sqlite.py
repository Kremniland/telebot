import sqlite3 as sq


async def db_start():
    '''подключение к базе данных, создание таблицы если ее не существует'''
    global db, cur

    db = sq.connect('new.db')
    cur = db.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS profile(user_id TEXT PRIMARY KEY, photo, age, name, description)")

    db.commit()

async def create_profile(user_id):
    '''если профиль с юзер_ид не создан то создание профиля с пустыми полями кроме юзер_ид'''
    user = cur.execute("SELECT 1 FROM  profile WHERE user_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO profile VALUES(?, ? ,?, ?, ?)", (user_id, '', '', '', ''))
        db.commit()

async def edit_profile(state, user_id):
    '''заполнение ранее созданного профиля'''
    async with state.proxy() as data:
        cur.execute("UPDATE profile SET photo = '{}', age = '{}',  name = '{}', description = '{}' WHERE user_id == '{}'".format(
            data['photo'], data['age'], data['name'], data['description'], user_id
        ))
        db.commit()



