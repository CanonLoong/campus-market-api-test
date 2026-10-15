import requests

BASE_URL = "http://localhost:8080"


def test_goods_list():
    # 商品列表不需要 Token，直接请求
    url = BASE_URL + "/api/goods/page"  # ⚠️ 这里自己回想或去 Swagger 找真实的商品列表路径
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json()["code"] == 200


def test_goods_add(token):  # 注意：发布商品需要 token，这里括号里要带上 token
    # 1. 路径改成 /api/goods/add（这是刚才抓到的真实路径）
    url = BASE_URL + "/api/goods/add"

    # 2. ⚠️ 重点！刚才截图里的 Header 是 X-Token！别再写 Authorization 了！
    headers = {
        "X-Token": token
    }

    # 3. 数据改成刚才在 Swagger 里成功的那组
    data = {
        "title": "九成新 Java 教材",
        "description": "这是一本九成新的二手教材，无笔记，包邮，适合考研。",
        "price": 25.5,
        "originalPrice": 59.0,
        "categoryId": 1,
        "conditionLevel": 2,
        # 换成文档里给的那段 Base64 图片
        "images": [
            "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIj48cmVjdCB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgZmlsbD0iI2YzNjZGMSIvPjwvc3ZnPg=="]
    }

    res = requests.post(url, json=data, headers=headers)

    # 4. 断言业务码必须是 200
    assert res.status_code == 200
    assert res.json()["code"] == 200, f"发布失败: {res.json()['message']}"