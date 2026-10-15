import requests

BASE_URL = "http://localhost:8080"


def test_order_invalid_delivery(buyer_token, seller_token):  # 👈 同时传入买家和卖家 token
    # 1. 买家创建一个订单（状态 0 待交易）
    goods_id = 5  # ⚠️ 换成真实在售商品 id
    create_url = BASE_URL + "/api/order/add"
    headers_buyer = {"X-Token": buyer_token}
    create_data = {
        "goodsId": goods_id,
        "tradePlace": "图书馆二楼大厅",
        "tradeTime": "2026-10-25T15:00:00",
        "tradeRemark": "希望现场试一下"
    }

    res_create = requests.post(create_url, json=create_data, headers=headers_buyer)
    assert res_create.json()["code"] == 200, f"创建订单失败: {res_create.json()['message']}"
    order_id = res_create.json()["data"]

    # 2. 关键：用“卖家”的 token 去点“确认交付”（此时状态为0，卖家想跳过确认直接交付，属于非法流转）
    delivery_url = f"{BASE_URL}/api/order/{order_id}/delivery"
    headers_seller = {"X-Token": seller_token}  # 👈 换成卖家 token
    res_delivery = requests.post(delivery_url, headers=headers_seller)

    # 3. 预期：权限通过了，但是状态机拦截
    print("接口返回：", res_delivery.json())
    assert res_delivery.json()["code"] == 400
    assert "当前订单状态为「待交易」，无法确认交付" in res_delivery.json()["message"]