def to_float(s):
    """文字列をfloatに変換する関数"""
    try:
        return float(s)
    except ValueError:
        return "変換できませんでした"

print(to_float("100"))

