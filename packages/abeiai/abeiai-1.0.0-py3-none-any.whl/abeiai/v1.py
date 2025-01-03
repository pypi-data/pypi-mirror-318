import json
import requests
import uuid
import hashlib
import time


class AbeiAI:
    def __init__(self, aap_id: str = '', aap_secret: str = ''):
        self.app_id = aap_id
        self.secret = aap_secret
        self.base_url = 'https://abeiai.com'

    def set_app_id(self, app_id: str):
        self.app_id = app_id

    def set_app_secret(self, app_secret: str):
        self.secret = app_secret

    def set_base_url(self, base_url: str):
        self.base_url = base_url

    @staticmethod
    def _md5(data):
        """
        MD5计算
        :param data: 需要计算的字符串
        :return: MD5值
        """
        md5data = hashlib.md5(str(data).encode(encoding='UTF-8')).hexdigest()
        return md5data

    @staticmethod
    def _sort_data(data, secret):
        """
        发送与接收的数组进行字典排序，排除空字段
        :param data: 需要排序的数组
        :return: 排序完成后拼接成的字符串
        """
        msg = []
        for key, value in sorted(data.items()):
            if value:
                msg.append("%s=%s" % (str(key), str(value)))
        msg.append("key=%s" % secret)
        return "&".join(msg)

    @staticmethod
    def _generate_random_str():
        return uuid.uuid4().hex

    def _post(self, path: str, data: dict) -> (bool, dict):
        url = f"{self.base_url}{path}"
        res = requests.post(url, data=data)
        return bool(res.status_code == 200), res.json()

    def _verity_sign(self, data):
        """
        验证签名
        :param data: 带有签名的字典
        :return: 错误返回False，正确返回字典
        """
        # 验证时间戳不超过5分钟有效期
        if int(time.time()) - data["timestamp"] > 300:
            return False
        sign = data["sign"]
        del data["sign"]
        ret = data if self._md5(self._sort_data(data, self.secret)) == sign else False
        return ret

    def _add_sign(self, data):
        """
        加入签名
        :param data: 需要加签名的字典
        :return: 带上签名的字典
        """
        data["timestamp"] = int(time.time())
        data["nonce_str"] = self._generate_random_str()
        data["sign"] = self._md5(self._sort_data(data, self.secret))
        return data

    def _read(self, key: str, msg_id: str = ''):
        path = "/open/v1/read/"
        req = {
            "app_id": self.app_id,
            "key": key,
        }
        if msg_id:
            req["msg_id"] = msg_id
        return self._post(path, self._add_sign(req))

    def _create(self, key: str, data: dict):
        path = "/open/v1/create/"
        req = {
            "app_id": self.app_id,
            "key": key,
            "data": json.dumps(data)
        }
        return self._post(path, self._add_sign(req))

    def group(self):
        """
        获取分组列表
        :return:
        """
        return self._read('group')

    def app(self):
        """
        获取app信息
        :return:
        """
        return self._read('app')

    def recharge(self):
        """
        获取充值信息
        :return:
        """
        return self._read('recharge')

    def history(self, msg_id: str):
        """
        获取使用信息
        :return:
        """
        return self._read('history', msg_id)

    def draw(self, data: dict):
        return self._create('draw', data)
