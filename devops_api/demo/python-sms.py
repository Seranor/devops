import json
import random
from ronglian_sms_sdk import SmsSDK

# 配置文件 settings.py
accId = '2c94811c86c00e9b0186f28b44c60b06'
accToken = 'f2034dcb98e74554a1ff04c6051d8fe5'
appId = '2c94811c86c00e9b0186f28b45b90b0d'
templateId = 1


# 工具函数 utils/
def send_message(mobile, datas, tid=None):
    sdk = SmsSDK(accId, accToken, appId)
    tid = templateId if tid is None else tid
    resp = sdk.sendMessage(tid, mobile, datas)
    response = json.loads(resp)
    return response


if __name__ == '__main__':
    code = f"{random.randint(100000, 999999):06d}"
    resp = send_message('13928835901', (code, 5))
    print(resp)
