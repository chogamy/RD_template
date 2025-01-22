import os
import argparse
from pydantic import BaseModel

from typing import Optional

from fastapi import FastAPI

DIR = os.path.dirname(os.path.realpath(__file__))


app = FastAPI()


class Test(BaseModel):
    test: Optional[str] = None


@app.post("/app/test")
def test(test: Test):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", default=None, type=str)
    args = parser.parse_args()

    # research in here
