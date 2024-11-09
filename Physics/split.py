import os
import re

def split_markdown(filename):
    # 打开并读取文件内容
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 使用正则表达式找到所有二级标题和内容
    sections = re.split(r'(?m)^## (lecture \d{2}: .+)', content)

    # 确保有内容和标题配对
    if len(sections) < 2:
        print("文件中没有找到符合格式的二级标题")
        return
    
    # 依次遍历标题和内容，写入新的 Markdown 文件
    for i in range(1, len(sections), 2):
        # 当前的标题和内容
        full_title = sections[i].strip()  # 完整标题，保留在文件内容中
        body = sections[i + 1].strip()

        # 提取 lecture 编号（例如 "lecture 03"）
        match = re.match(r'lecture (\d{2})', full_title)
        if match:
            lecture_number = match.group(1)  # 提取到的编号，例如 "03"
            output_filename = f"lecture{lecture_number}.md"

            # 写入文件，并保留原标题
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(f"## {full_title}\n\n{body}\n")
            
            print(f"已创建文件: {output_filename}")
        else:
            print(f"未找到符合格式的 lecture 编号：{full_title}")

# 使用脚本
split_markdown("physics2.md")