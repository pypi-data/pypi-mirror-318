from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bot_webhook_update import BotWebhookUpdate
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_uuid: str,
    *,
    body: BotWebhookUpdate,
    x_telegram_bot_api_secret_token: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_telegram_bot_api_secret_token, Unset):
        headers["x-telegram-bot-api-secret-token"] = x_telegram_bot_api_secret_token

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/bot-webhook/{bot_uuid}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = response.json()
        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    bot_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BotWebhookUpdate,
    x_telegram_bot_api_secret_token: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Bot Webhook

    Args:
        bot_uuid (str):
        x_telegram_bot_api_secret_token (Union[None, Unset, str]):
        body (BotWebhookUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        bot_uuid=bot_uuid,
        body=body,
        x_telegram_bot_api_secret_token=x_telegram_bot_api_secret_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    bot_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BotWebhookUpdate,
    x_telegram_bot_api_secret_token: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Bot Webhook

    Args:
        bot_uuid (str):
        x_telegram_bot_api_secret_token (Union[None, Unset, str]):
        body (BotWebhookUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        bot_uuid=bot_uuid,
        client=client,
        body=body,
        x_telegram_bot_api_secret_token=x_telegram_bot_api_secret_token,
    ).parsed


async def asyncio_detailed(
    bot_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BotWebhookUpdate,
    x_telegram_bot_api_secret_token: Union[None, Unset, str] = UNSET,
) -> Response[Union[Any, HTTPValidationError]]:
    """Bot Webhook

    Args:
        bot_uuid (str):
        x_telegram_bot_api_secret_token (Union[None, Unset, str]):
        body (BotWebhookUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        bot_uuid=bot_uuid,
        body=body,
        x_telegram_bot_api_secret_token=x_telegram_bot_api_secret_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_uuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: BotWebhookUpdate,
    x_telegram_bot_api_secret_token: Union[None, Unset, str] = UNSET,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Bot Webhook

    Args:
        bot_uuid (str):
        x_telegram_bot_api_secret_token (Union[None, Unset, str]):
        body (BotWebhookUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            bot_uuid=bot_uuid,
            client=client,
            body=body,
            x_telegram_bot_api_secret_token=x_telegram_bot_api_secret_token,
        )
    ).parsed
