import os
import re
from docx import Document

def clean_text(text):
    """清理文本，去掉空格和特殊字符"""
    cleaned_text = re.sub(r'\s+', ' ', text)  # 去除多余空格和换行符
    cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text)  # 去除特殊字符
    return cleaned_text

def process_dtxt(input_file, output_file):
    """从指定的.dtxt文件中读取文本，清理文本后写入到新的.docx文档中"""
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print("Error: 输入文件不存在")
        return
    
    # 读取原始文本
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # 清理文本
    cleaned_text = clean_text(text)
    
    # 创建新的docx文档并写入清理后的文本
    new_doc = Document()
    new_doc.add_paragraph(cleaned_text)
    new_doc.save(output_file)

    print("处理完成，输出文件路径：", output_file)

if __name__ == "__main__":
    # 输入和输出文件路径
    input_file = "wben5.txt"  # 替换为您的输入文件路径
    output_file = "liuxinshiyanwenbenshuju.docx"  # 替换为您的输出文件路径

    # 处理dtxt文档
    process_dtxt(input_file, output_file)

