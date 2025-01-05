from django.apps import AppConfig


class FrywebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fryweb'

    def ready(self):
        # 注册信号处理函数
        from . import signals

        # 让python可以import .fry文件
        from .fry.fryloader import install_path_hook
        install_path_hook()
