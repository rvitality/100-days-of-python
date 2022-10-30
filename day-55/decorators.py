class User:
    def __init__(self, name):
        self.name = name
        self.is_authenticated = False
        self.login()

    def login(self):
        self.is_authenticated = True


new_user = User("John")


def is_authenticated_decorator(fn):
    def wrapper(*args, **kwargs):
        user = args[0]
        if not user.is_authenticated:
            print("Please log in first.")
            return

        fn(user)

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


create_blog_post(new_user)
