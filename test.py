#ライブラリをインポート
import pandas as pd

print("pandasの準備が完了しました！ バージョン:", pd.__version__)

#データの読み込み
data = pd.read_csv("Database/Benesse/1571.csv")
print(data.head())

#データ型を見てみる
data.info()

# 1. 特定の列（例：w1回答フラグ）の回答人数をカウントする（単純集計）
print("\n▼ w1回答フラグの集計結果")
print(data['w1回答フラグ'].value_counts())

# 2. 欠損値（NaN）も含めてカウントしたい場合
print(data['w1回答フラグ'].value_counts(dropna=False))