from pydantic import BaseModel, Field, field_validator
from typing import Dict, List, Optional, Union

import yaml

from helpers import EnumYAMLDumper
from primitives import RunnerImage, GHAEvent


class Step(BaseModel):
    name: str = Field(..., description="The name of the step")
    uses: Optional[str] = Field(None, description="The action to use")
    run: Optional[str] = Field(None, description="The command to run")
    with_: Optional[Dict[str, str]] = Field(
        None, description="The inputs for the action", alias="with"
    )
    env: Optional[Dict[str, str]] = Field(
        None, description="The environment variables for the step"
    )

    @field_validator("uses", "run", mode="before")
    def check_conflict_run_and_uses(cls, value, info):
        """
        Validate that both `run` and `uses` are not defined in the same step.
        """
        # Check the field being validated and the current state of the model
        data = info.data
        print(data)
        if data.get("uses") and data.get("run"):
            raise ValueError("Cannot define both 'run' and 'uses' in the same step.")
        return value

    def to_dict(self):
        """Convert the Step into the GitHub Actions step format"""
        return self.model_dump(by_alias=True, exclude_none=True)

    class Config:
        allow_population_by_field_name = True
        extra = "forbid"


class Job(BaseModel):
    runs_on: Union[RunnerImage, str] = Field(
        ..., description="The runner to use", alias="runs-on"
    )
    steps: List[Step] = Field(default_factory=list, description="The steps to run")
    env: Optional[Dict[str, str]] = Field(
        None, description="The environment variables for the job"
    )
    if_: Optional[str] = Field(
        None, description="The condition to run the job", alias="if"
    )

    def to_dict(self):
        """Convert the Job into the GitHub Actions job format"""
        return {
            **self.model_dump(by_alias=True, exclude_none=True),
            "steps": [step.to_dict() for step in self.steps],
        }

    class Config:
        allow_population_by_field_name = True
        populate_by_name = True
        extra = "forbid"


class Workflow(BaseModel):
    name: str
    on: Union[
        List[GHAEvent],  # A simple list of events
        Dict[
            GHAEvent, Dict[str, Union[str, List[str]]]
        ],  # A dictionary of events with their configurations
    ]
    jobs: Dict[str, Job] = Field(default_factory=dict)

    def to_dict(self):
        """Convert the Workflow into the GitHub Actions workflow format."""
        base = self.model_dump(by_alias=True, exclude_none=True)
        if isinstance(base["on"], list):
            base["on"] = [event.value for event in base["on"]]
        if isinstance(base["on"], dict):
            base["on"] = {event.value: config for event, config in base["on"].items()}
        return base

    def to_yaml(self):
        """Convert the Workflow into a YAML string."""
        data = self.to_dict()
        return yaml.dump(
            data, Dumper=EnumYAMLDumper, default_flow_style=False, sort_keys=False
        )

    class Config:
        extra = "forbid"
