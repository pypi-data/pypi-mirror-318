import requests
import json
import urllib.parse


def get_root_xsrf_token():
    """
    获取站点csrf
    :return: {"xsrf_token": _xsrf_token, "pterodactyl_session": _pterodactyl_session}
    """
    res = requests.get('https://minekuai.com/', headers={
        'X-Requested-With': 'XMLHttpRequest'
    })
    _xsrf_token = res.cookies.get('XSRF-TOKEN')
    _pterodactyl_session = res.cookies.get('pterodactyl_session')
    return {"xsrf_token": _xsrf_token, "pterodactyl_session": _pterodactyl_session}


def get_xsrf_token(token):
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    res = requests.get('https://minekuai.com/sanctum/csrf-cookie', headers={
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session};',
        'X-Xsrf-Token': _xsrf_token
    })
    _xsrf_token = res.cookies.get('XSRF-TOKEN')
    _pterodactyl_session = res.cookies.get('pterodactyl_session')
    return {"xsrf_token": _xsrf_token, "pterodactyl_session": _pterodactyl_session}

def login_user(token, user):
    flag = True
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    username = user['username']
    password = user['password']

    res = requests.post('https://minekuai.com/auth/login', headers={
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session};',
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }, json={
        "user": username,
        "password": password,
    })
    content = json.loads(res.text)
    if 'errors' in content:
        print(content['errors'][0]['detail'])
        print('# ERROR #')
        flag = False
    else:
        print('登录成功')
    _xsrf_token = res.cookies.get('XSRF-TOKEN')
    _pterodactyl_session = res.cookies.get('pterodactyl_session')
    _remember_web = res.cookies.get('remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d')
    return {"xsrf_token": _xsrf_token, "pterodactyl_session": _pterodactyl_session, "remember_web": _remember_web}, flag

def get_user_info(token):
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    _remember_web = token['remember_web']
    res = requests.get('https://minekuai.com/api/client/account', headers={
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d={_remember_web}',
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    })
    return json.loads(res.text)

def get_user_id(_info):
    return str(_info['attributes']['id'])

def signin(token, _user_id):
    _xsrf_token = token['xsrf_token']
    res = requests.post('https://api.ungc.com.cn/api/minekuai/points/signIn', headers={
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'Content-Type': 'application/json'
    }, data=_user_id)
    content = json.loads(res.text)
    if 'code' in content:
        if content['code'] == 1:
            print(content['msg'])
        else:
            print(content['msg'])
    else:
        print(f'请求异常：{content["error"]}')

def get_server_id(token, _user_id):
    _xsrf_token = token['xsrf_token']
    res = requests.get(f'https://api.ungc.com.cn/api/minekuai/getServersByOwnerId?owner_id={_user_id}', headers={
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'Content-Type': 'application/json'
    })
    content = json.loads(res.text)
    if len(content['data']) == 0:
        print('没有找到服务器')
        return False
    return content['data'][0]['id']

def modify_server_suspend_time(token, _user_id, server):
    _xsrf_token = token['xsrf_token']
    _server_id = server['attributes']['id']
    res = requests.post('https://api.ungc.com.cn/api/minekuai/modifyServerSuspendTime', headers={
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'Content-Type': 'application/json'
    }, json={
        'user_id': _user_id,
        'server_id': _server_id,
        'days': 1,
        'prices': 100
    })
    content = json.loads(res.text)
    if content['code'] == 1:
        print(content['msg'])
    else:
        print(f'续费失败：{content["msg"]}')

def get_server_list(token, page=1):
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    _remember_web = token['remember_web']
    res = requests.get(f'https://minekuai.com/api/client?page={page}', headers={
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d={_remember_web}',
        'X-Xsrf-Token': urllib.parse.quote(_xsrf_token),
        'Accept': 'application/json',
    })
    content = json.loads(res.text)
    return content['data']

def set_server_startup(token, server, _startup='/bin/bash'):
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    _remember_web = token['remember_web']
    _uuid = server['attributes']['uuid']
    res = requests.post(f'https://minekuai.com/api/client/servers/{_uuid}/startup/startup/change', headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d={_remember_web}',
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'X-Requested-With': 'XMLHttpRequest',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }, json={
        "startup": _startup
    })
    content = json.loads(res.text)
    print(content)
    pass

def add_server_start_task(token, server):
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    _remember_web = token['remember_web']
    _uuid = server['attributes']['uuid']
    res = requests.post(f'https://minekuai.com/api/client/servers/{_uuid}/schedules', headers={
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d={_remember_web}',
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }, json={
        'is_active': True,
        'only_when_online': False,
        'name': '1',
        'minute': '*',
        'hour': '*',
        'day_of_month': '*',
        'day_of_week': '*',
        'month': '*'
    })
    content = json.loads(res.text)
    print(content)
    task_id = content['attributes']['id']
    res = requests.post(f'https://minekuai.com/api/client/servers/{_uuid}/schedules/{task_id}/tasks', headers={
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d={_remember_web}',
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }, json={
        'action': 'power',
        'payload': 'start',
        'continue_on_failure': True,
        'time_offset': '0'
    })
    content = json.loads(res.text)
    print(content)
    pass

