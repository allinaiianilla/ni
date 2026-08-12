from rich.console import Console
from rich.markdown import Markdown

import os
import json
from openai import OpenAI
from datetime import datetime
from prompt_toolkit import prompt

# 程序目标: 和ai聊天
# 功能实现:
# 1. 具备记忆功能,20条
# 2. ai返回内容展示两种方式:1-普通流式,2-markdown展示 用户可选择
# 3. 通过配置文件选择模型,可新增,可删除


# 实现方案
# 1. 配置文件, 程序启动后先读取配置文件,如果没有,提示用户输入模型信息,
# 配置- 选择配置 /models
# models_list, add, del
def write_message(filename, role, message):
    program_dir = os.path.dirname(os.path.abspath(__file__))
    messages_filepath = os.path.join(program_dir, filename)
    with open(messages_filepath, "a", encoding="utf-8") as f:
        f.write(f"{role}\n")
        f.write(f"{message}\n")

def read_config():
    program_dir = os.path.dirname(os.path.abspath(__file__))
    config_filename = "aichat_config.json"
    config_filepath = os.path.join(program_dir, config_filename)

    if os.path.isfile(config_filepath):
        try:
            with open(config_filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

                if data:
                    return data
        except Exception as e:
            print(f"读取配置文件{config_filepath}报错:{e}")
            return {}
    else:
        return {}

def write_config(config_data):
    program_dir = os.path.dirname(os.path.abspath(__file__))
    config_filename = "aichat_config.json"
    config_filepath = os.path.join(program_dir, config_filename)

    try:
        with open(config_filepath, "w", encoding="utf-8") as f:
            json.dump(config_data, f, ensure_ascii=False, indent=4)

            return True
    except Exception as e:
        print(f"写入配置文件{config_filepath}报错:{e}")
        return False

def add_model(data={}):
    if not data:
        data = {}
        data["models"] = {}
    else:
        if not data.get("models"):
            data["models"] = {}

    while True:
        print("添加大模型api信息:")
        base_url = input("填写大模型base_url:").strip()
        model_name = input("填写大模型名称(id):").strip()
        api_key = input("api_key:").strip()
        if base_url and model_name and api_key:
            data["models"][model_name] = {"base_url":base_url,"model_name":model_name,"api_key":api_key}
            add_flag = input("是否继续添加新模型?y/n:")
            if add_flag.lower().strip() == 'y':
                continue
            else:
                write_config(data)
                break
        else:
            print("模型信息填写有误,请重新输入")
            continue
def del_model(data,model_name):
    try:
        if data.get("models").get(model_name):
            del data["models"][model_name]
    except Exception as e:
        print(f"未找到模型{model_name},删除失败")

def select_models():
    data = read_config()
    try:
        if data.get("models"):
            for i, model_name in enumerate(data.get("models")):
                print(f"{i}:{model_name}")
        else:
            print("未查询到模型数据")
    except Exception as e:
        print("未查询到模型数据")


def inputs_send(message=""):
    lines = []
    if message:
        print(message,end="")
    while True:
        line = input("> ")
        if line == "/send":
            break

        lines.append(line)
    message = "\n".join(lines)

    return message

def inputs(message=""):
    user_input = prompt(message, multiline=True)
    return user_input

def get_client(model_data):
    try:
        client = OpenAI(
            api_key=model_data["api_key"],
            base_url=model_data["base_url"]
        )
        return client
    except Exception as e:
        print(f"连接大模型失败:{e}")
        return None

def get_response(client,model_data,messages):
    response = client.chat.completions.create(
        model = model_data.get("model_name"),
        messages=messages,
        stream=True
    )
    response_text = ""
    for chunk in response:
        if chunk.choices:
            text = chunk.choices[0].delta.content

            if text:
                response_text = response_text + text
                print(text, end="", flush=True)


    print()
    return response_text


def aichat():
    start_time = datetime.now()
    messages_filename = start_time.strftime("chat_%Y%m%d_%H%M%S.txt")
    print("Welcome use aichat!")

    while True:
        config_data = read_config()
        if config_data.get("models"):
            model_name, model_data = next(iter(config_data.get("models",{}).items()))
            break
        else:
            add_model()

    messages = []
    client = get_client(model_data)
    while True:
        try:
            print("user:")
            question_str = inputs().strip()
            if question_str.lower() in ("/q","/quit","/exit"):
                input("任意键关闭窗口...")
                break
        except KeyboardInterrupt:
            input("任意键关闭窗口...")
            break
        except Exception as e:
            input("任意键关闭窗口...")
            break
            
        if question_str.strip():
            question = {"role":"user","content":question_str}
            messages.append(question)
            write_message(messages_filename, "user:", question_str)
        else:
            print("用户消息不能为空")
            continue
        print(f"{model_name}:")
        response_str = get_response(client, model_data, messages[-20:])
        if response_str:
            response = {"role":"assistant","content":response_str}
            messages.append(response)
            write_message(messages_filename, "AI:", response_str)






def main():
    aichat()
    



if __name__ == "__main__":
    main()
