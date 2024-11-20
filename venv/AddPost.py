from locust import HttpUser, task, between
import random


class AddPosts(HttpUser):
  wait_time = between(1, 2)

  def on_start(self):
    self.client.post("/members/sign-in", json={
      "memberId":"member",
      "password": "1234"
    })

  @task
  def add_post(self):
    self.client.post("/posts", json={
      "name": "테스트 게시글" + str(random.randint(1, 100000)),
      "contents": "테스트 컨텐츠" + str(random.randint(1, 100000)),
      "categoryId": random.randint(1, 10),
      "fileId": random.randint(1, 10),
      "tags":[
        {
          "name":"tag1",
          "url":"https://"
        },
        {
          "name":"tag2",
          "url":"https://"
        }
      ]
    })