def register_send_mail(token, user):
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    _email = user['email']
    _username = user['username']
    res = requests.post('https://minekuai.com/auth/register', headers={
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}',
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }, json={
        'email': _email,
        'username': _username,
        'firstname': _username,
        'lastname': _username,
    })
    content = json.loads(res.content)
    if 'errors' in content:
        print(f'发送失败：{content["errors"][0]["detail"]}')
    elif 'error' in content:
        print(f'发送失败：{content["error"]}')
    else:
        print(f'发送成功，用户名：{_username}，邮箱：{_email}')

def submit_password(url, password):
    token = url.split('/')[-1].split('?')[0]
    email = urllib.parse.unquote(url.split('=')[-1])
    res = requests.get(url)
    _xsrf_token = res.cookies.get('XSRF-TOKEN')
    _pterodactyl_session = res.cookies.get('pterodactyl_session')
    result = requests.post('https://minekuai.com/auth/password/reset', headers={
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}',
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }, json={
        'email': email,
        'token': token,
        'password': password,
        'password_confirmation': password,
    })
    content = json.loads(result.text)
    if 'success' in content:
        print('密码设置成功')
    elif 'errors' in content:
        for error in content['errors']:
            print(error['detail'])
    else:
        print(content)

def get_user_score(token, _user_id):
    _xsrf_token = token['xsrf_token']
    res = requests.get(f'https://api.ungc.com.cn/api/minekuai/points/getPoints?user_id={_user_id}', headers={
        'X-Xsrf-Token': _xsrf_token
    })
    content = json.loads(res.text)
    print(f'当前积分: {content["points"]}')
    return content["points"]

def redeem_code(token, _user_id, _code):
    _xsrf_token = token['xsrf_token']
    res = requests.post('https://api.ungc.com.cn/api/minekuai/redeem/redeem', headers={
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
    }, json={
        'userId': _user_id,
        'redeem_id': _code,
    })
    content = json.loads(res.text)
    if content['code'] == 1:
        print(content['msg'])
    else:
        print(content['msg'])


def user_logout(token):
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    _remember_web = token['remember_web']
    requests.post('https://minekuai.com/auth/logout', headers={
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}; remember_web={_remember_web}'
    })

def create_server(token, _user_id):
    _xsrf_token = token['xsrf_token']
    res = requests.post('https://api.ungc.com.cn/api/minekuai/createServer', headers={
        'X-Xsrf-Token': _xsrf_token,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
    }, json={
        'user_id': _user_id,
        'points': 100,
        'days': 1,
    })
    content = json.loads(res.content)
    if 'code' in content:
        if content['code'] == 1:
            print('创建服务器成功')
        else:
            print(content['msg'])
    else:
        print(content)

def set_server_name(token, server, _server_name):
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    _remember_web = token['remember_web']
    _server_uuid = server['attributes']['uuid']
    requests.post(f'https://minekuai.com/api/client/servers/{_server_uuid}/settings/rename', headers={
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d={_remember_web};',
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
    }, json={
        'name': _server_name,
    })

def add_server_sub_user(token, server, _sub_user_email):
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    _remember_web = token['remember_web']
    _uuid = server['attributes']['uuid']
    requests.post(f'https://minekuai.com/api/client/servers/{_uuid}/users', headers={
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d={_remember_web};',
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
    }, json={
        'email': _sub_user_email,
        'permissions': [
            "websocket.connect", "control.console", "control.start", "control.stop", "control.restart", "user.create",
            "user.read", "user.update", "user.delete", "file.create", "file.read", "file.read-content", "file.update",
            "file.delete", "file.archive", "file.sftp", "allocation.read", "allocation.create", "allocation.update",
            "allocation.delete", "startup.read", "startup.update", "startup.docker-image", "schedule.create",
            "schedule.read", "schedule.update", "schedule.delete", "settings.rename", "settings.reinstall"
        ]
    })

def get_server_sub_user(token, server):
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    _remember_web = token['remember_web']
    _server_id = server['attributes']['id']
    res = requests.get(f'https://minekuai.com/api/client/servers/{_server_id}/users', headers={
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d={_remember_web};',
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
    })
    content = json.loads(res.content)
    return content['data']

def delete_server_sub_user(token, server, _sub_user_id):
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    _remember_web = token['remember_web']
    _server_id = server['attributes']['id']
    res = requests.delete(f'https://minekuai.com/api/client/servers/{_server_id}/users/{_sub_user_id}', headers={
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d={_remember_web};',
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
    })
    print(res.status_code)

def forget_send_email(token, _user):
    _xsrf_token = token['xsrf_token']
    _pterodactyl_session = token['pterodactyl_session']
    email = _user['email']
    res = requests.post('https://minekuai.com/auth/password', headers={
        'X-Xsrf-Token': urllib.parse.unquote(_xsrf_token),
        'Cookie': f'XSRF-TOKEN={_xsrf_token}; pterodactyl_session={_pterodactyl_session}',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }, json={
        'email': email,
    })
    content = json.loads(res.text)
    print(content)

def get_remote_user_list(mail_host="schhz.xyz", password="<PASSWORD>"):
    mail_list = get_all_email()
    _user_list = []
    for mail in mail_list:
        if str(mail['username']).endswith(mail_host):
            _user_list.append({
                'username': mail['full_name'],
                'email': mail['username'],
                'password': password,
            })
    json.dump(_user_list, open('../users.json', 'w'), indent=4)
    return _user_list

def get_user_list(list_name="users"):
    if list_name == 'users' and not os.path.exists(f'./{list_name}.json'):
        get_remote_user_list()
    else:
        print(f'用户列表文件{list_name}不存在')
        return []
    return json.load(open(f'./{list_name}.json'))