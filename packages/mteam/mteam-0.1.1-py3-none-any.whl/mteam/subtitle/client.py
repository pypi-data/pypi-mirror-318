from typing import List, Optional
from ..models import Result
from .models import (
    SubtitleUploadForm,
    SubtitleSearch,
    SubtitleInfo,
    SubtitleLanguage
)

class SubtitleClient:
    """字幕相关 API 客户端"""
    
    def __init__(self, base_client):
        self._client = base_client
    
    def upload(self, form: SubtitleUploadForm, file_path: str) -> Result:
        """
        上传字幕
        
        Args:
            form: 字幕上传表单
            file_path: 字幕文件路径
        """
        files = {'file': open(file_path, 'rb')}
        return Result(**self._client._make_request(
            "POST",
            "/subtitle/upload",
            data=form.model_dump(),
            files=files
        ))
    
    def search(self, params: SubtitleSearch) -> Result[List[SubtitleInfo]]:
        """
        搜索字幕
        
        Args:
            params: 搜索参数
        """
        return Result[List[SubtitleInfo]](**self._client._make_request(
            "POST",
            "/subtitle/search",
            json=params.model_dump()
        ))
    
    def download(self, subtitle_id: int) -> Result[bytes]:
        """
        下载字幕
        
        Args:
            subtitle_id: 字幕ID
        """
        return Result[bytes](**self._client._make_request(
            "GET",
            f"/subtitle/download/{subtitle_id}"
        ))
    
    def delete(self, subtitle_id: int) -> Result:
        """
        删除字幕
        
        Args:
            subtitle_id: 字幕ID
        """
        return Result(**self._client._make_request(
            "POST",
            f"/subtitle/delete/{subtitle_id}"
        ))
    
    def get_languages(self) -> Result[List[SubtitleLanguage]]:
        """获取支持的字幕语言列表"""
        return Result[List[SubtitleLanguage]](**self._client._make_request(
            "GET",
            "/subtitle/languages"
        ))
    
    def generate_download_link(self, subtitle_id: int) -> Result[str]:
        """
        生成字幕下载链接
        
        Args:
            subtitle_id: 字幕ID
        
        Returns:
            包含下载链接的结果
        """
        return Result[str](**self._client._make_request(
            "POST",
            "/subtitle/genlink",
            params={"id": subtitle_id}
        ))
    
    def get_subtitle_list(self, torrent_id: int) -> Result[List[SubtitleInfo]]:
        """
        获取种子的字幕列表
        
        Args:
            torrent_id: 种子ID
        
        Returns:
            包含字幕列表的结果
        """
        response = self._client._make_request(
            "POST",
            "/subtitle/list",
            params={"id": torrent_id}
        )
        
        # 确保响应中的数据被正确转换为 SubtitleInfo 对象列表
        if response.get("data"):
            response["data"] = [SubtitleInfo(**item) for item in response["data"]]
        
        return Result[List[SubtitleInfo]](**response) 