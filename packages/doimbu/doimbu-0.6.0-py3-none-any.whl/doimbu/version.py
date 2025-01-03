from __future__ import annotations

from pydantic import BaseModel, Field, PositiveInt, field_validator

DOCKER_IMAGE_FIRST_VERSION = '0.1.0'


def parse_version(version: str) -> tuple[int, int, int]:
    version_sections = version.split('.')

    for _ in range(len(version_sections), 3):
        version_sections.append('0')

    major, minor, patch = version_sections

    return int(major), int(minor), int(patch)

class Version(BaseModel):
    version: str
    major: int = Field(gt=0, default=0)
    minor: PositiveInt = 0
    patch: int = Field(gt=0, default=0)

    def model_post_init(self, *args, **kwargs):
        self.major, self.minor, self.patch = parse_version(self.version)
        self.version = f'{self.major}.{self.minor}.{self.patch}'

    # noinspection PyNestedDecorators
    @field_validator('version')
    @classmethod
    def max_3_sections(cls, value: str) -> str:
        assert len(value.split('.')) <= 3, (
            f'Invalid version {value}. '
            f'It must have at most 3 dot separated sections '
            f'(major.minor.patch).')

        return value

    # noinspection PyNestedDecorators
    @field_validator('version')
    @classmethod
    def only_positive_sections(cls, value: str) -> str:
        for section in value.split('.'):
            try:
                if int(section) < 0:
                    raise ValueError(
                        f'Version section must be greater than zero. '
                        f'{value} was found. ')
            finally:
                pass

        return value

    def __ge__(self, other_version: Version) -> bool:
        if self.major > other_version.major:
            return True
        elif self.major < other_version.major:
            return False

        if self.minor > other_version.minor:
            return True
        elif self.minor < other_version.minor:
            return False

        if self.patch > other_version.patch:
            return True
        elif self.patch < other_version.patch:
            return False

        return True

    def __repr__(self):
        return self.version
