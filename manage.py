import os
from flask_script import Manager 
from flask_migrate import Migrate, MigrateCommand
from develop import instance
from app import models
from app import db, create_app

config_name = "development"
APP = create_app(config_name)

migrate = Migrate(APP, db)
manager = Manager(APP)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
    