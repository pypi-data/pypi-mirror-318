# -*- coding: UTF-8 -*-
# python3

from devolib.util_httpc import GET, POST_JSON, POST_FORM
from devolib.util_json import json_from_str
from devolib.util_log import LOG_D, LOG_E, LOG_F
from devolib.util_fs import fullname_of_path

class FirIM:
    _api_host = 'http://api.appmeta.cn'
    _api_token = None

    def __init__(self, token):
        self._api_token = token
        
    # 发布应用获取上传凭证
    def _get_upload_token(self):
        res = POST_JSON(host=self._api_host, path='/apps', data={
            'type': 'android',
            'bundle_id': 'com.sports8.tennis.ground',
            'api_token': self._api_token
            })
        
        if res is None:
            raise Exception(f'get upload token failed.')

        return res['cert']['binary'] # { key, token, upload_url }
        
    # 上传文件
    def upload_file(self, file_path, name, version, build, changelog=""):
        upload_ticket = self._get_upload_token()

        key = upload_ticket['key']
        token = upload_ticket['token']
        upload_url = upload_ticket['upload_url']
        custom_headers = upload_ticket['custom_headers']

        fullname = fullname_of_path(file_path)

        res = POST_FORM(url=upload_url, form={
          'key': (None, key), 
          'token': (None, token), 
          'file': (fullname, open(file_path, 'rb')),
          'x:name': (None, name),
          'x:version': (None, version),
          'x:build': (None, build),
        #   'x:release_type': '' # only for ios: Adhoc, Inhouse
          'x:changelog': (None, 'xxxxxxx')
        }, headers=custom_headers)

    # 版本查询
    def get_latest_ver(self, app_id, alias=None):
        res = GET(self._api_host, f'/apps/latest/{app_id}?api_token={self._api_token}')

# {
#     "name": "韵动场馆",
#     "version": "84",
#     "changelog": "xxxxxxx",
#     "updated_at": 1725985082,
#     "versionShort": "3.2.14",
#     "build": "84",
#     "installUrl": "https://download.appmeta.cn/apps/653762cd23389f6010122e43/install?download_token=ea3b834259d5d75462c47cfd756a90e3&source=update",
#     "install_url": "https://download.appmeta.cn/apps/653762cd23389f6010122e43/install?download_token=ea3b834259d5d75462c47cfd756a90e3&source=update",
#     "direct_install_url": "https://download.appmeta.cn/apps/653762cd23389f6010122e43/install?download_token=ea3b834259d5d75462c47cfd756a90e3&source=update",
#     "update_url": "http://appdev.sport8.com.cn/q1gau4",
#     "binary": {
#         "fsize": 16396747
#     }
# }
        res = json_from_str(res)

        print(f'')
        print(f'########################')
        if alias is None:
            print(f'Name: {res["name"]}')
        else:
            print(f'Name: {res["name"]} ({alias})')
        print(f'VersionCode: {res["versionShort"]}')
        print(f'Build: {res["version"]}')
        print(f'Install: {res["installUrl"]}')
        print(f'QRCode: {res["update_url"]}')
        print(f'########################')
        print(f'')

#######################################

def cmd_handle_upload(args):
    fir = FirIM(args.token)
    fir.upload_file(args.file, args.name, args.version, args.build)

    fir.get_latest_ver(args.app_id, args.alias)
        

def cmd_handle_latest(args):
    fir = FirIM(args.token)
    fir.get_latest_ver(args.app_id)

def cmd_regist(subparsers):
    parser = subparsers.add_parser('fir.upload', help='fir upload build file')
    parser.add_argument('-t', '--token', type=str, required=True)
    parser.add_argument('-f', '--file', type=str, required=True)
    parser.add_argument('-n', '--name', type=str, required=True)
    parser.add_argument('-v', '--version', type=str, required=True)
    parser.add_argument('-b', '--build', type=str, required=True)
    parser.add_argument('-a', '--app_id', type=str, required=True)
    parser.add_argument('-l', '--alias', type=str, required=False)
    parser.set_defaults(handle=cmd_handle_upload)

    parser = subparsers.add_parser('fir.latest', help='fir get latest version info')
    parser.add_argument('-t', '--token', type=str, required=True)
    parser.add_argument('-a', '--app_id', type=str, required=True)
    parser.set_defaults(handle=cmd_handle_latest)