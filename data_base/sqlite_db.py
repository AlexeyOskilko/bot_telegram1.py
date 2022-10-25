from create_bot import bot
import os
import psycopg2

DATABASE_URL = 'postgres://pkfpxpakcwftld:23961115710b9bce1a0d4b5ec226af0ada68d4c1978bb845f09c13e26cfb0c23@ec2-54-76-43-89.eu-west-1.compute.amazonaws.com:5432/dau58lkna6sjag'#postgres://pkfpxpakcwftld:23961115710b9bce1a0d4b5ec226af0ada68d4c1978bb845f09c13e26cfb0c23@ec2-54-76-43-89.eu-west-1.compute.amazonaws.com:5432/dau58lkna6sjag'

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()


# if base:
#     print('Data base connected OK!')
#     base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT,name TEXT PRIMARY KEY, description TEXT, price TEXT)')
#     base.commit()

# async def sql_add_command(state):
#     async with state.proxy()as data:
#         cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?)', tuple(data.values()))
#         base.commit()
#
async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menupizza').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

async def sql_read2():

async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))

