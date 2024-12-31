import datetime
import re

from adbutils import AdbDevice

from AndroidTraceTool.core.micro_server import TraceSocket
from AndroidTraceTool.utils._print_util import print_error


def mark_trace(operation_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if "device" in kwargs:
                device = kwargs["device"]
            else:
                for kwarg in kwargs:
                    value = kwargs[kwarg]
                    if isinstance(value, AdbDevice):
                        device = kwargs["device"]
                        break
                else:
                    for prop_value in args[0].__dict__.values():
                        if isinstance(prop_value, AdbDevice):
                            device = prop_value
                            break
                    else:
                        print_error("方法中未定义device参数，无法通过注解标注trace")
                        return func(*args, **kwargs)
            if isinstance(device, AdbDevice):
                device = device.serial
            if device not in TraceSocket.device_socket_dict.keys():
                print_error("未提前注册socket，无法通过注解标注trace")
                return func(*args, **kwargs)
            socket = TraceSocket.device_socket_dict[device]
            new_operation_name = operation_name
            if "{" in operation_name and "}" in operation_name:
                pattern = r'\{([^}]*)\}'
                matches = re.findall(pattern, operation_name)
                for match in matches:
                    if match in kwargs:
                        new_operation_name = new_operation_name.replace(f"{{{match}}}", str(kwargs[match]))
            cookie = datetime.datetime.now().strftime("%H%M%S")
            socket._send_message(f"start_{new_operation_name}_{cookie}")
            # 执行被装饰的函数
            result = func(*args, **kwargs)
            socket._send_message(f"end_{new_operation_name}_{cookie}")
            return result

        return wrapper

    return decorator
