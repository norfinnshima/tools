# excel-to-html

@ [excel-to-html.py](./files/excel-to-html.py)

Excel を HTML テーブル断片へ変換する CLI スクリプトです。

- `argparse` で入力ファイル・出力先・シート指定を受け取れるように変更
- HTML エスケープを追加し、改行は `<br>` に変換
- 縦に結合されたセル相当のデータを `rowspan` で再現
- 未使用コードや壊れた HTML (`</body>`) を除去

使い方:

```bash
pip install -r excel-to-html/requirements.txt
python excel-to-html/files/excel-to-html.py test.xlsx -o table.html
python excel-to-html/files/excel-to-html.py test.xlsx --sheet Sheet1
```
