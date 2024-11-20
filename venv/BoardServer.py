import json

from locust import HttpUser, task, between
import random


class BoardServer(HttpUser):
  wait_time = between(1, 2)

  def on_start(self):
    # 로그인 요청을 전송하는 코드
    self.client.post("/members/sign-in", json={"memberId": "member",
                                             "password": "1234"})

  @task
  def view_item(self):
    sortStatus = random.choice(
      ["CATEGORIES", "NEWEST", "OLDEST", "HIGHPRICE", "LOWPRICE", "GRADE"])
    categoryId = random.randint(1, 10)
    name = '테스트 게시글'.join(str(random.randint(1, 10000)))
    headers = {'Content-Type': 'application/json'}
    data = {"sortStatus": sortStatus,
            "categoryId": categoryId,
            "name": name}

    self.client.post("/search", json=data, headers=headers)
