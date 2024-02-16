import os

import reflex as rx
from dotenv import load_dotenv

load_dotenv()

config = rx.Config(
    app_name="silver_journey",
    db_url="postgresql://{user}:{password}@{hostname}:{port}/{db}".format(
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        hostname=os.environ['POSTGRES_HOSTNAME'],
        port=os.environ['POSTGRES_PORT'],
        db=os.environ['POSTGRES_DB'],
    ),
    telemetry_enabled=False,
)
