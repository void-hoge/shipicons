# SHIP ICON MAKER
- タク作るときの船のアイコンを生成するやつ

![VOIDHOGE.png](VOIDHOGE.png)

## INSTALLATION
- Pythonの画像編集ライブラリのPillowが必要
  - `pip3 install Pillow`
- 船の名前用のフォントとして、Roboto-Mediumを使っている。
  - システムフォントにない場合はインストールするか、別のフォントをmain.pyの5行目で指定する必要がある。

## USAGE
- `./main.py (CV|BB|CA|CL|DD|cv|bb|ca|cl|dd) (enemy|friend) <name> <directory>`
- ディレクトリ名の末尾は/である必要がある。(ファイル名をdirectory+nameとして保存するため)
  - 忘れるとカレントディレクトリにぶちまける
- T10の艦名リスト((cv|bb|ca|dd)_list.txt)が付属しているので、それを使って`./generate`すると良い感じに生成してくれる。(生成済み)
  - リストを編集して自由に船を増やせる。
  - その際全て再生成されるので注意
