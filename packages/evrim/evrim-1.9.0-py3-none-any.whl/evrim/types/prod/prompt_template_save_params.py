# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PromptTemplateSaveParams"]


class PromptTemplateSaveParams(TypedDict, total=False):
    fields: Required[Iterable[Dict[str, object]]]

    name: Required[str]

    questions: List[str]
