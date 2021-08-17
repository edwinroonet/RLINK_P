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


class Sg_comp(models.Model):
    c_no = models.AutoField(10, primary_key=True)
    c_name = models.CharField(max_length=100, null=True)
    c_ceo = models.CharField(max_length=100, null=True)
    c_manager = models.CharField(max_length=100, null=True)
    c_tel = models.CharField(max_length=50, null=True)
    c_addr1 = models.CharField(max_length=255, null=True)
    c_addr2 = models.CharField(max_length=255, null=True)
    c_addr3 = models.CharField(max_length=255, null=True)
    c_service_addr = models.CharField(max_length=255, null=True)
    c_intro = models.CharField(max_length=255, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    u_no = models.IntegerField(null=True)

    class Meta:
        db_table = 'sg_comp'


class Sg_comp_img(models.Model):
    ci_no = models.AutoField(10, primary_key=True)
    c_no = models.IntegerField(null=True)
    img = models.CharField(max_length=255, null=True)
    img_1 = models.CharField(max_length=255, null=True)
    img_2 = models.CharField(max_length=255, null=True)
    img_3 = models.CharField(max_length=255, null=True)
    img_4 = models.CharField(max_length=255, null=True)
    img_5 = models.CharField(max_length=255, null=True)
    img_6 = models.CharField(max_length=255, null=True)
    img_7 = models.CharField(max_length=255, null=True)
    img_8 = models.CharField(max_length=255, null=True)
    img_9 = models.CharField(max_length=255, null=True)
    img_info = models.CharField(max_length=255, null=True)
    img1_info = models.CharField(max_length=255, null=True)
    img2_info = models.CharField(max_length=255, null=True)
    img3_info = models.CharField(max_length=255, null=True)
    img4_info = models.CharField(max_length=255, null=True)
    img5_info = models.CharField(max_length=255, null=True)
    img6_info = models.CharField(max_length=255, null=True)
    img7_info = models.CharField(max_length=255, null=True)
    img8_info = models.CharField(max_length=255, null=True)
    img9_info = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'sg_comp_img'

class Sg_estimate_from(models.Model):
    ef_no = models.AutoField(10, primary_key=True)
    ef_name = models.CharField(max_length=255, null=True)
    ef_tel = models.CharField(max_length=255, null=True)
    ef_addr1 = models.CharField(max_length=255, null=True)
    ef_addr2 = models.CharField(max_length=255, null=True)
    ef_addr3 = models.CharField(max_length=255, null=True)
    ef_kind = models.CharField(max_length=100, null=True)
    ef_req_list = models.CharField(max_length=255, null=True)
    ef_text = models.CharField(max_length=255, null=True)
    ef_etc = models.CharField(max_length=255, null=True)
    ef_complete = models.CharField(max_length=1, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    u_no = models.IntegerField(null=True)
    c_no = models.IntegerField(null=True)
    ef_img1 = models.CharField(max_length=255, null=True)
    ef_img2 = models.CharField(max_length=255, null=True)
    ef_img3 = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'sg_estimate_from'

class Sg_estimate_to(models.Model):
    et_no = models.AutoField(10, primary_key=True)
    c_no = models.IntegerField(null=True)
    ef_no = models.IntegerField(null=True)
    et_status = models.IntegerField(null=True)
    et_total_amt = models.IntegerField(null=True)
    et_text = models.CharField(max_length=255, null=True)
    et_obj_1 = models.CharField(max_length=255, null=True)
    et_obj_2 = models.CharField(max_length=255, null=True)
    et_obj_3 = models.CharField(max_length=255, null=True)
    et_obj_4 = models.CharField(max_length=255, null=True)
    et_obj_5 = models.CharField(max_length=255, null=True)
    et_file_1 = models.CharField(max_length=255, null=True)
    et_file_2 = models.CharField(max_length=255, null=True)
    et_file_3 = models.CharField(max_length=255, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sg_estimate_to'


class Sg_review(models.Model):
    rv_no = models.AutoField(10, primary_key=True)
    rv_reviewer = models.CharField(max_length=255, null=True)
    rv_score = models.FloatField(null=True)
    rv_text = models.CharField(max_length=255, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    et_no = models.IntegerField(null=True)
    c_no = models.IntegerField(null=True)
    ef_no = models.IntegerField(null=True)

    class Meta:
        db_table = 'sg_review'

class Sg_category(models.Model):
    ct_no = models.AutoField(10, primary_key=True)
    ct_name = models.CharField(max_length=255, null=True)
    ct_authority = models.IntegerField(null=True)

    class Meta:
        db_table = 'sg_category'

class Sg_section(models.Model):
    st_no = models.AutoField(10, primary_key=True)
    ct_no = models.IntegerField(null=True)
    st_name = models.CharField(max_length=255, null=True)
    st_view_yn = models.IntegerField(null=True)
    st_authority = models.IntegerField(null=True)
    st_regdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sg_section'

class Sg_board(models.Model):
    br_no = models.AutoField(10, primary_key=True)
    br_type = models.CharField(max_length=255, null=True)
    br_title = models.CharField(max_length=255, null=True)
    br_text = models.CharField(max_length=255, null=True)
    br_view = models.IntegerField(null=True)
    br_secret_yn = models.IntegerField(null=True)
    br_password = models.CharField(max_length=255, null=True)
    br_status = models.IntegerField(null=True)
    br_view_yn = models.IntegerField(null=True)
    br_authority = models.IntegerField(null=True)
    br_popup_yn = models.IntegerField(null=True)
    br_fromntc = models.DateTimeField()
    br_tontc = models.DateTimeField()
    br_regdate = models.DateTimeField(auto_now_add=True)
    u_no = models.IntegerField(null=True)
    st_no = models.IntegerField(null=True)
    ct_no = models.IntegerField(null=True)

    class Meta:
        db_table = 'sg_board'

class Sg_board_img(models.Model):
    bi_no = models.AutoField(10, primary_key=True)
    br_no = models.IntegerField(null=True)
    bi_image = models.CharField(max_length=255, null=True)
    bi_image_filename = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'sg_board_img'

class Sg_estimate_check(models.Model):
    efc_no = models.AutoField(10, primary_key=True)
    u_no = models.IntegerField(null=True)
    ef_no = models.IntegerField(null=True)
    efc_yn = models.IntegerField(null=True)

    class Meta:
        db_table = 'sg_estimate_check'

class Sg_chat_check(models.Model):
    ctc_no = models.AutoField(10, primary_key=True)
    u_no = models.IntegerField(null=True)
    ctc_rec = models.IntegerField(null=True)
    ctc_lastchat = models.DateTimeField(auto_now_add=False)

    class Meta:
        db_table = 'sg_chat_check'

class Sg_comp_check(models.Model):
    cc_no = models.AutoField(10, primary_key=True)
    u_no = models.IntegerField(null=True)
    c_no = models.IntegerField(null=True)
    cc_yn = models.IntegerField(null=True)

    class Meta:
        db_table = 'sg_comp_check'

class Sg_code(models.Model):
    depth1 = models.CharField(max_length=10, null=True)
    depth2 = models.CharField(max_length=10, null=True)
    depth3 = models.CharField(max_length=10, null=True)
    key = models.CharField(max_length=20, null=True)
    value = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'sg_code'

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


'''
    서비스 이용 관리
'''


def estimateAdmin():
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.reg_date, a.ef_no, b.u_id, a.reg_date as today, a.ef_complete, c.c_name    '
        sql = sql + 'FROM rlink.sg_estimate_from a '
        sql = sql + 'LEFT JOIN rlink.sg_user b '
        sql = sql + 'on a.u_no = b.u_no '
        sql = sql + 'LEFT JOIN (SELECT c.ef_no, d.c_name FROM sg_estimate_to c, sg_comp d WHERE c.et_status = 2 AND c.c_no = d.c_no) c '
        sql = sql + 'on a.ef_no = c.ef_no '
        sql = sql + 'ORDER BY a.reg_date DESC '

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

# 당일자 견적요청 수
def todayEstimateCnt(c_service_addr=None, c_no=None, u_no=None):
    try:
        c = connections['default'].cursor()
        param = []
        sql = ' '
        sql = sql+' select count(*) as count '
        sql = sql+' from  '
        sql = sql+' ( '
        sql = sql+'     SELECT a.reg_date, a.ef_no, a.ef_addr1, a.ef_addr2, a.ef_text, a.ef_complete, a.reg_date as "today", b.et_status, c.efc_yn '
        sql = sql+'     FROM sg_estimate_from a    '
        sql = sql+'         LEFT JOIN ( SELECT x.*               '
        sql = sql+'         FROM sg_estimate_to x             '
        sql = sql+'         WHERE  x.c_no = %s ) b  '
        sql = sql+'         on a.ef_no = b.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c '
        sql = sql+'         on a.ef_no = c.ef_no '
        sql = sql+'         AND c.u_no = %s  '
        sql = sql+'     WHERE date(a.reg_date) = date(now()) '
        sql = sql+'     and (a.ef_complete = "N" or a.ef_complete = "I") '
        sql = sql+'     and %s like CONCAT("%%", a.ef_addr1, "%%") '
        sql = sql+'     and %s like CONCAT("%%", a.ef_addr2, "%%") '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a1.reg_date, a1.ef_no, a1.ef_addr1, a1.ef_addr2, a1.ef_text, a1.ef_complete, a1.reg_date as "today", b1.et_status, c1.efc_yn '
        sql = sql+'     FROM sg_estimate_from a1    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         WHERE  x.c_no = %s ) b1 '
        sql = sql+'         on a1.ef_no = b1.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c1 '
        sql = sql+'         on a1.ef_no = c1.ef_no '
        sql = sql+'         AND c1.u_no = %s  '
        sql = sql+'     WHERE date(a1.reg_date) = date(now()) '
        sql = sql+'     and (a1.ef_complete = "S" and a1.c_no = %s ) '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a2.reg_date, a2.ef_no, a2.ef_addr1, a2.ef_addr2, a2.ef_text, a2.ef_complete, a2.reg_date as "today", b2.et_status, c2.efc_yn '
        sql = sql+'     FROM sg_estimate_from a2    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         WHERE  x.c_no = %s ) b2  '
        sql = sql+'         on a2.ef_no = b2.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c2 '
        sql = sql+'         on a2.ef_no = c2.ef_no '
        sql = sql+'         AND c2.u_no = %s  '
        sql = sql+'     WHERE date(a2.reg_date) = date(now()) '
        sql = sql+'      and (a2.ef_complete = "Y" and a2.ef_no = b2.ef_no) '
        sql = sql+' ) x '
        sql = sql+' ORDER BY ef_no DESC '

        param.append(c_no)
        param.append(u_no)
        param.append(c_service_addr)
        param.append(c_service_addr)
        param.append(c_no)
        param.append(u_no)
        param.append(c_no)
        param.append(c_no)
        param.append(u_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return []
    finally:
        c.close()


# 관리자 당일자 견적요청 수
def adminTodayEstimateCnt(u_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = ' '
        sql = sql+' select count(*) as count '
        sql = sql+' from  '
        sql = sql+' ( '
        sql = sql+'     SELECT a.reg_date, a.ef_no, a.ef_addr1, a.ef_addr2, a.ef_text, a.ef_complete, a.reg_date as "today", b.et_status, c.efc_yn '
        sql = sql+'     FROM sg_estimate_from a    '
        sql = sql+'         LEFT JOIN ( SELECT x.*               '
        sql = sql+'         FROM sg_estimate_to x             '
        sql = sql+'         ) b  '
        sql = sql+'         on a.ef_no = b.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c '
        sql = sql+'         on a.ef_no = c.ef_no '
        sql = sql+'         AND c.u_no = %s '
        sql = sql+'     WHERE date(a.reg_date) = date(now()) '
        sql = sql+'     and (a.ef_complete = "N" or a.ef_complete = "I") '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a1.reg_date, a1.ef_no, a1.ef_addr1, a1.ef_addr2, a1.ef_text, a1.ef_complete, a1.reg_date as "today", b1.et_status, c1.efc_yn '
        sql = sql+'     FROM sg_estimate_from a1    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'          ) b1 '
        sql = sql+'         on a1.ef_no = b1.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c1 '
        sql = sql+'         on a1.ef_no = c1.ef_no '
        sql = sql+'         AND c1.u_no = %s  '
        sql = sql+'     WHERE date(a1.reg_date) = date(now()) '
        sql = sql+'     and (a1.ef_complete = "S" ) '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a2.reg_date, a2.ef_no, a2.ef_addr1, a2.ef_addr2, a2.ef_text, a2.ef_complete, a2.reg_date as "today", b2.et_status, c2.efc_yn '
        sql = sql+'     FROM sg_estimate_from a2    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         ) b2  '
        sql = sql+'         on a2.ef_no = b2.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c2 '
        sql = sql+'         on a2.ef_no = c2.ef_no '
        sql = sql+'         AND c2.u_no = %s '
        sql = sql+'     WHERE date(a2.reg_date) = date(now()) '
        sql = sql+'      and (a2.ef_complete = "Y" and a2.ef_no = b2.ef_no) '
        sql = sql+' ) x '
        sql = sql+' ORDER BY ef_no DESC '

        param.append(u_no)
        param.append(u_no)
        param.append(u_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return []
    finally:
        c.close()

# 당일자 미답변 수
def todayNoanswerCnt():
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT count(ef_no) as count  '
        sql = sql + 'FROM rlink.sg_estimate_from '
        sql = sql + 'WHERE date(reg_date) = date(now()) '
        sql = sql + 'AND ef_complete = "N" '

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

# 당일자 세탁 의뢰
def todayCompleteCnt(c_service_addr=None, c_no=None, u_no=None):
    try:
        c = connections['default'].cursor()
        param = []
        sql = ' '
        sql = sql+' select count(*) as count '
        sql = sql+' from  '
        sql = sql+' ( '
        sql = sql+'     SELECT a.reg_date, a.ef_no, a.ef_addr1, a.ef_addr2, a.ef_text, a.ef_complete, a.reg_date as "today", b.et_status, c.efc_yn '
        sql = sql+'     FROM sg_estimate_from a    '
        sql = sql+'         LEFT JOIN ( SELECT x.*               '
        sql = sql+'         FROM sg_estimate_to x             '
        sql = sql+'         WHERE  x.c_no = %s ) b  '
        sql = sql+'         on a.ef_no = b.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c '
        sql = sql+'         on a.ef_no = c.ef_no '
        sql = sql+'         AND c.u_no = %s  '
        sql = sql+'     WHERE date(a.reg_date) = date(now()) '
        sql = sql+'     and (a.ef_complete = "N" or a.ef_complete = "I") '
        sql = sql+'     and %s like CONCAT("%%", a.ef_addr1, "%%") '
        sql = sql+'     and %s like CONCAT("%%", a.ef_addr2, "%%") '
        sql = sql+'     and b.et_status >= 2 '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a1.reg_date, a1.ef_no, a1.ef_addr1, a1.ef_addr2, a1.ef_text, a1.ef_complete, a1.reg_date as "today", b1.et_status, c1.efc_yn '
        sql = sql+'     FROM sg_estimate_from a1    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         WHERE  x.c_no = %s ) b1 '
        sql = sql+'         on a1.ef_no = b1.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c1 '
        sql = sql+'         on a1.ef_no = c1.ef_no '
        sql = sql+'         AND c1.u_no = %s  '
        sql = sql+'     WHERE date(a1.reg_date) = date(now()) '
        sql = sql+'     and (a1.ef_complete = "S" and a1.c_no = %s ) '
        sql = sql+'     and b1.et_status >= 2 '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a2.reg_date, a2.ef_no, a2.ef_addr1, a2.ef_addr2, a2.ef_text, a2.ef_complete, a2.reg_date as "today", b2.et_status, c2.efc_yn '
        sql = sql+'     FROM sg_estimate_from a2    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         WHERE  x.c_no = %s ) b2  '
        sql = sql+'         on a2.ef_no = b2.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c2 '
        sql = sql+'         on a2.ef_no = c2.ef_no '
        sql = sql+'         AND c2.u_no = %s  '
        sql = sql+'     WHERE date(a2.reg_date) = date(now()) '
        sql = sql+'      and (a2.ef_complete = "Y" and a2.ef_no = b2.ef_no) '
        sql = sql+'     and b2.et_status >= 2 '
        sql = sql+' ) x '
        sql = sql+' ORDER BY ef_no DESC '

        param.append(c_no)
        param.append(u_no)
        param.append(c_service_addr)
        param.append(c_service_addr)
        param.append(c_no)
        param.append(u_no)
        param.append(c_no)
        param.append(c_no)
        param.append(u_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return []
    finally:
        c.close()

# 관리자 당일자 세탁 의뢰
def adminTodayCompleteCnt(u_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = ' '
        sql = sql+' select count(*) as count '
        sql = sql+' from  '
        sql = sql+' ( '
        sql = sql+'     SELECT a.reg_date, a.ef_no, a.ef_addr1, a.ef_addr2, a.ef_text, a.ef_complete, a.reg_date as "today", b.et_status, c.efc_yn '
        sql = sql+'     FROM sg_estimate_from a    '
        sql = sql+'         LEFT JOIN ( SELECT x.*               '
        sql = sql+'         FROM sg_estimate_to x             '
        sql = sql+'         ) b  '
        sql = sql+'         on a.ef_no = b.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c '
        sql = sql+'         on a.ef_no = c.ef_no '
        sql = sql+'         AND c.u_no = %s '
        sql = sql+'     WHERE date(a.reg_date) = date(now()) '
        sql = sql+'     and (a.ef_complete = "N" or a.ef_complete = "I") '
        sql = sql+'     and b.et_status >= 2 '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a1.reg_date, a1.ef_no, a1.ef_addr1, a1.ef_addr2, a1.ef_text, a1.ef_complete, a1.reg_date as "today", b1.et_status, c1.efc_yn '
        sql = sql+'     FROM sg_estimate_from a1    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         ) b1 '
        sql = sql+'         on a1.ef_no = b1.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c1 '
        sql = sql+'         on a1.ef_no = c1.ef_no '
        sql = sql+'         AND c1.u_no = %s  '
        sql = sql+'     WHERE date(a1.reg_date) = date(now()) '
        sql = sql+'     and (a1.ef_complete = "S" ) '
        sql = sql+'     and b1.et_status >= 2 '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a2.reg_date, a2.ef_no, a2.ef_addr1, a2.ef_addr2, a2.ef_text, a2.ef_complete, a2.reg_date as "today", b2.et_status, c2.efc_yn '
        sql = sql+'     FROM sg_estimate_from a2    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'          ) b2  '
        sql = sql+'         on a2.ef_no = b2.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c2 '
        sql = sql+'         on a2.ef_no = c2.ef_no '
        sql = sql+'         AND c2.u_no = %s '
        sql = sql+'     WHERE date(a2.reg_date) = date(now()) '
        sql = sql+'      and (a2.ef_complete = "Y" and a2.ef_no = b2.ef_no) '
        sql = sql+'     and b2.et_status >= 2 '
        sql = sql+' ) x '
        sql = sql+' ORDER BY ef_no DESC '

        param.append(u_no)
        param.append(u_no)
        param.append(u_no)
        
        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return []
    finally:
        c.close()

'''
    업체
'''

# 회사 정보 리스트(답변 횟수, 세탁의뢰 횟수, 평점, 평점(퍼센트), 후기 건수)
def compInfo(addr1=None, addr2=None):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.c_no, a.c_name, a.c_addr1, a.c_addr2, a.c_addr3, b.etc_count, c.ett_count, d.rv_score, d.rv_score as pscore, d.rv_count   '
        sql = sql + 'FROM rlink.sg_comp a  '
        sql = sql + ' LEFT JOIN (SELECT c_no, count(c_no) as ett_count from rlink.sg_estimate_to GROUP BY c_no) c '
        sql = sql + ' on a.c_no = c.c_no '
        sql = sql + ' LEFT JOIN (SELECT c_no, count(c_no) as etc_count from rlink.sg_estimate_to '
        sql = sql + '      WHERE et_status = 3 GROUP BY c_no) b  '
        sql = sql + ' on a.c_no = b.c_no '
        sql = sql + ' LEFT JOIN (SELECT c_no, avg(rv_score) as rv_score, count(rv_no) as rv_count from rlink.sg_review '
        sql = sql + '      GROUP BY c_no) d  '
        sql = sql + ' on a.c_no = d.c_no '
        if addr1:
            sql = sql + 'WHERE a.c_service_addr like %s '
            param.append('%'+addr1+'%')
        if addr2:
            sql = sql + 'AND a.c_service_addr like %s '
            param.append('%'+addr2+'%')
        sql = sql + 'ORDER BY a.c_no DESC '

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

# 회사 정보 요약
def compSummary(c_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT IFNULL(b.etc_count, 0) etc_count, IFNULL(c.ett_count, 0) ett_count, IFNULL(d.rv_count, 0) rv_count   '
        sql = sql + 'FROM rlink.sg_comp a  '
        sql = sql + ' LEFT JOIN (SELECT c_no, count(c_no) as ett_count from rlink.sg_estimate_to GROUP BY c_no) c '
        sql = sql + ' on a.c_no = c.c_no '
        sql = sql + ' LEFT JOIN (SELECT c_no, count(c_no) as etc_count from rlink.sg_estimate_to '
        sql = sql + '      WHERE et_status = 3 GROUP BY c_no) b  '
        sql = sql + ' on a.c_no = b.c_no '
        sql = sql + ' LEFT JOIN (SELECT c_no, avg(rv_score) as rv_score, count(rv_no) as rv_count from rlink.sg_review '
        sql = sql + '      GROUP BY c_no) d  '
        sql = sql + ' on a.c_no = d.c_no '
        sql = sql + 'WHERE a.c_no = %s '

        param.append(c_no)

        print(sql)
        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()


def compWorks(c_service_addr, c_no, u_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = ' '
        sql = sql+' select * '
        sql = sql+' from  '
        sql = sql+' ( '
        sql = sql+'     SELECT a.reg_date, a.ef_no, a.ef_addr1, a.ef_addr2, a.ef_addr3, a.ef_text, a.ef_complete, a.reg_date as "today", a.u_no, a.ef_kind, a.ef_req_list, a.ef_name, b.et_no, b.et_status, b.et_total_amt, c.efc_yn '
        sql = sql+'     FROM sg_estimate_from a    '
        sql = sql+'         LEFT JOIN ( SELECT x.*               '
        sql = sql+'         FROM sg_estimate_to x             '
        sql = sql+'         WHERE  x.c_no = %s ) b  '
        sql = sql+'         on a.ef_no = b.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c '
        sql = sql+'         on a.ef_no = c.ef_no '
        sql = sql+'         AND c.u_no = %s  '
        #sql = sql+'     WHERE date(a.reg_date) = date(now()) '
        sql = sql+'     WHERE  '
        sql = sql+'      (a.ef_complete = "N" or a.ef_complete = "I") '
        sql = sql+'     and %s like CONCAT("%%", a.ef_addr1, "%%") '
        sql = sql+'     and %s like CONCAT("%%", a.ef_addr2, "%%") '
        sql = sql+'     and b.et_status >= 2 '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a1.reg_date, a1.ef_no, a1.ef_addr1, a1.ef_addr2, a1.ef_addr3, a1.ef_text, a1.ef_complete, a1.reg_date as "today", a1.u_no, a1.ef_kind, a1.ef_req_list, a1.ef_name, b1.et_no, b1.et_status, b1.et_total_amt, c1.efc_yn '
        sql = sql+'     FROM sg_estimate_from a1    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         WHERE  x.c_no = %s ) b1 '
        sql = sql+'         on a1.ef_no = b1.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c1 '
        sql = sql+'         on a1.ef_no = c1.ef_no '
        sql = sql+'         AND c1.u_no = %s  '
        #sql = sql+'     WHERE date(a1.reg_date) = date(now()) '
        sql = sql+'     WHERE '
        sql = sql+'      (a1.ef_complete = "S" and a1.c_no = %s ) '
        sql = sql+'     and b1.et_status >= 2 '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a2.reg_date, a2.ef_no, a2.ef_addr1, a2.ef_addr2, a2.ef_addr3, a2.ef_text, a2.ef_complete, a2.reg_date as "today", a2.u_no, a2.ef_kind, a2.ef_req_list, a2.ef_name, b2.et_no, b2.et_status, b2.et_total_amt, c2.efc_yn '
        sql = sql+'     FROM sg_estimate_from a2    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         WHERE  x.c_no = %s ) b2  '
        sql = sql+'         on a2.ef_no = b2.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c2 '
        sql = sql+'         on a2.ef_no = c2.ef_no '
        sql = sql+'         AND c2.u_no = %s  '
        #sql = sql+'     WHERE date(a2.reg_date) = date(now()) '
        sql = sql+'     WHERE '
        sql = sql+'      (a2.ef_complete = "Y" and a2.ef_no = b2.ef_no) '
        sql = sql+'     and b2.et_status >= 2 '
        sql = sql+' ) x '
        sql = sql+' ORDER BY ef_no DESC '

        param.append(c_no)
        param.append(u_no)
        param.append(c_service_addr)
        param.append(c_service_addr)
        param.append(c_no)
        param.append(u_no)
        param.append(c_no)
        param.append(c_no)
        param.append(u_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

# 견적요청자 아이디와 견적응답자 아이디로 둘간의 거래내역을 찾아서 최신순으로 정렬함
def getEstimateUserComp(u_id, c_u_id):
    try:
        c = connections['default'].cursor()
        param = [c_u_id, u_id]
        sql = 'SELECT a.ef_no, a.ef_name, a.ef_addr1, a.ef_addr2, a.ef_addr3, a.ef_kind, a.ef_req_list, a.u_no, c.u_name,   '
        sql = sql + ' b.c_name, b.et_no, b.c_no, b.et_status, b.et_total_amt, b.et_obj_1, b.et_obj_2, b.et_obj_3, b.et_obj_4, b.et_obj_5  '
        sql = sql + ' FROM sg_estimate_from a  '
        sql = sql + '   LEFT JOIN ( SELECT y.c_name, x.*  '
        sql = sql + '               FROM sg_estimate_to x, sg_comp y, sg_user z  '
        sql = sql + '               WHERE z.u_no = %s '
        sql = sql + '                 AND y.u_no = z.u_no '
        sql = sql + '                 AND x.c_no = y.c_no '
        sql = sql + '                 ) b '
        sql = sql + '   on a.ef_no = b.ef_no '
        sql = sql + '   LEFT JOIN sg_user c '
        sql = sql + '   on a.u_no = c.u_no '
        sql = sql + ' WHERE a.u_no = %s '
        sql = sql + ' order by a.reg_date desc '

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

#회사 후기 건수 및 평점 평균
def compAvg(c_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT count(rv_no) as count, avg(rv_score) as avg_score  '
        sql = sql + ' FROM sg_review '
        sql = sql + ' WHERE c_no = %s '

        param.append(c_no)
        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

# 지역내 업체 확인
def compInArea(addr1=None, addr2=None):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT u_no  '
        sql = sql + 'FROM rlink.sg_comp '
        sql = sql + 'WHERE c_service_addr like %s '
        sql = sql + 'AND c_service_addr like %s '
        sql = sql + 'ORDER BY c_no DESC '

        param.append('%' + addr1 + '%')
        param.append('%' + addr2 + '%')

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()


'''
    리뷰
'''

# 사용자 리뷰목록
def reviewListUser(u_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT c.c_name, b.rv_score, b.rv_text, b.rv_no    '
        sql = sql + 'FROM rlink.sg_estimate_from a, '
        sql = sql + '     rlink.sg_review b, '
        sql = sql + '     rlink.sg_comp c '
        sql = sql + 'WHERE a.u_no = %s '
        sql = sql + 'AND a.ef_complete = "Y" '
        sql = sql + 'AND a.ef_no = b.ef_no '
        sql = sql + 'AND b.c_no = c.c_no '
        sql = sql + 'ORDER BY b.rv_no DESC '

        param.append(u_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

# 사용자 후기 미등록목룍
def noReviewListUser(u_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.ef_no, c.et_no, b.c_no, b.c_name, c.et_total_amt    '
        sql = sql + 'FROM rlink.sg_estimate_from a, '
        sql = sql + '     rlink.sg_comp b, '
        sql = sql + '     rlink.sg_estimate_to c '
        sql = sql + 'WHERE a.u_no = %s '
        sql = sql + 'AND a.ef_complete = "Y" '
        sql = sql + 'AND a.ef_no not in (SELECT ef_no FROM sg_review) '
        sql = sql + 'AND b.c_no = c.c_no '
        sql = sql + 'AND a.ef_no = c.ef_no '
        sql = sql + 'AND c.et_status = 3 '
        sql = sql + 'ORDER BY c.et_no DESC '

        param.append(u_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

'''
    게시판
'''

def boardListMain(cat):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.br_no, a.br_title, a.br_regdate, a.st_no   '
        sql = sql + 'FROM rlink.sg_board a '
        sql = sql + 'WHERE a.ct_no = %s '
        sql = sql + 'ORDER BY a.br_no DESC '
        sql = sql + 'LIMIT 4 '

        param.append(cat)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()


def boardListPage(cat):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.br_no  '
        sql = sql + 'FROM rlink.sg_board a '
        sql = sql + 'WHERE a.ct_no = %s '

        param.append(cat)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

def boardList(cat, cnt):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.br_no, a.br_title, a.br_regdate, a.st_no  '
        sql = sql + 'FROM rlink.sg_board a '
        sql = sql + 'WHERE a.ct_no = %s '
        sql = sql + 'ORDER BY a.br_no DESC '
        sql = sql + 'LIMIT %s, 10'

        param.append(cat)
        param.append(cnt)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

def boardDetail(br_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.br_title, a.br_regdate, a.br_text, a.ct_no, a.u_no, b.ct_name  '
        sql = sql + 'FROM rlink.sg_board a, '
        sql = sql + '     rlink.sg_category b '
        sql = sql + 'WHERE a.ct_no = b.ct_no '
        sql = sql + 'AND a.br_no = %s '

        param.append(br_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
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


'''
    견적
'''

def estimatefComp(c_service_addr, c_no, u_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = ' '
        sql = sql+' select * '
        sql = sql+' from  '
        sql = sql+' ( '
        sql = sql+'     SELECT a.reg_date, a.ef_no, a.ef_addr1, a.ef_addr2, a.ef_text, a.ef_complete, a.reg_date as "today", a.u_no, b.et_no, b.et_status, c.efc_yn '
        sql = sql+'     FROM sg_estimate_from a    '
        sql = sql+'         LEFT JOIN ( SELECT x.*               '
        sql = sql+'         FROM sg_estimate_to x             '
        sql = sql+'         WHERE  x.c_no = %s ) b  '
        sql = sql+'         on a.ef_no = b.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c '
        sql = sql+'         on a.ef_no = c.ef_no '
        sql = sql+'         AND c.u_no = %s  '
        #sql = sql+'     WHERE date(a.reg_date) = date(now()) '
        sql = sql+'     WHERE  '
        sql = sql+'      (a.ef_complete = "N" or a.ef_complete = "I") '
        sql = sql+'     and %s like CONCAT("%%", a.ef_addr1, "%%") '
        sql = sql+'     and %s like CONCAT("%%", a.ef_addr2, "%%") '
        #sql = sql+'     and b.et_status >= 2 '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a1.reg_date, a1.ef_no, a1.ef_addr1, a1.ef_addr2, a1.ef_text, a1.ef_complete, a1.reg_date as "today", a1.u_no, b1.et_no, b1.et_status, c1.efc_yn '
        sql = sql+'     FROM sg_estimate_from a1    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         WHERE  x.c_no = %s ) b1 '
        sql = sql+'         on a1.ef_no = b1.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c1 '
        sql = sql+'         on a1.ef_no = c1.ef_no '
        sql = sql+'         AND c1.u_no = %s  '
        #sql = sql+'     WHERE date(a1.reg_date) = date(now()) '
        sql = sql+'     WHERE '
        sql = sql+'      (a1.ef_complete = "S" and a1.c_no = %s ) '
        #sql = sql+'     and b1.et_status >= 2 '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a2.reg_date, a2.ef_no, a2.ef_addr1, a2.ef_addr2, a2.ef_text, a2.ef_complete, a2.reg_date as "today", a2.u_no, b2.et_no, b2.et_status, c2.efc_yn '
        sql = sql+'     FROM sg_estimate_from a2    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         WHERE  x.c_no = %s ) b2  '
        sql = sql+'         on a2.ef_no = b2.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c2 '
        sql = sql+'         on a2.ef_no = c2.ef_no '
        sql = sql+'         AND c2.u_no = %s  '
        #sql = sql+'     WHERE date(a2.reg_date) = date(now()) '
        sql = sql+'     WHERE '
        sql = sql+'      (a2.ef_complete = "Y" and a2.ef_no = b2.ef_no) '
        #sql = sql+'     and b2.et_status >= 2 '
        sql = sql+' ) x '
        sql = sql+' ORDER BY ef_no DESC '

        param.append(c_no)
        param.append(u_no)
        param.append(c_service_addr)
        param.append(c_service_addr)
        param.append(c_no)
        param.append(u_no)
        param.append(c_no)
        param.append(c_no)
        param.append(u_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return []
    finally:
        c.close()


def adminEstimatefComp(u_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = ' '
        sql = sql+' select * '
        sql = sql+' from  '
        sql = sql+' ( '
        sql = sql+'     SELECT a.reg_date, a.ef_no, a.ef_addr1, a.ef_addr2, a.ef_text, a.ef_complete, a.reg_date as "today", a.u_no, b.et_no, b.et_status, c.efc_yn '
        sql = sql+'     FROM sg_estimate_from a    '
        sql = sql+'         LEFT JOIN ( SELECT x.*               '
        sql = sql+'         FROM sg_estimate_to x             '
        sql = sql+'          ) b  '
        sql = sql+'         on a.ef_no = b.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c '
        sql = sql+'         on a.ef_no = c.ef_no '
        sql = sql+'         AND c.u_no = %s  '
        #sql = sql+'     WHERE date(a.reg_date) = date(now()) '
        sql = sql+'     WHERE  '
        sql = sql+'      (a.ef_complete = "N" or a.ef_complete = "I") '
        #sql = sql+'     and b.et_status >= 2 '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a1.reg_date, a1.ef_no, a1.ef_addr1, a1.ef_addr2, a1.ef_text, a1.ef_complete, a1.reg_date as "today", a1.u_no, b1.et_no, b1.et_status, c1.efc_yn '
        sql = sql+'     FROM sg_estimate_from a1    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'          ) b1 '
        sql = sql+'         on a1.ef_no = b1.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c1 '
        sql = sql+'         on a1.ef_no = c1.ef_no '
        sql = sql+'         AND c1.u_no = %s '
        #sql = sql+'     WHERE date(a1.reg_date) = date(now()) '
        sql = sql+'     WHERE '
        sql = sql+'      (a1.ef_complete = "S" ) '
        #sql = sql+'     and b1.et_status >= 2 '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a2.reg_date, a2.ef_no, a2.ef_addr1, a2.ef_addr2, a2.ef_text, a2.ef_complete, a2.reg_date as "today", a2.u_no, b2.et_no, b2.et_status, c2.efc_yn '
        sql = sql+'     FROM sg_estimate_from a2    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         ) b2  '
        sql = sql+'         on a2.ef_no = b2.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c2 '
        sql = sql+'         on a2.ef_no = c2.ef_no '
        sql = sql+'         AND c2.u_no = %s  '
        #sql = sql+'     WHERE date(a2.reg_date) = date(now()) '
        sql = sql+'     WHERE '
        sql = sql+'      (a2.ef_complete = "Y" and a2.ef_no = b2.ef_no) '
        #sql = sql+'     and b2.et_status >= 2 '
        sql = sql+' ) x '
        sql = sql+' ORDER BY ef_no DESC '

        param.append(u_no)
        param.append(u_no)
        param.append(u_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return []
    finally:
        c.close()

def estimateCheck(c_service_addr, u_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.ef_no  '
        sql = sql + 'FROM rlink.sg_estimate_from a  '
        sql = sql + 'WHERE %s like CONCAT("%%", a.ef_addr1, "%%") '
        sql = sql + 'AND %s like CONCAT("%%", a.ef_addr2, "%%") '
        sql = sql + 'AND a.u_no = %s '
        sql = sql + 'ORDER BY a.ef_no DESC '

        param.append(c_service_addr)
        param.append(c_service_addr)
        param.append(u_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

def noanwserfComp(c_service_addr, c_no, u_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = ' '
        sql = sql+' select * '
        sql = sql+' from  '
        sql = sql+' ( '
        sql = sql+'     SELECT a.reg_date, a.ef_no, a.ef_addr1, a.ef_addr2, a.ef_text, a.ef_complete, a.reg_date as "today", a.u_no, b.et_status, c.efc_yn '
        sql = sql+'     FROM sg_estimate_from a    '
        sql = sql+'         LEFT JOIN ( SELECT x.*               '
        sql = sql+'         FROM sg_estimate_to x             '
        sql = sql+'         WHERE  x.c_no = %s ) b  '
        sql = sql+'         on a.ef_no = b.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c '
        sql = sql+'         on a.ef_no = c.ef_no '
        sql = sql+'         AND c.u_no = %s  '
        #sql = sql+'     WHERE date(a.reg_date) = date(now()) '
        sql = sql+'     WHERE  '
        sql = sql+'      (a.ef_complete = "N" or a.ef_complete = "I") '
        sql = sql+'     and %s like CONCAT("%%", a.ef_addr1, "%%") '
        sql = sql+'     and %s like CONCAT("%%", a.ef_addr2, "%%") '
        sql = sql+'     and b.et_status is null '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a1.reg_date, a1.ef_no, a1.ef_addr1, a1.ef_addr2, a1.ef_text, a1.ef_complete, a1.reg_date as "today", a1.u_no, b1.et_status, c1.efc_yn '
        sql = sql+'     FROM sg_estimate_from a1    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         WHERE  x.c_no = %s ) b1 '
        sql = sql+'         on a1.ef_no = b1.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c1 '
        sql = sql+'         on a1.ef_no = c1.ef_no '
        sql = sql+'         AND c1.u_no = %s  '
        #sql = sql+'     WHERE date(a1.reg_date) = date(now()) '
        sql = sql+'     WHERE '
        sql = sql+'      (a1.ef_complete = "S" and a1.c_no = %s ) '
        sql = sql+'     and b1.et_status is null '
        sql = sql+'     UNION '
        sql = sql+'     SELECT a2.reg_date, a2.ef_no, a2.ef_addr1, a2.ef_addr2, a2.ef_text, a2.ef_complete, a2.reg_date as "today", a2.u_no, b2.et_status, c2.efc_yn '
        sql = sql+'     FROM sg_estimate_from a2    '
        sql = sql+'         LEFT JOIN ( SELECT x.*                '
        sql = sql+'         FROM sg_estimate_to x              '
        sql = sql+'         WHERE  x.c_no = %s ) b2  '
        sql = sql+'         on a2.ef_no = b2.ef_no '
        sql = sql+'         LEFT JOIN sg_estimate_check c2 '
        sql = sql+'         on a2.ef_no = c2.ef_no '
        sql = sql+'         AND c2.u_no = %s  '
        #sql = sql+'     WHERE date(a2.reg_date) = date(now()) '
        sql = sql+'     WHERE '
        sql = sql+'      (a2.ef_complete = "Y" and a2.ef_no = b2.ef_no) '
        sql = sql+'     and b2.et_status is null '
        sql = sql+' ) x '
        sql = sql+' ORDER BY ef_no DESC '

        param.append(c_no)
        param.append(u_no)
        param.append(c_service_addr)
        param.append(c_service_addr)
        param.append(c_no)
        param.append(u_no)
        param.append(c_no)
        param.append(c_no)
        param.append(u_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return []
    finally:
        c.close()

def estimatetComp(ef_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.*   '
        sql = sql + 'FROM rlink.sg_estimate_to a '
        sql = sql + 'WHERE a.ef_no = %s '
        sql = sql + 'AND a.et_status >= 2 '
        sql = sql + 'ORDER BY a.et_no DESC '

        param.append(ef_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

def reqList(u_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.*, b.et_status, d.chatid    '
        sql = sql + 'FROM rlink.sg_estimate_from a '
        sql = sql + '     LEFT JOIN sg_estimate_to b  '
        sql = sql + '     on a.ef_no = b.ef_no  '
        sql = sql + '     and b.et_status = (SELECT max(c.et_status) FROM sg_estimate_to c WHERE b.ef_no=c.ef_no) '
        sql = sql + '     LEFT JOIN sg_comp c  '
        sql = sql + '     on b.c_no = c.c_no  '
        sql = sql + '     LEFT JOIN sg_user d  '
        sql = sql + '     on c.u_no = d.u_no  '
        sql = sql + 'WHERE a.u_no = %s '
        sql = sql + 'GROUP BY a.ef_no '
        sql = sql + 'ORDER BY a.ef_no DESC '

        param.append(u_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

def reqEstList(u_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.*, b.et_status, d.chatid   '
        sql = sql + 'FROM rlink.sg_estimate_from a '
        sql = sql + '     LEFT JOIN sg_estimate_to b  '
        sql = sql + '     on a.ef_no = b.ef_no  '
        sql = sql + '     and b.et_status = (SELECT max(c.et_status) FROM sg_estimate_to c WHERE b.ef_no=c.ef_no) '
        sql = sql + '     LEFT JOIN sg_comp c  '
        sql = sql + '     on b.c_no = c.c_no  '
        sql = sql + '     LEFT JOIN sg_user d  '
        sql = sql + '     on c.u_no = d.u_no  '
        sql = sql + 'WHERE a.u_no = %s '
        sql = sql + 'AND a.ef_complete != "N"  '
        sql = sql + 'AND b.et_status is not null '
        sql = sql + 'GROUP BY a.ef_no '
        sql = sql + 'ORDER BY a.ef_no DESC '

        param.append(u_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

def estimateServiceComp(c_no):
    try:
        c = connections['default'].cursor()
        param = []
        sql = 'SELECT a.*, b.ef_addr1, b.ef_addr2, b.ef_text, b.u_no   '
        sql = sql + 'FROM rlink.sg_estimate_to a '
        sql = sql + '     LEFT JOIN sg_estimate_from b  '
        sql = sql + '     on a.ef_no =b.ef_no '
        sql = sql + 'WHERE a.c_no = %s '
        sql = sql + 'ORDER BY FIELD(a.et_status, 1) DESC, '
        sql = sql + ' a.et_no DESC '

        param.append(c_no)

        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()


'''
    코드
'''

def selectCode(depth3, depth1=None):
    try:
        c = connections['default'].cursor()
        param = [depth3]
        sql = 'SELECT a.key, a.value '
        sql = sql + 'FROM rlink.sg_code a '
        sql = sql + 'WHERE a.depth3 = %s '
        if depth1:
            param = [depth3, depth1]
            sql = sql + 'AND a.depth1 = %s '
        c.execute(sql, param)
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return False
    finally:
        c.close()

def getCodeSetak(d3, d1="세탁"):
    try:
        c = connections['default'].cursor()
        sql = 'SELECT a.key, a.value  '
        sql = sql + 'FROM rlink.sg_code a '
        sql = sql + 'WHERE a.depth1 = %s '
        sql = sql + 'AND a.depth3 = %s '
        c.execute(sql, [d1, d3])
        rst = dictfetchall(c)
        return rst
    except Exception as e:
        print(e)
        return []
    finally:
        c.close()