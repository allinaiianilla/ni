from prompt_toolkit import prompt

def get_multiline_input(prompt_text: str = "请输入内容（按 Alt+Enter 或 Esc+Enter 结束）:\n") -> str:
    """
    获取用户输入的多行文本，并返回输入内容。
    """
    # 使用 multiline=True 开启多行模式
    user_input = prompt(prompt_text, multiline=True)
    return user_input

# 示例调用
if __name__ == "__main__":
    result = get_multiline_input()
    print("\n--- 你输入的内容是 ---")
    print(result)

