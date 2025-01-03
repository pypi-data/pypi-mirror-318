from dotenv import load_dotenv
import os
from web3 import Web3
from .ostium import Ostium


class OstiumSDK:
    def __init__(self, network="arbitrum", private_key: str = None, rpc_url: str = None):
        load_dotenv()
        self.private_key = private_key or os.getenv('OSTIUM_PRIVATE_KEY')
        if not self.private_key:
            raise ValueError(
                "No private key provided. Please provide via constructor or OSTIUM_PRIVATE_KEY environment variable")

        # Use provided RPC URL or get from env
        self.rpc_url = rpc_url or os.getenv('OSTIUM_RPC_URL')
        if not self.rpc_url:
            raise ValueError(
                "No RPC URL provided. Please provide via constructor or OSTIUM_RPC_URL environment variable")

        # Initialize Web3
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))

        # Set network-specific addresses
        if network == "arbitrum":
            self.usdc_address = "0xaf88d065e77c8cC2239327C5EDb3A432268e5831"
            self.ostium_trading_storage_address = "0x937F3002dE1C7b9E6f461f5F5C5Ac5cA8A1a6339"
            self.ostium_trading_address = "0x4c78B6566864e374a5949C6EE1408Fd0Fe01A6ED"
        else:
            raise ValueError(f"Unsupported network: {network}")

        # Initialize Ostium instance
        self.ostium = Ostium(
            self.w3,
            self.usdc_address,
            self.ostium_trading_storage_address,
            self.ostium_trading_address,
            private_key=self.private_key
        )
