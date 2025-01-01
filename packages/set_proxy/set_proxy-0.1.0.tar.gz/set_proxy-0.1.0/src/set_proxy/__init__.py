import os


def set_socks(port=20170):
  os.environ["http_proxy"] = f"socks5://127.0.0.1:{port}"
  os.environ["https_proxy"] = f"socks5://127.0.0.1:{port}"
  os.environ["all_proxy"] = f"socks5://127.0.0.1:{port}"
  print(f"set socks5://127.0.0.1:{port}")


def set_http_proxy(port=1087):
  os.environ["http_proxy"] = f"http://127.0.0.1:{port}"
  os.environ["https_proxy"] = f"http://127.0.0.1:{port}"
  os.environ["all_proxy"] = f"http://127.0.0.1:{port}"
  print(f"set http://127.0.0.1:{port}")


def check_link(url: str):
  import requests

  seconds = 3
  try:
    response = requests.get(url, timeout=seconds)
    assert response.status_code == 200
    # print(response.text)
    print(f"{url} success")
    return True
  except requests.exceptions.ReadTimeout:
    print(f"{url} ReadTimeout.")
    return False


def check_hf(
  url: str = "https://hf-mirror.com/huggingface/Qwen2-VL/resolve/main/README.md",
):
  return check_link(url)


def check_baidu(url: str = "https://www.baidu.com"):
  return check_link(url)


def check_google(url: str = "https://www.google.com"):
  return check_link(url)


if __name__ == "__main__":
  set_socks()
  check_hf()
  check_google()
