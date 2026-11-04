from pydantic import BaseModel, Field, ConfigDict


class TaskCreate(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=120
    )

    description: str | None = Field(
        default=None,
        max_length=500
    )


class TaskUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=120
    )

    description: str | None = Field(
        default=None,
        max_length=500
    )

    is_completed: bool | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    is_completed: bool

    model_config = ConfigDict(
        from_attributes=True
    )
