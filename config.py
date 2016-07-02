import os
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

BLOGGING_DISQUS_SITENAME = "vctr"

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# pagination
BLOGS_PER_PAGE = 3
