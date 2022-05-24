from pyrogram import Client

API_KEY = int(input("10263857: "))
API_HASH = input("fb26b012190c60f071297370b55e48df: ")
with Client(':memory:', api_id=API_KEY, api_hash=API_HASH) as app:
    print(app.export_session_string())
