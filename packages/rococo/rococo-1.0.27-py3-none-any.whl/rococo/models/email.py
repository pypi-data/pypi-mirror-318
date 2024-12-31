"""
Email model
"""

from dataclasses import dataclass, field
from typing import Optional

from . import VersionedModel

@dataclass
class Email(VersionedModel):
    """A email method model."""

    person: str = field(default=None, metadata={
        'relationship': {'model': 'Person'},
        'field_type': 'entity_id'
    })
    email: Optional[str] = None
    is_verified: bool = False
    is_default: bool = False
