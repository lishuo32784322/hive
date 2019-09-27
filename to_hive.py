from pyhive import hive


conn = hive.Connection(host='10.0.4.10', port=10500, username='bigdata', database='bigdata_test')
cursor = conn.cursor()
#sql = "insert into table test_log partition (dt='20190810') values('百搭','and','1.2.1','应用宝','110','1555582998','192.168.1.1','53-100','63-200','153572667726118901','4ad1ba7b-2c08-395c-ada5-5bda10d30565','897DFD91756D3E953DF550442AF1EBC4','3D390C73-6959-410C-9FB1-099F1FF26260','5.1.1','HUAWEIGRA-CL10','HUAWEI','HUAWEI','1920x1080','1','中国联通', '1555582998000','event_id': 'view'+'\t'+'source': '1'+'\t'+'post_id': '134098527256287657'+'\t'+'mtype': '1'+'\t'+'impressionId': 'f1aa6227a3630b7c08169f8a3a8fc75b'+'\t'+'flag': 'user_cf,lda'+'\t'+'start_time': '1565239413000'+'\t'+'end_time': '1565239453000')"

#sql = "insert into table test1(value, event) values('lishuo','a:1')"
sql = "insert into bigdata_test.test_log partition(dt='2019-08-13') select '百搭','and','1.2.1','应用宝','110','1555582998','192.168.1.1','53-100','63-200','153572667726118901','4ad1ba7b-2c08-395c-ada5-5bda10d30565','897DFD91756D3E953DF550442AF1EBC4','3D390C73-6959-410C-9FB1-099F1FF26260','5.1.1','HUAWEIGRA-CL10','HUAWEI','HUAWEI','1920x1080','1','中国联通', '1555582998000',map('event_id', 'play','post_id', '123')"
cursor.execute(sql)
