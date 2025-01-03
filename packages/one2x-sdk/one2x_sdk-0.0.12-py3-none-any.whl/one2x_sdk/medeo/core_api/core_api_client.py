import os
import requests
from requests.exceptions import RequestException

from one2x_sdk.utils.logger import get_default_logger

"""
    os.environ["MEDEO_CORE_API_BASE_URL"] = "https://api.example.com"
    os.environ["MEDEO_SERVICE_AUTH_TOKEN"] = "my-secret-token"
    os.environ["ENV"] = "prod"

    api_client = CoreApiClient()

    response = api_client.request("GET", "v1/users", params={"id": 123})
    print("GET Response:", response)

    response = api_client.request("POST", "v1/users", json={"name": "John", "age": 30})
    print("POST Response:", response)
"""
class CoreApiClient:
    def __init__(self, base_url=None, token=None, enable_requests=None, logger=None):
        self.base_url = base_url or os.getenv(
            "MEDEO_CORE_API_BASE_URL", "http://localhost:3000"
        )
        self.token = token or os.getenv("MEDEO_CORE_API_AUTH_TOKEN", "default-token")
        self.logger = logger
        self.enable_requests = (
            enable_requests
            if enable_requests is not None
            else os.getenv("MEDEO_CORE_API_ENABLE_REQUESTS", "false").lower() in "true"
        )

        self.logger = logger or get_default_logger('CoreApiClient')
        self.session = requests.Session()

    def _build_headers(self):
        headers = {"Content-Type": "application/json", "Cookie": f"medeo-service-auth-token={self.token}"}
        return headers

    """
    发送 HTTP 请求
    :param method: 请求方法 ("GET" 或 "POST")
    :param api_path: API 路径
    :param params: 查询参数 (dict, 可选)
    :param data: 表单数据 (dict, 可选)
    :param json: JSON 数据 (dict, 可选)
    :return: 响应数据 (dict 或 None)
    """
    def request(self, method, api_path, params=None, data=None, json=None):
        if not self.enable_requests:
            self.logger.info(
                f"Skipping request to {api_path} in non-production environment"
            )
            return None

        url = f"{self.base_url}/{api_path.strip('/')}"
        headers = self._build_headers()

        try:
            result = self.session.request(
                method=method.upper(),
                url=url,
                params=params,
                data=data,
                json=json,
                headers=headers,
                timeout=10,
            )
            result.raise_for_status()
            return result.json()

        except Exception as e:
            self.logger.error(f"Unexpected error! result: {result.text}, e:{e}")
            return None