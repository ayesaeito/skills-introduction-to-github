# 导入必要的库
import tkinter as tk
import sympy as sp
from sympy import sqrt, cbrt, pi, E, simplify

# 定义按钮点击事件处理函数，用于向输入框中添加数字或运算符
def button_click(num):
    current = entry.get()
    last_char = current[-1] if current else ''
    
    # 自动添加乘号的逻辑
    need_multiply = False
    if current and num in ['sqrt(', 'cbrt(', 'pi', 'e', '(']:
        if last_char.isdigit() or last_char in [')', 'π', 'e']:
            need_multiply = True
    
    entry.delete(0, tk.END)
    if need_multiply:
        entry.insert(0, current + '*' + str(num))
    else:
        entry.insert(0, current + str(num))

# 定义删除一个字符的函数
def backspace():
    current = entry.get()
    if current:
        entry.delete(len(current) - 1, tk.END)

# 定义全部清除函数
def full_clear():
    entry.delete(0, tk.END)

# 定义计算按钮事件处理函数，使用SymPy进行符号计算
def calculate():
    try:
        expression = entry.get()
        # 替换符号以便SymPy识别
        expression = expression.replace('π', 'pi').replace('^', '**').replace('e', 'E')
        # 将字符串转换为SymPy表达式
        expr = sp.sympify(expression)
        # 简化表达式（包括分母有理化）
        result = simplify(expr)
        # 将结果转换为字符串并替换符号以便显示
        result_str = str(result).replace('sqrt', '√').replace('pi', 'π').replace('E', 'e')
        entry.delete(0, tk.END)
        entry.insert(0, result_str)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "错误")

# 创建主窗口
root = tk.Tk()
root.title("科学计算器")
root.geometry("400x600")  # 设置窗口初始大小

# 创建输入框，设置宽度和字体
entry = tk.Entry(root, width=18, borderwidth=5, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# 定义按钮列表，包含按钮的文本、行和列信息
buttons = [
    # 无理数按钮移动到左侧
    ('√(', 1, 0), ('∛(', 2, 0), ('π', 3, 0), ('e', 4, 0), ('^', 5, 0),
    ('7', 1, 1), ('8', 1, 2), ('9', 1, 3), ('/', 1, 4),
    ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('*', 2, 4),
    ('1', 3, 1), ('2', 3, 2), ('3', 3, 3), ('-', 3, 4),
    ('0', 4, 1), ('.', 4, 2), ('=', 4, 3), ('+', 4, 4),
    ('(', 5, 1), (')', 5, 2), ('C', 5, 3), ('删除', 5, 4)
]

# 定义按钮的字体
button_font = ('Arial', 14)

# 遍历按钮列表，创建并放置按钮
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=calculate, font=button_font)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=full_clear, font=button_font)
    elif text == '删除':
        btn = tk.Button(root, text=text, padx=20, pady=20, command=backspace, font=button_font)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: button_click(t), font=button_font)
    btn.grid(row=row, column=col, sticky="nsew")

# 设置网格权重，使按钮可以随窗口大小调整
for i in range(8):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

# 运行主循环
root.mainloop()
