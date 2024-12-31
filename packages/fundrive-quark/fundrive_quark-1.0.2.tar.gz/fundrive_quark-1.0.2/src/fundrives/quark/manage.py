# -*- coding: utf-8 -*-
import json
import os
import random
import re
import shutil
import string
import time
from datetime import datetime
from typing import List, Dict, Tuple, Any, Union

import requests
from funutil import getLogger, deep_get

logger = getLogger("fundrive")


def get_id_from_url(url) -> str:
    """pwd_id"""
    pattern = r"/s/(\w+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return ""


def safe_copy(src, dst):
    if not os.path.exists(src):
        print(f"源文件不存在，跳过复制：{src}")
        return

    if os.path.exists(dst):
        os.remove(dst)
        print(f"目标文件已存在，已删除：{dst}")

    try:
        shutil.copy(src, dst)
        print(f"文件已复制到：{dst}")
    except Exception as e:
        print("备份share_url.txt文件错误，", e)


def generate_random_code(length=4):
    characters = string.ascii_letters + string.digits
    random_code = "".join(random.choice(characters) for _ in range(length))
    return random_code


def get_datetime(
    timestamp: Union[int, float, None] = None, fmt: str = "%Y-%m-%d %H:%M:%S"
) -> str:
    if timestamp is None or not isinstance(timestamp, (int, float)):
        return datetime.today().strftime(fmt)
    else:
        dt = datetime.fromtimestamp(timestamp)
        formatted_time = dt.strftime(fmt)
        return formatted_time


