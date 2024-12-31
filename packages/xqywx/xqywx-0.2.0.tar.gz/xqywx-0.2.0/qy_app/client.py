import os
import requests
from typing import Optional, Union, Dict

class QyAppClient:
    """企业微信应用客户端"""
    
    def __init__(self, base_url: str = ""):
        self.base_url = base_url.rstrip('/')
        
    def send_text(
        self,
        content: str,
        touser: str = "XuRui",
        agentid: int = 1000005
    ) -> Dict:
        """
        发送文本消息
        
        Args:
            content: 消息内容
            touser: 接收者用户名
            agentid: 应用ID
            
        Returns:
            Dict: 接口返回结果
        """
        url = f"{self.base_url}/send_message"
        data = {
            "content": content,
            "touser": touser,
            "agentid": agentid
        }
        
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
        
    def send_image(
        self,
        image_path: str,
        touser: str = "XuRui",
        agentid: int = 1000005
    ) -> Dict:
        """
        上传并发送图片消息
        
        Args:
            image_path: 图片文件路径
            touser: 接收者用户名
            agentid: 应用ID
            
        Returns:
            Dict: 接口返回结果
        """
        # 检查文件是否存在
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"图片文件不存在: {image_path}")
            
        # 上传图片
        upload_url = f"{self.base_url}/upload_image"
        with open(image_path, 'rb') as f:
            files = {'file': f}
            upload_response = requests.post(upload_url, files=files)
            upload_response.raise_for_status()
            upload_result = upload_response.json()
            
            if upload_result['status'] != 'success':
                raise Exception(f"上传图片失败: {upload_result}")
                
            media_id = upload_result['media_id']
        
        # 发送图片消息
        send_url = f"{self.base_url}/send_image"
        data = {
            "media_id": media_id,
            "touser": touser,
            "agentid": agentid
        }
        
        response = requests.post(send_url, json=data)
        response.raise_for_status()
        return response.json() 