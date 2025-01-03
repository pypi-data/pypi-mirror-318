import json
import logging
import time


class RequestDataFormatter(logging.Formatter):
    def format(self, record):
        created_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(record.created))

        data = getattr(record, 'data', {})

        log_record = {
            "timestamp": created_time,
            "level": record.levelname,
            "message": record.getMessage(),
            "client_ip": data.get('client_ip', None),
            "method": data.get('method', None),
            "path": data.get('path', None),
            "status_code": data.get('status_code', None),
            "user_agent": data.get('user_agent', None),
            "headers": data.get('headers', None),
            "body_size": data.get('body_size', None),
            "packet_size": data.get('packet_size', None),
            "body_content": data.get('body_content', None),
        }

        return json.dumps(log_record)