class QuarkPanManage:
    def __init__(self, cookies, *args, **kwargs) -> None:
        # self.base_url = 'https://drive.quark.cn/1/clouddrive'
        self.base_url = "https://drive-pc.quark.cn/1/clouddrive"

        self.headers: Dict[str, str] = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
            " Chrome/94.0.4606.71 Safari/537.36 Core/1.94.225.400 QQBrowser/12.2.5544.400",
            "origin": "https://pan.quark.cn",
            "referer": "https://pan.quark.cn/",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": cookies,
        }

    @staticmethod
    def get_pwd_id(share_url: str) -> str:
        return share_url.split("?")[0].split("/s/")[1]

    @staticmethod
    def extract_urls(text: str) -> list:
        url_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
        return re.findall(url_pattern, text)[0]

    def request(
        self,
        uri,
        method="GET",
        params=None,
        headers=None,
        data=None,
        timeout=10,
        *args,
        **kwargs,
    ):
        url = f"{self.base_url}/{uri}"
        params = params or {}
        params.update(
            {
                "pr": "ucpro",
                "fr": "pc",
                "uc_param_str": "",
                "__dt": random.randint(100, 9999),
                "__t": int(time.time()) * 1000,
            }
        )
        return requests.request(
            method,
            url,
            params=params,
            headers=headers or self.headers,
            json=data,
            timeout=timeout,
            *args,
            **kwargs,
        ).json()

    def get_stoken(self, pwd_id: str) -> str:
        data = {"pwd_id": pwd_id, "passcode": ""}
        json_data = self.request(
            "share/sharepage/token",
            "post",
            data=data,
        )
        if json_data["status"] == 200 and json_data["data"]:
            stoken = json_data["data"]["stoken"]
        else:
            stoken = ""
            logger.info(f"文件转存失败，{json_data['message']}")
        return stoken

    def get_detail(
        self,
        pwd_id: str,
        stoken: str,
        pdir_fid: str = "0",
        size=50,
        sort="file_type:asc,updated_at:desc",
    ) -> Tuple[str, List[Dict[str, Union[int, str]]]]:
        file_list: List[Dict[str, Union[int, str]]] = []
        for page in range(1, 100):
            params = {
                "pwd_id": pwd_id,
                "stoken": stoken,
                "pdir_fid": pdir_fid,
                "force": "0",
                "_page": page,
                "_size": size,
                "_sort": sort,
            }

            json_data = self.request("share/sharepage/detail", "get", params=params)
            is_owner = json_data["data"]["is_owner"]
            _total = json_data["metadata"]["_total"]
            if _total < 1:
                return is_owner, file_list

            _size = json_data["metadata"]["_size"]  # 每页限制数量
            _count = json_data["metadata"]["_count"]  # 当前页数量

            _list = json_data["data"]["list"]

            for file in _list:
                file_list.append(
                    {
                        "fid": file["fid"],
                        "file_name": file["file_name"],
                        "file_type": file["file_type"],
                        "dir": file["dir"],
                        "pdir_fid": file["pdir_fid"],
                        "include_items": file["include_items"]
                        if "include_items" in file
                        else "",
                        "share_fid_token": file["share_fid_token"],
                        "status": file["status"],
                    }
                )
            if _total <= _size or _count < _size:
                return is_owner, file_list

    def get_user_info(self) -> str:
        params = {
            "fr": "pc",
            "platform": "pc",
        }
        return requests.get(
            "https://pan.quark.cn/account/info", params=params, headers=self.headers
        ).json()

    def create_dir(self, pdir_name="新建文件夹", pdir_fid="") -> None:
        json_data = {
            "pdir_fid": pdir_fid,
            "file_name": pdir_name,
            "dir_path": "",
            "dir_init_lock": False,
        }
        return self.request("file", "post", data=json_data)

    def save_shared(
        self,
        share_url: str,
        folder_id: Union[str, None] = None,
    ) -> None:
        logger.info(f"文件分享链接：{share_url}")
        pwd_id = self.get_pwd_id(share_url)
        stoken = self.get_stoken(pwd_id)
        if not stoken:
            return
        is_owner, data_list = self.get_detail(pwd_id, stoken)
        files_count = 0
        folders_count = 0
        files_list: List[str] = []
        folders_list: List[str] = []
        files_id_list = []

        if data_list:
            total_files_count = len(data_list)
            for data in data_list:
                if data["dir"]:
                    folders_count += 1
                    folders_list.append(data["file_name"])
                else:
                    files_count += 1
                    files_list.append(data["file_name"])
                    files_id_list.append((data["fid"], data["file_name"]))

            logger.info(
                f"转存总数：{total_files_count}，文件数：{files_count}，文件夹数：{folders_count} | 支持嵌套"
            )
            logger.info(f"文件转存列表：{files_list}")
            logger.info(f"文件夹转存列表：{folders_list}")

            fid_list = [i["fid"] for i in data_list]
            share_fid_token_list = [i["share_fid_token"] for i in data_list]

            if not folder_id:
                logger.info(
                    "保存目录ID不合法，请重新获取，如果无法获取，请输入0作为文件夹ID"
                )
                return

            if is_owner == 1:
                logger.info("网盘中已经存在该文件，无需再次转存")
                return
            task_id = self.get_share_save_task_id(
                pwd_id, stoken, fid_list, share_fid_token_list, to_pdir_fid=folder_id
            )
            self.submit_task(task_id)

    def get_file_download_url(self, fid: str) -> None:
        data = {"fids": [fid]}
        json_data = self.request("file/download", "post", data=data)
        data_list = json_data.get("data", None)

        if json_data["status"] != 200:
            logger.info(
                f"文件下载地址列表获取失败, {json_data['message']}", error_msg=True
            )
            return
        elif data_list:
            logger.info("文件下载地址列表获取成功")
        return data_list[0]["download_url"]

    def get_share_save_task_id(
        self,
        pwd_id: str,
        stoken: str,
        first_ids: List[str],
        share_fid_tokens: List[str],
        to_pdir_fid: str = "0",
    ) -> str:
        data = {
            "fid_list": first_ids,
            "fid_token_list": share_fid_tokens,
            "to_pdir_fid": to_pdir_fid,
            "pwd_id": pwd_id,
            "stoken": stoken,
            "pdir_fid": "0",
            "scene": "link",
        }

        response = self.request("share/sharepage/save", "post", data=data)
        json_data = response.json()
        task_id = json_data["data"]["task_id"]
        logger.info(f"获取任务ID：{task_id}")
        return task_id

    def submit_task(
        self, task_id: str, retry: int = 50
    ) -> Union[bool, Dict[str, Union[str, Dict[str, Union[int, str]]]]]:
        for i in range(retry):
            # 随机暂停100-50毫秒
            time.sleep(random.randint(500, 1000) / 1000)
            logger.info(f"第{i + 1}次提交任务")
            params = {"task_id": task_id, "retry_index": i}
            json_data = self.request("task", "get", headers=self.headers, params=params)

            if json_data["message"] != "ok":
                if (
                    json_data["code"] == 32003
                    and "capacity limit" in json_data["message"]
                ):
                    logger.info(
                        "转存失败，网盘容量不足！请注意当前已成功保存的个数，避免重复保存",
                    )
                elif json_data["code"] == 41013:
                    logger.info(
                        f"网盘文件夹不存在，请重新运行按3切换保存目录后重试！",
                    )
                else:
                    logger.info(
                        f"错误信息：{json_data['message']}",
                    )
                continue

            if json_data["data"]["status"] != 2:
                continue

            if json_data["data"]["task_title"] == "分享-转存":
                logger.info(f"结束任务ID：{task_id}")
                logger.info(
                    f"文件保存位置：{deep_get(json_data, 'data', 'save_as', 'to_pdir_name') or '根目录'} 文件夹"
                )
            return json_data

    def get_share_task_id(
        self,
        fid: str,
        file_name: str,
        url_type: int = 1,
        expired_type: int = 2,
        password: str = "",
    ) -> str:
        json_data = {
            "fid_list": [fid],
            "title": file_name,
            "url_type": url_type,
            "expired_type": expired_type,
        }
        if url_type == 2:
            json_data["passcode"] = password or generate_random_code()
        json_data = self.request("share", "post", json=json_data)
        return json_data["data"]["task_id"]

    def get_share_id(self, task_id: str) -> str:
        params = {
            "task_id": task_id,
            "retry_index": "0",
        }
        json_data = self.request("task", "get", params=params)
        return json_data["data"]["share_id"]

    def submit_share(self, share_id: str) -> None:
        json_data = {
            "share_id": share_id,
        }
        json_data = self.request(
            "share/password",
            "post",
            data=json_data,
        )
        share_url = json_data["data"]["share_url"]
        if "passcode" in json_data["data"]:
            share_url = share_url + f"?pwd={json_data['data']['passcode']}"
        return share_url

    def share(
        self,
        share_url: str,
        folder_id: Union[str, None] = None,
        url_type: int = 1,
        expired_type: int = 2,
        password: str = "",
    ) -> None:
        first_dir = ""
        second_dir = ""
        try:
            logger.info(f"文件夹网页地址：{share_url}")
            pwd_id = share_url.rsplit("/", maxsplit=1)[1].split("-")[0]

            first_page = 1
            n = 0
            error = 0
            os.makedirs("share", exist_ok=True)

            while True:
                json_data = self.get_file_list(
                    pwd_id, page=first_page, size=50, fetch_total=True
                )
                for i1 in json_data["data"]["list"]:
                    if not i1["dir"]:
                        continue

                    first_dir = i1["file_name"]
                    second_page = 1
                    while True:
                        logger.info(
                            f"正在获取{first_dir}第{first_page}页，二级目录第{second_page}页，目前共分享{n}文件"
                        )
                        json_data2 = self.get_file_list(
                            i1["fid"],
                            page=second_page,
                            size=50,
                            fetch_total=True,
                        )
                        for i2 in json_data2["data"]["list"]:
                            if not i2["dir"]:
                                continue

                            n += 1
                            share_success = False

                            fid = ""
                            for i in range(3):
                                try:
                                    second_dir = i2["file_name"]
                                    logger.info(
                                        f"{n}.开始分享 {first_dir}/{second_dir} 文件夹"
                                    )
                                    random_time = random.choice([0.5, 1, 1.5, 2])
                                    time.sleep(random_time)
                                    # print('获取到文件夹ID：', i2['fid'])
                                    fid = i2["fid"]
                                    task_id = self.get_share_task_id(
                                        fid,
                                        second_dir,
                                        url_type=url_type,
                                        expired_type=expired_type,
                                        password=password,
                                    )
                                    share_id = self.get_share_id(task_id)
                                    share_url = self.submit_share(share_id)
                                    logger.info(
                                        f"{n} | {first_dir} | {second_dir} | {share_url}"
                                    )
                                    logger.info(
                                        f"{n}.分享成功 {first_dir}/{second_dir} 文件夹"
                                    )
                                    share_success = True
                                    break

                                except Exception as e:
                                    share_error_msg = e
                                    error += 1

                                if not share_success:
                                    logger.error("分享失败：", share_error_msg)
                                    logger.error(
                                        f"{error}.{first_dir}/{second_dir} 文件夹"
                                    )
                                    logger.error(
                                        f"{n} | {first_dir} | {second_dir} | {fid}"
                                    )

                        second_total = json_data2["metadata"]["_total"]
                        second_size = json_data2["metadata"]["_size"]
                        second_page = json_data2["metadata"]["_page"]
                        if second_size * second_page >= second_total:
                            break
                        second_page += 1

                second_total = json_data["metadata"]["_total"]
                second_size = json_data["metadata"]["_size"]
                second_page = json_data["metadata"]["_page"]
                if second_size * second_page >= second_total:
                    break
                first_page += 1
            logger.info(f"总共分享了 {n} 个文件夹")

        except Exception as e:
            print("分享失败：", e)
            logger.error(f"{first_dir}/{second_dir} 文件夹")

    def share_retry(
        self,
        retry_url: str,
        url_type: int = 1,
        expired_type: int = 2,
        password: str = "",
    ):
        data_list = retry_url.split("\n")

        error = 0
        error_data = []
        for n, i1 in enumerate(data_list):
            data = i1.split(" | ")
            if data and len(data) == 4:
                first_dir = data[-3]
                second_dir = data[-2]
                fid = data[-1]
                share_success = False
                for i in range(3):
                    try:
                        task_id = self.get_share_task_id(
                            fid,
                            second_dir,
                            url_type=url_type,
                            expired_type=expired_type,
                            password=password,
                        )
                        logger.debug("获取到任务ID：", task_id)
                        share_id = self.get_share_id(task_id)
                        logger.debug("获取到分享ID：", share_id)
                        share_url = self.submit_share(share_id)
                        logger.info(f"{n} | {first_dir} | {second_dir} | {share_url}")
                        logger.info(f"{n}.分享成功 {first_dir}/{second_dir} 文件夹")
                        share_success = True
                        break
                    except Exception as e:
                        logger.error("分享失败：", e)
                        error += 1

                if not share_success:
                    error_data.append(i1)
        error_content = "\n".join(error_data)
        logger.error(error_content)

    def search_file(
        self, file_name, page=1, size=50, sort="file_type:desc,updated_at:desc"
    ):
        logger.info("正在从网盘搜索文件🔍")
        params = {
            "q": file_name,
            "_page": page,
            "_size": size,
            "_sort": sort,
            "_fetch_total": 1,
            "_is_hl": "1",
        }
        return self.request("file/search", params=params)

    def get_file_list(
        self,
        pdir_fid="0",
        page=1,
        size=100,
        fetch_total=False,
        sort="file_type:asc,file_name:asc",
    ) -> Dict[str, Any]:
        params = {
            "pdir_fid": pdir_fid,
            "_page": page,
            "_size": size,
            "_fetch_total": fetch_total,
            "_fetch_sub_dirs": "1",
            "_sort": sort,
        }

        return self.request("file/sort", "get", params=params)

    def del_file(self, file_id):
        logger.debug("正在删除文件")
        data = {"action_type": 2, "filelist": [file_id], "exclude_fids": []}
        return self.request("file/delete", "post", data=data)

    def store(self, url: str):
        pwd_id = get_id_from_url(url)
        stoken = self.get_stoken(pwd_id)
        detail = self.get_detail(pwd_id, stoken)[1][0]
        file_name = detail.get("title")

        first_id, share_fid_token, file_type = (
            detail.get("fid"),
            detail.get("share_fid_token"),
            detail.get("file_type"),
        )
        task = self.save_task_id(pwd_id, stoken, first_id, share_fid_token)
        data = self.task(task)
        file_id = data.get("data").get("save_as").get("save_as_top_fids")[0]
        share_task_id = self.share_task_id(file_id, file_name)
        share_id = self.task(share_task_id).get("data").get("share_id")
        share_link = self.get_share_link(share_id)
        logger.info(file_id, file_name, file_type, share_link)

    def save_task_id(self, pwd_id, stoken, first_id, share_fid_token, to_pdir_fid=0):
        logger.info("获取保存文件的TASKID")

        data = {
            "fid_list": [first_id],
            "fid_token_list": [share_fid_token],
            "to_pdir_fid": to_pdir_fid,
            "pwd_id": pwd_id,
            "stoken": stoken,
            "pdir_fid": "0",
            "scene": "link",
        }
        response = self.request("share/sharepage/save", "POST", data=data)
        logger.info(response.json())
        task_id = response.json().get("data").get("task_id")
        return task_id

    def task(self, task_id, trice=10):
        """根据task_id进行任务"""
        logger.info("根据TASKID执行任务")
        trys = 0
        for i in range(trice):
            url = f"task"
            trys += 1
            data = {"task_id": task_id, "retry_index": "range"}
            response = self.request(url, "get", headers=self.headers, data=data)
            logger.info(response)
            if response.get("data").get("status"):
                return response
        return False

    def share_task_id(self, file_id, file_name):
        """创建分享任务ID"""
        data = {
            "fid_list": [file_id],
            "title": file_name,
            "url_type": 1,
            "expired_type": 1,
        }
        response = self.request("share", "POST", data=data)
        return response.get("data").get("task_id")

    def get_share_link(self, share_id):
        url = "https://drive-pc.quark.cn/1/clouddrive/share/password?pr=ucpro&fr=pc&uc_param_str="
        data = {"share_id": share_id}
        response = requests.post(url=url, json=data, headers=self.headers)
        return response.json().get("data").get("share_url")
