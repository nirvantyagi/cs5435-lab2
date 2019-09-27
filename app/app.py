from bottle import install, run, TEMPLATE_PATH
from bottle.ext import sqlalchemy as orm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import app.api
import app.models
from app.scripts.registration import register_users
from app.scripts.breaches import load_breaches

TEMPLATE_PATH.insert(0, 'app/views/')


def run_server():
    # database setup
    engine = create_engine('sqlite:///:memory:', echo=True)
    app.models.base.Base.metadata.create_all(engine)

    # initialize database
    Session = sessionmaker(bind=engine)
    session = Session()

    register_users(session)

    session.commit()
    session.close()


    # run server
    install(orm.Plugin(
        engine,
        keyword='db',
    ))
    run(host='localhost', port=8080)

