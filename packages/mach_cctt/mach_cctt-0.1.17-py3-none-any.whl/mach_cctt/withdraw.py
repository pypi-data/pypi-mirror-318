import asyncio

from mach_client import (
    Account,
    AccountID,
    AccountIDManager,
    AccountManager,
    AssetServer,
    Chain,
    MachClient,
    NativeCoin,
    Token,
)
from mach_client.asset.token import NATIVE_COIN_ADDRESS

from .log import Logger


async def withdraw_chain(
    client: MachClient,
    account: Account,
    recipient: AccountID,
    balances: dict[Token, int],
) -> None:
    for token, balance in balances.items():
        if balance <= 0 or isinstance(token, NativeCoin):
            continue

        await token.transfer(
            sender=account,
            recipient=recipient,
            amount=balance,
        )

    # Transfer gas last

    if not (
        native_coin := Token.try_lookup_address(account.chain, NATIVE_COIN_ADDRESS)
    ):
        return

    # TODO: `client.estimate_gas` is the gas estimate for a Mach transaction, not a transfer
    # This could leave more dust than necessary
    balance, gas_estimate = await asyncio.gather(
        native_coin.get_balance(account.downcast()),
        client.estimate_gas(account.chain),
    )

    if (amount := balance - gas_estimate.gas_estimate * gas_estimate.gas_price) <= 0:
        return

    await native_coin.transfer(
        sender=account,
        recipient=recipient,
        amount=amount,
    )


async def withdraw(
    client: MachClient,
    asset_server: AssetServer,
    account_manager: AccountManager,
    recipients: AccountIDManager,
    logger: Logger,
) -> list[tuple[Chain, Exception]]:
    balances = await asset_server.get_all_token_balances(account_manager.downcast())
    coros = []

    for chain, chain_balances in balances.items():
        account = account_manager.get(chain)
        recipient = recipients.get(chain)

        if not account or not recipient:
            continue

        coros.append(withdraw_chain(client, account, recipient, chain_balances))

    exceptions = []

    for chain, result in zip(
        balances.keys(), await asyncio.gather(*coros, return_exceptions=True)
    ):
        if isinstance(result, Exception):
            logger.error(f"Failed to withdraw on {chain}:", exc_info=result)
            exceptions.append((chain, result))

    return exceptions
