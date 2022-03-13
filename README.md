# SHIP ICON GENERATOR
- タク作るときの船のアイコンを生成するやつ

![VOIDHOGE.png](VOIDHOGE.png)

## INSTALLATION
- Pythonの画像編集ライブラリのPillowが必要
  - `pip3 install Pillow`
- 船の名前用のフォントとして、Roboto-Mediumを使っている。
  - システムフォントにない場合はインストールするか、別のフォントをmain.pyの5行目で指定する必要がある。

## USAGE
- `./main.py (CV|BB|CA|CL|DD|cv|bb|ca|cl|dd) (enemy|ally) <name> <filename>`
- 名前に空白を含む場合は、"DES MOINES"のようにダブルクウォートで囲むと吉。
- T10の艦名リスト((cv|bb|ca|dd)_list.txt)が付属しているので、それを使って`./generate`すると良い感じに生成してくれる。(生成済み)
  - リストを編集して自由に船を増やせる。
  - その際全て再生成されるので注意
- allships/に0.10.10の全艦リストを追加した。
  - これを得るためのjsonviwerのクエリをallships/query.txtに書いた。

## LICENSE
- 艦の名前及びID、アイコン(文字部分を除く記号)は、WGの著作物である。よって、以下のガイドラインに基づいてこのリポジトリを公開する。
  - 日本語: https://worldofwarships.asia/ja/news/general-news/content-creator-guidelines/
  - English: https://worldofwarships.asia/en/news/general-news/content-creator-guidelines/
- このプログラムなどを頒布、改変した上で頒布する場合、上のガイドラインに適合する必要がある。
- 私(IGN:voidhoge, Github:void-hoge, Twitter:@voidhoge, Discord: void-hoge#5115)はこのリポジトリに含まれるデータ、プログラム、及びプログラムによって生成されたデータに対してなんの責任も負わない。
- 一部にテスト艦の名前を含むが、これは全てdevelopment blogの内容による。テスト中に名前が変更されることがある。また、一時的なテストのためのテスト艦で、今後実装されないものも含まれる。(Brennus, Lapplandなど)
