from typing import Optional
from web3 import Web3
from .config import NetworkConfig
from .ostium import Ostium
# from .formulae import Formulae
from .subgraph import SubgraphClient
from .price import Price
from .balance import Balance


class OstiumSDK:
    def __init__(
        self,
        network_config: NetworkConfig,
        custom_rpc_url: Optional[str] = None,
        custom_graph_url: Optional[str] = None
    ):
        self.config = network_config
        self.w3 = Web3(Web3.HTTPProvider(
            custom_rpc_url or network_config.rpc_url
        ))
        self.ostium = Ostium(
            self.w3,
            network_config.contracts["usdc"],
            network_config.contracts["trading"],
            network_config.contracts["tradingStorage"]
        )
        # self.formulae = Formulae()
        self.subgraph = SubgraphClient(
            custom_graph_url or network_config.graph_url
        )
        self.price = Price()
        self.balance = Balance(self.w3, network_config.contracts["usdc"])
