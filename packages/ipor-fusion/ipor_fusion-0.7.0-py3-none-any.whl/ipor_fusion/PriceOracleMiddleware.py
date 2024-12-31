from typing import List

from eth_abi import encode, decode
from eth_utils import function_signature_to_4byte_selector
from hexbytes import HexBytes
from web3 import Web3
from web3.types import LogReceipt

from ipor_fusion.TransactionExecutor import TransactionExecutor


class AssetPriceSource:
    def __init__(self, asset: str, source: str):
        self.asset = asset
        self.source = source


class PriceOracleMiddleware:

    def __init__(
        self,
        transaction_executor: TransactionExecutor,
        price_oracle_middleware_address: str,
    ):
        self._transaction_executor = transaction_executor
        self._price_oracle_middleware_address = price_oracle_middleware_address

    def address(self) -> str:
        return self._price_oracle_middleware_address

    def get_source_of_asset_price(self, asset: str) -> str:
        signature = function_signature_to_4byte_selector(
            "getSourceOfAssetPrice(address)"
        )
        read = self._transaction_executor.read(
            self._price_oracle_middleware_address,
            signature + encode(["address"], [asset]),
        )
        (source_of_asset_price,) = decode(["address"], read)
        return source_of_asset_price

    def CHAINLINK_FEED_REGISTRY(self) -> str:
        signature = function_signature_to_4byte_selector("CHAINLINK_FEED_REGISTRY()")
        read = self._transaction_executor.read(
            self._price_oracle_middleware_address, signature
        )
        (chainlink_feed_registry,) = decode(["address"], read)
        return chainlink_feed_registry

    def get_assets_price_sources(self) -> (int, int):
        events = self.get_asset_price_source_updated_events()

        assets_price_sources = []
        for event in events:
            (asset, source) = decode(["address", "address"], event["data"])
            assets_price_sources.append(
                AssetPriceSource(
                    Web3.to_checksum_address(asset), Web3.to_checksum_address(source)
                )
            )

        return assets_price_sources

    def get_asset_price_source_updated_events(self) -> List[LogReceipt]:
        event_signature_hash = HexBytes(
            Web3.keccak(text="AssetPriceSourceUpdated(address,address)")
        ).to_0x_hex()
        logs = self._transaction_executor.get_logs(
            contract_address=self._price_oracle_middleware_address,
            topics=[event_signature_hash],
        )
        return logs
