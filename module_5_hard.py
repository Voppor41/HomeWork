import hashlib


class User:
    """
    Класс пользователя, содержащий ключевые данные(имя, возвраст, пароль) пользователя
    """

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        if isinstance(other, User):
            return self.password == other.password

    def __str__(self):
        return f'User(nickname={self.nickname}, age={self.age})'

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def play(self):
        if self.time_now < self.duration:
            self.time_now += 1
            print(f'Playing {self.title}: {self.time_now}/{self.duration} seconds.')
        else:
            print(f'{self.title} has finished playing.')

    def __str__(self):
        return f'Video(title={self.title}, duration={self.duration})'


class UrTube:

    users = []
    videos = []

    def __init__(self):
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.chek_passwor(password):
                self.current_user = user
                print(f"Вы успешно вошли как {nickname}. Рады видеть вас снова!")
            return f"Ошибка входа, проверьте логин и пароль!"

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print('Nickname already exists.')
            return
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f'Вы вошли и зарегестрировались как {new_user.nickname}.')

    def log_out(self):
        if self.current_user:
            print(f"Вы вышли с аккаунта {self.current_user.nickname}")
            self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f'Добавлено видео: {video.title}.')
            else:
                print(f'Видео {video.title} уже существует.')

    def get_videos(self, keyword):
        found_videos = [video.title for video in self.videos if keyword.lower() in video.title.lower()]
        return found_videos

    def watch_video(self, title):
        if not self.current_user != None:
            print()
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and (not self.current_user or self.current_user.age < 18):
                    print(f'Access denied to {video.title}. This video is for adults only.')
                    return
                print(f'Starting to watch {video.title}.')
                while video.time_now < video.duration:
                    video.play()
                return
        print(f'Video {title} not found.')


if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
