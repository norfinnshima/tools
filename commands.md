git remote to usb
===

```
cd /Volumes/USB_BUFFALO/git
git init --bare xxxxx.git
```

PW付きZipファイル作成
===

```
zip -e -r 新しく作成するzipフォルダ名.zip sample/ -x "*.DS_Store"
```

ディレクトリ連番で作成
===

```
mkdir day{1..30} && touch day{1..30}/memo.md
```
