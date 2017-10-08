# Chroma Key on kokasai2017

## 空飛ぶじゅうたん

これは空飛ぶ絨毯(じゅうたん)です.

背景は工科大の映像や他の映像に変更可能です。

## 概要

以下は主にクロマキー合成の仕組みについて解説します。

### クロマキー処理とは

> クロマキー処理とは、画像から特定の色(Chroma)領域を除去し、物体を抽出する手法のこと。

> 奈良先端科学技術大学院大学OpenCVプログラミングブック制作チーム, 「OpenCV プログラミングブック第2版 OpenCV 1.1対応」より引用

テレビニュースの天気予報などで天気図とキャスターが合成されるのもこの仕組みを利用しています。

クロマキーでは次の手順で処理を行います。

1. 対象物体を含むビデオ映像と背景映像を読み込み
2. ビデオ映像から背景を表すマスク（切り取り範囲）を作成
3. マスクに基づいて映像から必要な部分をコピー
4. マスクを反転し対象物を抽出
5. 背景映像とビデオ映像を足し合わせ
