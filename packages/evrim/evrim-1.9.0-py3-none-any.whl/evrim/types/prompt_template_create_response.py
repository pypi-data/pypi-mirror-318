# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["PromptTemplateCreateResponse"]


class PromptTemplateCreateResponse(BaseModel):
    fields: List[Dict[str, object]]

    name: str

    questions: Optional[List[str]] = None
