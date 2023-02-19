from .base import *

# pip install django-environで事前にインストールしておく必要がある
import environ
# もし .env.dev ファイルが存在したら設定を読み込む。（ただし同じ変数の値は上書きされない。）
# env.read_env(os.path.join(BASE_DIR, '.env.dev'))

# .envファイルを読み込み
env = environ.Env()

# 本番環境用
# env.read_env(Path.joinpath(BASE_DIR, 'secrets/.env.production'))

# 開発環境用
env.read_env(Path.joinpath(BASE_DIR, 'secrets/.env.develop'))

#シークレットキーはGitに絶対に上げない
SECRET_KEY = env('SECRET_KEY')
DEBUG = env.bool('DEBUG')
# ALLOWED_HOSTS = ['localhost',]
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
# CSRF_TRUSTED_ORIGINS = ['https://特定のドメイン'] django4.0からこれをしないと管理画面に入るときにCSRFのエラーになる
CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS')

DATABASES = {
    'default': env.db(),
}

##################
# Email settings #
##################
# 開発時は実際にメールを送信せず、コンソールに件名や本文、Fromアドレス、Toアドレスなどを出力することができる。
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGGING = {
    # バージョンは「1」固定
    'version': 1,
    # 既存のログ設定を無効化しない
    'disable_existing_loggers': False,
    # ログフォーマット
    'formatters': {
        # 開発用 
        'develop': {
            'format':   '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d '
                        '%(message)s'
        },
    },
    # ハンドラ
    'handlers': {
        # コンソール出力用のハンドラ
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'develop',
        },
    },
    # ロガー
    'loggers': {
        # 自作アプリケーション全般のログを拾うロガー
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Django本体が出すログ全般を拾うロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # 発行されるSQL文を出力するための設定。パフォーマンスの観点から「DEBUG=True」の時にしか出力されない。
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}