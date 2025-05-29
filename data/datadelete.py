def load_data(filename):
    """加载数据
    单条格式：(摘要, 内容)
    """
    D = []
    with open(filename, encoding='utf-8') as f:
        for line in f.readlines():
            # 删除领域信息
            line = line.rstrip('\n')
            summary, content = line.split('\t')[:2]  # 只保留摘要和内容
            D.append((summary, content))
    return D

def export_data(data, output_filename):
    """将数据导出为TSV文件
    """
    with open(output_filename, 'w', encoding='utf-8') as f:
        for summary, content in data:
            line = summary + '\t' + content + '\n'
            f.write(line)

# 加载数据
filename = 'dev.tsv'  # 修改为你的文件路径
data = load_data(filename)

# 导出处理后的数据为TSV文件
output_filename = 'dev__no-keyword.tsv'  # 设置输出文件名
export_data(data, output_filename)
