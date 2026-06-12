import requests
import sys
import time

BASE_URL = "http://192.168.12.46"

def submit(name):
    sess = requests.Session()
    r = sess.post(f"{BASE_URL}/api/submit_all", json={"name": name, "doubt": ""})
    data = r.json()
    if data.get("success"):
        print(f"[+] {name} 提交成功!")
        return True
    else:
        print(f"[-] 提交失败: {data.get('msg', '未知错误')}")
        return False

def watch(name, interval=36000):
    print(f"[*] 正在监听新任务，每 {interval} 秒检测一次...")
    last_task_id = None

    while True:
        try:
            r = requests.get(f"{BASE_URL}/api/get_status", timeout=5)
            data = r.json()
            task_id = data.get("task_id")

            if task_id is None:
                time.sleep(interval)
                continue

            if last_task_id is None:
                last_task_id = task_id
                print(f"[*] 当前任务ID: {task_id}")
            elif task_id != last_task_id:
                print(f"[*] 检测到新任务! (旧: {last_task_id}, 新: {task_id})")
                submit(name)
                last_task_id = task_id
        except Exception as e:
            print(f"[-] 请求失败: {e}")

        time.sleep(interval)

if __name__ == "__main__":

    name = '王疆龙'

    # while True:

    #     if watch(name):
    
    submit(name)
    # watch(name)

