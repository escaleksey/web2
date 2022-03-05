from flask import Flask
from data import db_session
from data.user import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

def user_create(surname, name, age, position, speciality, address, email, hashed_password):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    user.hashed_password = hashed_password
    return user


def main():
    db_session.global_init("db/mars.db")
    db_sess = db_session.create_session()
    db_sess.add(user_create("Scott", "Ridley", 21, "captain",
                            "research engineer", "module_1", "scott_chief@mars.org", "cap"))
    db_sess.commit()
    db_sess.add(user_create("Kushnarev", "Aleksey", 16, "student",
                            "programmer", "module_2", "Aleksey@mars.org", "notcap"))
    db_sess.commit()
    db_sess.add(user_create("Popov", "Arthur", 17, "DJ",
                            "dj", "module_1", "Arthur@mars.org", "dj"))
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False

    db_sess.add(job)
    db_sess.commit()
    db_sess.close()
    #app.run()



if __name__ == '__main__':
    main()