from pyhive import hive


conn = hive.Connection(host='10.0.4.10', port=10500, username='bigdata', database='bigdata_test')
cursor = conn.cursor()
#sql1 = "insert into test1 select 'lishuo1', str_to_map('event_id:play,post_id:123123')"
sql1 = "insert into test1 select 'lishuo1', map('event_id', 'play','post_id', '123')"
cursor.execute(sql1)
