import uvicorn
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By

from selenium.webdriver.edge.options import Options
from fastapi import FastAPI

PORT = "$PORT"
HOST = "0.0.0.0"

app = FastAPI()

@app.get("/temperature")
def get_temperature():
    chrome_options = Options()
    wd = Edge(options=chrome_options)
    wd.get("https://www.bergfex.at/sommer/eibiswald/wetter/")
    return wd.find_element(By.CLASS_NAME, 'value').text


if __name__ == '__main__':
    uvicorn.run(app, host=HOST, port=PORT)