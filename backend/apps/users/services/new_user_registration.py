from django.contrib.auth import get_user_model


class NewUserRegistration:
    def create_user(self, requset_post):
        user = get_user_model().objects.create_user(
            username=requset_post.get("email").lower(),
            email=requset_post.get("email").lower(),
        )
        user.phone = requset_post.get("phone")
        user.first_name = requset_post.get("first_name")
        user.last_name = requset_post.get("last_name")
        user.second_name = requset_post.get("second_name")
        user.is_active = True
        user.set_password(requset_post.get("password1"))
        user.save()
        return user

    def validate(self, requset_post):
        errors = []
        if (
            get_user_model()
            .objects.filter(username=requset_post.get("email").lower())
            .count()
            > 0
        ):
            errors.append("Пользователь с таким email уже зарегестрирован")
        if str(requset_post.get("password1")) != str(
            requset_post.get("password2")
        ):
            errors.append("Пароли не совпадают")
        return errors

    def execute(self, requset_post):
        errors = self.validate(requset_post)
        if len(errors) > 0:
            return {"errors": errors, "user": None}
        else:
            return {"errors": None, "user": self.create_user(requset_post)}
