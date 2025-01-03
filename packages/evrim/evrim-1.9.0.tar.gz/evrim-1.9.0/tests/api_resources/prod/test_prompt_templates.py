# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evrim import Evrim, AsyncEvrim
from evrim.types import Template
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPromptTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_save(self, client: Evrim) -> None:
        prompt_template = client.prod.prompt_templates.save(
            fields=[{"foo": "bar"}],
            name="name",
        )
        assert_matches_type(Template, prompt_template, path=["response"])

    @parametrize
    def test_method_save_with_all_params(self, client: Evrim) -> None:
        prompt_template = client.prod.prompt_templates.save(
            fields=[{"foo": "bar"}],
            name="name",
            questions=["string"],
        )
        assert_matches_type(Template, prompt_template, path=["response"])

    @parametrize
    def test_raw_response_save(self, client: Evrim) -> None:
        response = client.prod.prompt_templates.with_raw_response.save(
            fields=[{"foo": "bar"}],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_template = response.parse()
        assert_matches_type(Template, prompt_template, path=["response"])

    @parametrize
    def test_streaming_response_save(self, client: Evrim) -> None:
        with client.prod.prompt_templates.with_streaming_response.save(
            fields=[{"foo": "bar"}],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_template = response.parse()
            assert_matches_type(Template, prompt_template, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPromptTemplates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_save(self, async_client: AsyncEvrim) -> None:
        prompt_template = await async_client.prod.prompt_templates.save(
            fields=[{"foo": "bar"}],
            name="name",
        )
        assert_matches_type(Template, prompt_template, path=["response"])

    @parametrize
    async def test_method_save_with_all_params(self, async_client: AsyncEvrim) -> None:
        prompt_template = await async_client.prod.prompt_templates.save(
            fields=[{"foo": "bar"}],
            name="name",
            questions=["string"],
        )
        assert_matches_type(Template, prompt_template, path=["response"])

    @parametrize
    async def test_raw_response_save(self, async_client: AsyncEvrim) -> None:
        response = await async_client.prod.prompt_templates.with_raw_response.save(
            fields=[{"foo": "bar"}],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt_template = await response.parse()
        assert_matches_type(Template, prompt_template, path=["response"])

    @parametrize
    async def test_streaming_response_save(self, async_client: AsyncEvrim) -> None:
        async with async_client.prod.prompt_templates.with_streaming_response.save(
            fields=[{"foo": "bar"}],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt_template = await response.parse()
            assert_matches_type(Template, prompt_template, path=["response"])

        assert cast(Any, response.is_closed) is True
