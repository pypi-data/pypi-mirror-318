from dotenv import load_dotenv
import os
from web3 import Web3
from .ostium import Ostium
from .config import NetworkConfig


class OstiumSDK:
    def __init__(self, network="mainnet", private_key: str = None, rpc_url: str = None):
        load_dotenv()
        self.private_key = private_key or os.getenv('PRIVATE_KEY')
        if not self.private_key:
            raise ValueError(
                "No private key provided. Please provide via constructor or PRIVATE_KEY environment variable")

        self.rpc_url = rpc_url or os.getenv('RPC_URL')
        if not self.rpc_url:
            raise ValueError(
                f"No RPC URL provided for {network}. Please provide via constructor or RPC_URL environment variable")

        # Initialize Web3
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))

        # Get network configuration
        if network == "mainnet":
            self.network_config = NetworkConfig.mainnet()
        elif network == "testnet":
            self.network_config = NetworkConfig.testnet()
        else:
            raise ValueError(
                f"Unsupported network: {network}. Use 'mainnet' or 'testnet'")

        # Initialize Ostium instance
        self.ostium = Ostium(
            self.w3,
            self.network_config.contracts["usdc"],
            self.network_config.contracts["tradingStorage"],
            self.network_config.contracts["trading"],
            private_key=self.private_key
        )
