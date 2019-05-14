import pymysql
import base64

db = pymysql.connect(host='vijay-app-db.ckv6z1bs6r16.us-east-2.rds.amazonaws.com',  # your host
                     user='root',  # username
                     passwd='12345678',  # password
                     db='sampleDB')  # database name

def insertFoods(product_productId, review_userId, review_profileName, review_helpfulness, review_score, review_time, review_summary, review_text):
    print('insertFoods called')

    sql = """INSERT INTO foods (product_productId, review_userId, review_profileName, review_helpfulness, review_score, review_time, review_summary, review_text) VALUES ( "%s","%s","%s","%s","%s","%s","%s","%s" )""" % (
        product_productId, review_userId, review_profileName, review_helpfulness, review_score, review_time, review_summary, review_text)
    result = db_operation(sql)
    print(result)


def db_operation(sql):
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        return cursor.fetchall()
    except Exception as e:
        print(e)
        db.rollback()
