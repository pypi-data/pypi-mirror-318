import re
from datetime import datetime
import time
import os
import uiautomation as auto

class TranscriptItem:
    def __init__(self, timestamp, speaker, content):
        self.timestamp = timestamp
        self.speaker = speaker
        self.content = content
    
    def to_string(self):
        return f"[{self.timestamp}] {self.speaker}: {self.content}"

class TranscriptManager:
    def __init__(self):
        self.transcripts = {}
        self.output_dir = os.path.join(os.path.expanduser("~"), ".zoomzoom", "transcripts")
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def add_transcript(self, transcript_item):
        key = f"{transcript_item.timestamp}_{transcript_item.speaker}"
        self.transcripts[key] = transcript_item
    
    def _get_output_path(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return os.path.join(self.output_dir, f"transcript_{timestamp}.txt")
    
    def save_to_file(self):
        if not self.transcripts:
            return
        
        output_path = self._get_output_path()
        
        # 按时间戳排序
        sorted_items = sorted(
            self.transcripts.values(),
            key=lambda x: datetime.strptime(x.timestamp, '%H:%M:%S')
        )
        
        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            for item in sorted_items:
                f.write(f"{item.to_string()}\n")
        
        return output_path

def monitor_transcript(callback):
    """监控Zoom字幕并返回TranscriptManager实例"""
    manager = TranscriptManager()
    
    def monitor_loop():
        try:
            # 查找Zoom会议窗口
            zoom_window = auto.WindowControl(searchDepth=1, ClassName='ZPContentViewWndClass')
            if not zoom_window.Exists():
                raise Exception("找不到Zoom会议窗口")
            
            # 查找字幕区域
            caption_control = zoom_window.GroupControl(AutomationId="closedCaption")
            if not caption_control.Exists():
                raise Exception("找不到字幕区域，请确保已启用实时字幕")
            
            # 正则表达式模式
            pattern = r'\[([\d:]+)\] ([^:]+): (.+)'
            
            # 持续监控字幕更新
            while True:
                try:
                    caption_text = caption_control.Name
                    if caption_text:
                        # 解析字幕文本
                        match = re.match(pattern, caption_text)
                        if match:
                            timestamp, speaker, content = match.groups()
                            # 创建TranscriptItem并添加到管理器
                            item = TranscriptItem(timestamp, speaker, content)
                            manager.add_transcript(item)
                            # 通过回调函数通知更新
                            callback("transcript", item)
                    
                    time.sleep(0.1)  # 短暂休眠以减少CPU使用
                    
                except Exception as e:
                    print(f"监控循环中出错: {e}")
                    time.sleep(1)  # 出错时稍长休眠
                    
        except Exception as e:
            callback("error", str(e))
    
    return manager, monitor_loop