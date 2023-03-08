# This is a sample Python script.


# 这是单行注释
"""
这是多行注释
这是多行注释
"""
import pymysql as pymysql

'''
也可以用三个单引号来进行多行注释
'''


def get_menu_list(username):
    SQL_CONFIG_MENU = {"host": "172.25.62.63", "port": 3306, "user": 'shunan',
                       "passwd": 'S82-#1KHg', "db": 'new_data_main',
                       "charset": 'utf8'}
    mysql_conn = pymysql.connect(**SQL_CONFIG_MENU)
    mysql_cursor = mysql_conn.cursor()

    select_sql = '''
               SELECT distinct avm.id,avm.name,dir_parent_id,url,type,description,order_key from ab_user u join ab_user_role r on u.id=r.user_id JOIN ab_permission_view_role ar on ar.role_id=r.role_id
               join ab_permission_view apv on ar.permission_view_id=apv.id join ab_view_menu avm on apv.view_menu_id=avm.id
               where u.username=%s and avm.dir_parent_id is not null order by avm.order_key, avm.id
               '''.format()
    if username:
        select_sql = select_sql % (str(username))
    else:
        return []
    result_list = []
    result_dict = {}
    try:
        mysql_cursor.execute(select_sql)
        results = mysql_cursor.fetchall()
        dashboard_name_list = [row[1] for row in results if row[4] == "board"]
        select_dash_sql = f'''select id, slug, dashboard_title from dashboards where dashboard_title in ('{"','".join(dashboard_name_list)}') '''
        mysql_cursor.execute(select_dash_sql)
        dash_results = mysql_cursor.fetchall()
        dashboard_name_id_dict = {row[2]: {"id": row[0], "url": f"/superset/dashboard/{row[1] or row[0]}/"} for row in
                                  dash_results}
        for row in results:
            result = {}
            result['dirId'] = row[0]
            result['name'] = row[1]
            result['dirParentId'] = row[2]
            result['url'] = row[3]
            result['type'] = row[4]
            result['description'] = row[5]
            result['list'] = []
            if row[4] == "board":
                curr_dash = dashboard_name_id_dict.get(row[1])
                if curr_dash is None:
                    continue
                result['dirId'] = curr_dash['id']
                result['url'] = curr_dash['url']
                result['type'] = ""
            result_dict[row[0]] = result
            result_list.append(result)
        mysql_conn.commit()
    except Exception as e:
        mysql_conn.rollback()

    mysql_cursor.close()
    mysql_conn.close()
    for menu in result_list:
        dirParentId = menu.get("dirParentId", None)
        if dirParentId:
            if result_dict.__contains__(dirParentId):
                parent_menu = result_dict.get(dirParentId)
                list = parent_menu.get("list")
                list.append(menu)
                parent_menu['list'] = list
                result_dict[dirParentId] = parent_menu

    values = result_dict.values()
    menu_list = []
    for menu in values:
        dirParentId = menu.get("dirParentId", None)
        if not dirParentId:
            menu_list.append(menu)
    return menu_list


if __name__ == '__main__':
    menu_list = get_menu_list(13100000000)
    print(menu_list)
