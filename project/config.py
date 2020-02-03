from project.environment import env


class ConfigFlask(object):
    # Reload app after each change in our code
    DEBUG = env.bool("BACKEND_DEBUG")
    # Enable CSRF protection
    CSRF_ENABLED = env.bool("BACKEND_CSRF_ENABLED")
    # Where backend is allocated (0.0.0.0 to expose it or localhost to avoid external request)
    HOST = env.str("BACKEND_HOST")
    # Port where backend is listening
    PORT = env.int("BACKEND_CONTAINER_PORT")


class ConfigDB(object):
    # Where database is allocated and required credentials
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4".format(
        env.str("DATABASE_USER"),
        env.str("DATABASE_PASSWORD"),
        env.str("DATABASE_HOST"),
        env.str("DATABASE_CONTAINER_PORT"),
        env.str("DATABASE_NAME")
    )
    # Track the object modifications (something like flush)
    SQLALCHEMY_TRACK_MODIFICATIONS = env.bool("DATABASE_TRACK_MODIFICATIONS")
    # Display the excuted queries to debug
    SQLALCHEMY_ECHO = env.str("DATABASE_ECHO")
    # Where are the database migration scripts 
    MIGRATION_PATH = env.str("DATABASE_MIGRATION_PATH")