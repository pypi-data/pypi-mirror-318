from enum import Enum


class RunnerImage(str, Enum):
    """Available runner operating systems."""

    UBUNTU_LATEST = "ubuntu-latest"
    UBUNTU_24_04 = "ubuntu-24.04"
    UBUNTU_22_04 = "ubuntu-22.04"
    UBUNTU_20_04 = "ubuntu-20.04"
    WINDOWS_LATEST = "windows-latest"
    WINDOWS_2025 = "windows-2025"
    WINDOWS_2022 = "windows-2022"
    WINDOWS_2019 = "windows-2019"
    MACOS_LATEST = "macos-latest"
    MACOS_15 = "macos-15"
    MACOS_14 = "macos-14"
    MACOS_13 = "macos-13"


class RunnerArch(str, Enum):
    """Available runner architectures."""

    X64 = "x64"
    ARM64 = "arm64"
    ARM = "arm"


class GHAEvent(str, Enum):
    """Common GitHub Actions event types."""

    PUSH = "push"
    PULL_REQUEST = "pull_request"
    RELEASE = "release"
    WORKFLOW_DISPATCH = "workflow_dispatch"
    SCHEDULE = "schedule"


class PushEventConfig(str, Enum):
    """Configuration options for the push event."""

    BRANCH = "branch"
    TAG = "tag"
    PATHS = "paths"


class PullRequestEventConfig(str, Enum):
    """Configuration options for the pull_request event."""

    TYPES = "types"
    BRANCHES = "branches"
    PATHS = "paths"


class ReleaseEventConfig(str, Enum):
    """Configuration options for the release event."""

    TYPES = "types"
    BRANCHES = "branches"
    PATHS = "paths"


class WorkflowDispatchEventConfig(str, Enum):
    """Configuration options for the workflow_dispatch event."""

    INPUTS = "inputs"


class ScheduleEventConfig(str, Enum):
    """Configuration options for the schedule event."""

    CRON = "cron"
    EVENTS = "events"
