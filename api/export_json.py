
def export_json(data, file_name):
    # 同ディレクトリにdataの結果をjsonファイルとして保存する
    with open(file_name, "w") as f:
        f.write(str(data))
