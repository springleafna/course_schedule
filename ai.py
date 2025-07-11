from http import HTTPStatus
from os import getenv
from dashscope import Application
from config import APP_ID, DOC_LINK

def call_ai_api(prompt: str) -> dict:
    """
    调用 DashScope AI API 并返回结构化结果
    :param prompt: 用户输入的原始课程信息
    :return: 包含 success 和 result 的字典
    """
    try:
        response = Application.call(
            api_key=getenv('COURSE_SCHEDULE_APIKEY'),
            app_id=APP_ID,
            prompt=prompt
        )

        if response.status_code != HTTPStatus.OK:
            return {
                "success": False,
                "error": {
                    "request_id": response.request_id,
                    "code": response.status_code,
                    "message": response.message,
                    "doc_link": DOC_LINK
                }
            }
        else:
            return {
                "success": True,
                "result": response.output.text
            }

    except Exception as e:
        return {
            "success": False,
            "error": {
                "message": str(e)
            }
        }
