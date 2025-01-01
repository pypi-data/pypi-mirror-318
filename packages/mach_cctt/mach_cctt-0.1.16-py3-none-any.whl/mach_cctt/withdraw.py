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
    SupportedChain,
    Token,
)
from mach_client.asset.token import NATIVE_COIN_ADDRESS

from .log import Logger


async def withdraw_network(
    client: MachClient,
    asset_server: AssetServer,
    account: Account,
    recipient: AccountID,
) -> None:
    balances = await asset_server.get_token_balances(account.downcast())

    # This has to be done sequentially to avoid nonce issues
    for chain, chain_balances in balances.items():
        for token, balance in chain_balances.items():
            if balance <= 0 or isinstance(token, NativeCoin):
                continue

            await token.transfer(
                sender=account,
                recipient=recipient,
                amount=balance,
            )

        # Transfer gas last

        if not (native_coin := Token.try_lookup_address(chain, NATIVE_COIN_ADDRESS)):
            continue

        # TODO: `client.estimate_gas` is the gas estimate for a Mach transaction, not a transfer
        # This could leave more dust than necessary
        balance, gas_estimate = await asyncio.gather(
            native_coin.get_balance(account.downcast()), client.estimate_gas(chain)
        )

        if (
            amount := balance - gas_estimate.gas_estimate * gas_estimate.gas_price
        ) <= 0:
            continue

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
    coros = []
    withdraw_chains = []

    for chain in SupportedChain:
        account = account_manager.get(chain.value)
        recipient = recipients.get(chain.value)

        if not account or not recipient:
            continue

        coros.append(withdraw_network(client, asset_server, account, recipient))
        withdraw_chains.append(chain.value)

    exceptions = []

    for chain, result in zip(
        withdraw_chains, await asyncio.gather(*coros, return_exceptions=True)
    ):
        if isinstance(result, Exception):
            logger.error(f"Failed to withdraw on network {chain}:", exc_info=result)
            exceptions.append((chain, result))

    return exceptions
