# SHIP ICON MAKER
- タク作るときの船のアイコンを生成するやつ

![VOIDHOGE.png](VOIDHOGE.png)

## INSTALLATION
- Pythonの画像編集ライブラリのPillowが必要
  - `pip3 install Pillow`
- 船の名前用のフォントとして、Roboto-Mediumを使っている。
  - システムフォントにない場合はインストールするか、別のフォントをmain.pyの5行目で指定する必要がある。

## USAGE
- `./main.py (CV|BB|CA|CL|DD|cv|bb|ca|cl|dd) (enemy|friend) <name> <filename>`
- 名前に空白を含む場合は、"DES MOINES"のようにダブルクウォートで囲むと吉。
- T10の艦名リスト((cv|bb|ca|dd)_list.txt)が付属しているので、それを使って`./generate`すると良い感じに生成してくれる。(生成済み)
  - リストを編集して自由に船を増やせる。
  - その際全て再生成されるので注意
- allships/に0.10.10の全艦リストを追加した。
  - これを得るためのjsonviwerのクエリをallships/query.txtに書いた。

## LICENSE
- WGに怒られる使い方はやめよう。商用利用とか。
- 私void-hoge(Twitter@voidhoge)は、このプログラム、このリポジトリに含まれる全てのデータ、このプログラムによって生成された全てのデータについて、なんの責任も負わない。
