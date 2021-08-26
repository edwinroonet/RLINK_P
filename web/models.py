from django.db import models
from django.db import connections

# Create your models here.

class Sg_user(models.Model):
    u_no = models.AutoField(10, primary_key=True)
    u_name = models.CharField(max_length=50, null=True)
    u_email = models.CharField(max_length=100, null=True)
    u_id = models.CharField(max_length=100, null=True)
    u_passwd = models.CharField(max_length=255, null=True)
    u_tel = models.CharField(max_length=50, null=True)
    u_addr1 = models.CharField(max_length=255, null=True)
    u_addr2 = models.CharField(max_length=255, null=True)
    u_addr3 = models.CharField(max_length=255, null=True)
    u_agree = models.IntegerField(null=True)
    u_auth = models.CharField(max_length=100, null=True)
    u_kind = models.CharField(max_length=20, null=True)
    u_type = models.CharField(max_length=10, null=True)
    u_manager = models.CharField(max_length=20, null=True)
    u_access = models.IntegerField(null=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=1)
    is_authenticated = models.BooleanField(default=1)
    chatid = models.IntegerField(null=True)

    class Meta:
        db_table = 'sg_user'


def listfetchall(cursor):
    return cursor.fetchall()

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dbexecute(sql):
    try:
        print("dbexecute start")
        c = connections['default'].cursor()
        c.execute(sql, [])
        rst = listfetchall(c)
        print(rst)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()


def dbexecuteQuery(sql, param):
    try:
        c = connections['default'].cursor()
        c.execute(sql, param)
        print(sql)
        print(param)
        rst = dictfetchall(c)
        print(rst)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()


def boardListAdmin(cat):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.br_title, a.br_regdate, b.u_name, c.ct_name  '
        sql = sql + 'FROM rlink.sg_board a, '
        sql = sql + '     rlink.sg_user b, '
        sql = sql + '     rlink.sg_category c '
        sql = sql + 'WHERE a.ct_no = %s '
        sql = sql + 'AND a.u_no = b.u_no '
        sql = sql + 'AND a.ct_no = c.ct_no '
        sql = sql + 'ORDER BY a.br_no DESC '

        param.append(cat)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

