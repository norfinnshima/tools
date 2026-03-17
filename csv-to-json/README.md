# csv-to-json

@ [csv-to-json.html](./files/csv-to-json.html)

ブラウザだけで完結する CSV → JSON 変換ツールです。文字コードの既定値は `UTF-8` にしています。主な改善点:

- `TextDecoder` を使って `UTF-8` / `Shift_JIS` を切り替え可能
- ダブルクォートを含む CSV を扱えるパーサに差し替え
- 列選択 UI を整理し、全選択・全解除・ダウンロードを追加
- グローバル変数中心の実装を状態管理付きの構成へ整理

使い方:

1. `files/csv-to-json.html` をブラウザで開く
2. CSV ファイルと文字コードを選ぶ
3. 出力対象の列を選択して `JSON に変換`
4. `JSON を保存` でダウンロード
