from project import app
from project.config import ConfigFlask

# Run app
if __name__ == '__main__':
    app.run(host=ConfigFlask.HOST, port=ConfigFlask.PORT)