# man_woman_cnn_part1
## 記事
*スクレイピング：https://cpptake.com/archives/268 
*モデル作成　　：https://cpptake.com/archives/303

## 概要
男女識別AIのスクレイピング、前処理、モデル作成までのコードを残します。

### 1.スクレイピング
*本レポジトリのscraping.py FlickrAPIを利用して、男女のデータをスクレピングで取得するスクリプト。 利用にはFlickrAPIの登録が必要。

今回の取り組みでは、様々な男女のデータをスクレイピングで取得し、CNNモデル作成のデータとして利用した。

Flickr：https://www.flickr.com/groups/japanese/

### 2.顔検知
*本リポジトリのface_detection.ipynb,face_detection.py 取得した男女画像の顔部分のみを切り取る処理のスクリプト。

opencvのhaarcascade_frontalface_alt2.xmlを利用してます。 opencvリポジトリ:https://github.com/opencv/opencv/tree/master/data/haarcascades

### 3.モデル作成
*本リポジトリのface_cnn.ipynb 男女の顔画像の識別モデルを作成するスクリプト。（Jupyternotebook）

Kerasを利用した男女識別モデルを作成。 Dropout,L2正則化などを利用して過学習を防ぐようなモデルを作成。 学習済みモデルは、「model_weight」フォルダに格納。

## 参考文献
Nishpy Notes：https://nishipy.com/archives/662
