from pydantic import BaseModel


class ProfileCreate(BaseModel):

    age: int | None = None

    height: float | None = None

    weight: float | None = None

    fitness_goal: str | None = None

    diet_preference: str | None = None

    sleep_goal: float | None = None

    water_goal: float | None = None