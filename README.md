# portfolio_docker_nextjs_django_nginx

## .envファイル
.envファイルはgitに上げないようにしているので、
.env.exampleを.envにリネームして利用する必要があります。
また、SECRET＿KEYは以下のコマンドで各自で生成してください。

    $ python3 manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())


