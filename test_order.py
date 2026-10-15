import requests

BASE_URL = "http://localhost:8080"


def test_order_invalid_delivery(buyer_token):
    # 1. 买家预约一个在售商品（你自己去 Swagger 找一个真实在售的商品 id 替换 1）
    goods_id = 1  # ⚠️ 换成真实在售商品的 id
    create_url = BASE_URL + "/api/order/add"
    headers = {"X-Token": buyer_token}
    create_data = {
        "goodsId": goods_id,
        "tradePlace": "图书馆二楼大厅",
        "tradeTime": "2026-10-25T15:00:00",
        "tradeRemark": "希望现场试一下"
    }

    res_create = requests.post(create_url, json=create_data, headers=headers)
    assert res_create.json()["code"] == 200, f"创建订单失败: {res_create.json()['message']}"
    order_id = res_create.json()["data"]  # 拿到订单 id


    # 2. 此时订单是 0 待交易，买家直接去点“确认交付”（这是非法操作）
    delivery_url = f"{BASE_URL}/api/order/{order_id}/delivery"
    res_delivery = requests.post(delivery_url, headers=headers)

    # 3. 预期后端拦截：状态码 400，且返回提示
    print("接口返回：", res_delivery.json())  # 方便你调试看真实文案
    assert res_delivery.json()["code"] == 400
    # 这里先用 in 模糊匹配，不管它文案到底有没有“无法确认交付”，只要报错就行
    assert "当前订单状态为「待交易」" in res_delivery.json()["message"]