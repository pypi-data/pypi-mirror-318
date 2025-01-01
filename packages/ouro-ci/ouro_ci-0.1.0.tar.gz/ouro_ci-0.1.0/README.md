# ouro

ouro is a Python-based DSL (domain specific language) for generating GitHub Actions workflows, without needing to write YAML. 

This package is currently under development.

## Why ouro?

- No more YAML
- Fully programmable
- Less duplication
- Sync with GitHub Actions

## Quickstart

1. Install `ouro`

```python
pip install ouro
```

2. Create a Python script
```python
from ouro.core import Workflow, Job, Step
from ouro.primitives import RunnerImage, GHAEvent


def create_workflow():
    steps = [
        Step(name="Checkout", uses="actions/checkout@v2"),
        Step(name="Install dependencies", run="pip install -r requirements.txt"),
        Step(name="Run tests", run="pytest"),
    ]

    jobs = {"test": Job(runs_on=RunnerImage.UBUNTU_LATEST, steps=steps)}

    return Workflow(
        name="CI",
        on={
            GHAEvent.PUSH: {"branches": ["main"], "tags": ["v*"]},
            GHAEvent.PULL_REQUEST: {"branches": ["main"]},
        },
        jobs=jobs,
    )
```

3. Run `ouro synth` to generate your workflow(s)


Built with ❤️ and 🐍