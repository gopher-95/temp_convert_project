import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv()
APP_NAME = os.getenv("APP_NAME", "Temperature converter")
APP_AUTHOR = os.getenv("APP_AUTHOR", "Unknown")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

app = FastAPI(title=APP_NAME)


def convert_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def convert_kelvin(celsius):
    return celsius + 273.15


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": APP_VERSION}


@app.get("/convert/fahrenheit")
def celsius_to_fahrenheit(celsius: float):
    return {"celsius": celsius, "fahrenheit": convert_fahrenheit(celsius)}


@app.get("/convert/kelvin")
def celsius_to_kelvin(celsius: float):
    return {"celsius": celsius, "kelvin": convert_kelvin(celsius)}


@app.get("/convert/all")
def convert_all_temp(celsius: float):
    return {
        "celsius": celsius,
        "fahrenheit": convert_fahrenheit(celsius),
        "kelvin": convert_kelvin(celsius),
    }


@app.get("/convert/to/{unit}")
def convert_to_unit(unit: str, celsius: float):
    if unit == "fahrenheit":
        result = {"celsius": celsius, "fahrenheit": convert_fahrenheit(celsius)}
    elif unit == "kelvin":
        result = {"celsius": celsius, "kelvin": convert_kelvin(celsius)}
    else:
        raise HTTPException(
            status_code=400,
            detail=f"Не удалось распознать: {unit}. Используйте 'fahrenheit' или 'kelvin'.",
        )

    return result
