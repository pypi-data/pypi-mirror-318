from solana.rpc.async_api import AsyncClient
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from spl.token.instructions import create_mint, mint_to
from spl.token.constants import TOKEN_PROGRAM_ID
from config.settings import Settings


class BlockchainManager:
    def __init__(self):
        self.settings = Settings()
        self.client = AsyncClient(self.settings.solana_rpc_url)
        self.mint_authority = Keypair.from_secret_key(
            bytes(self.settings.admin_private_key)
        )

    async def create_token(self, agent_id: str, initial_supply: int) -> str:
        # Create mint account
        mint_account = Keypair()

        # Calculate minimum lamports for mint account
        mint_rent = await self.client.get_minimum_balance_for_rent_exemption(
            82
        )

        # Create transaction for token creation
        transaction = Transaction()
        transaction.add(
            create_mint(
                TOKEN_PROGRAM_ID,
                mint_account.pubkey(),
                self.mint_authority.pubkey(),
                None,
                9  # decimals
            )
        )

        # Send and confirm transaction
        result = await self.client.send_transaction(
            transaction,
            self.mint_authority,
            mint_account
        )

        if result["result"]:
            mint_address = str(mint_account.pubkey())
            return mint_address
        else:
            raise Exception("Failed to create token")

    async def mint_tokens(
            self,
            token_address: str,
            recipient: str,
            amount: int
    ) -> bool:
        mint_pubkey = Pubkey.from_string(token_address)
        recipient_pubkey = Pubkey.from_string(recipient)

        transaction = Transaction()
        transaction.add(
            mint_to(
                TOKEN_PROGRAM_ID,
                mint_pubkey,
                recipient_pubkey,
                self.mint_authority.pubkey(),
                amount
            )
        )

        result = await self.client.send_transaction(
            transaction,
            self.mint_authority
        )

        return bool(result["result"])

    async def get_token_balance(
            self,
            token_address: str,
            wallet_address: str
    ) -> int:
        response = await self.client.get_token_account_balance(
            Pubkey.from_string(token_address)
        )
        return int(response["result"]["value"]["amount"])

    async def get_sol_balance(self, wallet_address: str) -> int:
        response = await self.client.get_balance(
            Pubkey.from_string(wallet_address)
        )
        return response["result"]["value"]