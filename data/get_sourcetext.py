import pandas as pd

def extract_source_text(input_file, output_file):
    """
    从输入的 .tsv 文件中提取源文本，并将其保存到另一个 .tsv 文件中。

    Args:
        input_file (str): 输入的 .tsv 文件路径。
        output_file (str): 输出的 .tsv 文件路径。
    """
    # 读取 .tsv 文件，指定分隔符为 '\t'
    df = pd.read_csv(input_file, sep='\t', header=None, names=["summary", "source"])
    
    # 提取后半部分（源文本）
    source_text = df["source"]
    
    # 将源文本保存到新的 .tsv 文件
    source_text.to_csv(output_file, sep='\t', index=False, header=False)
    print(f"源文本已成功保存到: {output_file}")

if __name__ == "__main__":
    input_tsv = "/home/ubuntu/WorkSpace/WHR/t5-pegasus-chinese-main/t5-pegasus-chinese-main/data/train1.tsv"  # 替换为你的输入 .tsv 文件路径
    output_tsv = "/home/ubuntu/WorkSpace/WHR/t5-pegasus-chinese-main/t5-pegasus-chinese-main/data/sourcetext1.tsv"  # 替换为你的输出 .tsv 文件路径
    extract_source_text(input_tsv, output_tsv)
