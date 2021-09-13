# Django Girls

## このアプリについて
- pythonを使用したWebアプリケーションフレームワークであるDjangoで作成したブログアプリ

- Django Girlsのチュートリアル　https://tutorial.djangogirls.org/ja/


# Usage（利用方法）

## 仮想環境
1. 作成
    ```
    $ python3 -m venv myvenv
    ```
1. 起動
    ```
    $ source myvenv/bin/activate
    ```
1. 停止
    ```
    $ deactivate
    ```
## Djangoのインストール
1. コマンドを実行するディレクトリに`requirements.txt`ファイルを作成する
    - アプリに必要なパッケージ（ライブラリ）を一括でインストールするため、以下のテキストを追加
    ```
    Django~=2.2.4
    ```
1. パッケージをインストール
    ```
    (myvenv) ~$ python -m pip install --upgrade pip
    ```
    
## Webサーバ
1. 起動
    ```
    (myvenv) ~/djangogirls$ python manage.py runserver
    ```
1. 動作確認
    
    http://127.0.0.1:8000/
    

1. 停止

    CTRL + C    
