# tools

このリポジトリは、手元作業を補助する小さな変換ツール群の置き場です。
各ツールはディレクトリ単位で分けてあり、実装本体、メモ、確認用サンプルを近い場所にまとめています。

## 目次

### `csv-to-json/`

CSV を JSON に変換するブラウザツールです。

- 実装: `csv-to-json/files/csv-to-json.html`
- メモ: `csv-to-json/README.md`
- 入力サンプル: `csv-to-json/samples/sample.csv`
- 期待結果: `csv-to-json/samples/sample.expected.json`

ブラウザで HTML を開き、CSV を選んでそのまま JSON に変換します。

### `excel-to-html/`

Excel を HTML テーブル断片に変換する Python CLI ツールです。

- 実装: `excel-to-html/files/excel-to-html.py`
- メモ: `excel-to-html/README.md`
- 依存定義: `excel-to-html/requirements.txt`
- 入力サンプル: `excel-to-html/samples/sample.xlsx`
- 期待結果: `excel-to-html/samples/sample.expected.html`
- 生成例: `excel-to-html/samples/output.html`

空セルを上のセルの継続として扱い、`rowspan` 付きの HTML テーブルを出力します。

### `excel-to-html-browser/`

Excel を HTML に変換するブラウザ版です。既存の Python 版とは別実装です。

- 実装: `excel-to-html-browser/files/excel-to-html-browser.html`
- メモ: `excel-to-html-browser/README.md`

`.xlsx` / `.xls` をブラウザで読み込み、シートを選んで HTML に変換します。

### `commands.md`

変換ツールとは別に、よく使うコマンド断片のメモです。

## 使い分け

- すぐ使いたいなら `csv-to-json` と `excel-to-html-browser`
- ローカル処理やバッチ用途なら `excel-to-html`

## 補足

- ブラウザ版はローカルファイルを直接処理します
- `excel-to-html-browser` は Excel 読み込みに CDN 上のライブラリを使うため、ページ読込時にネット接続が必要です
- 公開リポジトリとしては機密情報を含まない構成ですが、ブラウザ版で外部 CDN を避けたい場合はライブラリをローカル同梱に切り替えるとより堅実です
