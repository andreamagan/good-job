from project import app, config
from project.config import ConfigFlask

# Run app
app.run(host=ConfigFlask.HOST, port=ConfigFlask.PORT)