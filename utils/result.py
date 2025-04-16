import json
from dataclasses import dataclass

# 这是统一包装返回类，方便前端处理数据
@dataclass
class Result:
    status: str
    code: int
    message: str
    data: any = None

    @classmethod
    def ok(cls, msg: any = 'success', data: any = None): return cls('success', 200, msg, data).to_json()

    @classmethod
    def not_json(cls): return cls('warning', 401, 'not json').to_json()

    @classmethod
    def empty_str(cls, msg: any = 'empty string'): return cls('Not found', 404, msg).to_json()

    @classmethod
    def client_err(cls, msg: any = 'other error'): return cls('error', 400, msg).to_json()

    @classmethod
    def server_err(cls, msg: any = 'server error'): return cls('error', 500, msg).to_json()

    @classmethod
    def unknown_err(cls): return cls('error', 505, 'unknown error').to_json()

    def to_dict(self):  # 新增返回字典的方法
        return {"status": self.status, "code": self.code, "message": self.message, "data": self.data}

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)