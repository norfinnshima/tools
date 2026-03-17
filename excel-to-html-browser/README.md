# excel-to-html-browser

@ [excel-to-html-browser.html](./files/excel-to-html-browser.html)

ブラウザだけで完結する Excel → HTML 変換ツールです。

- `.xlsx` / `.xls` をブラウザで選択して変換
- シートを選んで HTML テーブル断片を生成
- 空セルの連続を `rowspan` として扱い、既存 Python 版の意図に寄せた出力を生成
- 画面上でプレビューし、そのまま `.html` として保存可能

注意:

- Excel 読み込みには CDN 上の `SheetJS` を利用しているため、初回読み込み時にネットワーク接続が必要です
- 変換ロジックは `excel-to-html/files/excel-to-html.py` と同じく、空セルを上のセルの継続として扱います

使い方:

1. `files/excel-to-html-browser.html` をブラウザで開く
2. Excel ファイルを選択する
3. 必要ならシートを切り替える
4. `HTML に変換` を押す
5. プレビュー確認後に `HTML を保存` を押す
