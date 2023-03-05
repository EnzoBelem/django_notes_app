from random import randint

from faker import Faker

fake = Faker('pt_BR')


def rand_ratio():
    return randint(800, 849), randint(473, 573)


def make_note():
    return {
        'created_at': fake.date_time(),
        'title': fake.sentence(nb_words=6),
        'description': fake.text(300),
        'note_text': fake.text(3000),
        'author': {
            'first_name': fake.first_name(),
            'second_name': fake.last_name()
        },
        'tags': [
            {'name': fake.word()},
            {'name': fake.word()},
            {'name': fake.word()},
        ],
        'cover': {
            'url': 'https://loremflickr.com/%s/%s' % rand_ratio(),
        }
    }
