from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        print(" INSIDE USER APPS")
        import users.signals

    # def ready(self):
    #     print(" INSIDE USER APPS")
    #     # import users.signals
    #     post_save.connect(save_profile, sender=User)
    #     post_save.connect(create_profile, sender=User)
