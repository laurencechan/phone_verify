# coding=utf-8

import json
import requests

# 请求的头部内容

headers = {
    "X-LC-Id": "w0grSDBm18wlXulEAVjVwp2k-gzGzoHsz",
    "X-LC-Key": "QPcsMuw6eixnhLgJkP2p38wS",
    "Content-Type": "application/json",
}

# 请求发送验证码API
REQUEST_SMS_CODE_URL = "https://leancloud.cn/1.1/requestSmsCode"

# 请求校验验证码 API
VERIFY_SMS_CODE_URL = "https://leancloud.cn/1.1/verifySmsCode/"


def send_message(phone):
    """
    通过POST请求 requestSmsCode API发送验证码到指定手机
    ：param phone: 通过网页表单获取电话号码
    ：:return:
    """

    data = {
        "mobilePhoneNumber": phone,
    }

    # POST 方法参数包含三个部分
    # REQUEST_SMS_CODE_URL: 请求的URL
    # data: 请求的内容，要将内容编码成Json格式
    # headers: 请求的头部，包含 ID KEY以及 Content-Type 信息
    r = requests.post(REQUEST_SMS_CODE_URL, data=json.dumps(data), headers=headers)
    # 响应r的status_code值为200 说明响应成功
    # 否则说明失败
    if r.status_code == 20:
        return True
    else:
        return False


def verify(phone, code):
    """
    发送POST请求到verifySmsCode API获取校验结果
    ：param phone: 通过网页表单获取的电话号
    ：param code： 通过网页表单获取的验证码
    ：return:
    """
    target_url = VERIFY_SMS_CODE_URL + "%s?mobilePhoneNumber=%s" % (code, phone)

    # 这里的POST方法只传入了两个参数

    r = requests.post(target_url,headers=headers)

    if r.status_code == 200:
        return True
    else:
        return False
