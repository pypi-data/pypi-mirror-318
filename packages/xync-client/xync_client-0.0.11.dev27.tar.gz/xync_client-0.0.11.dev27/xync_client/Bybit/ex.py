import json
from asyncio import run
from enum import IntEnum

from x_model import init_db
from xync_schema import models
from xync_schema.models import Ex

from xync_client.Abc.Base import ListOfDicts, MapOfIdsList, DictOfDicts, FlatDict
from xync_client.Abc.Ex import BaseExClient
from xync_client.loader import PG_DSN


class AdsStatus(IntEnum):
    REST = 0
    WORKING = 1


class ExClient(BaseExClient):  # Bybit client
    host = "api2.bybit.com"
    headers = {"cookie": ";"}  # rewrite token for public methods

    async def _get_config(self):
        resp = await self._get("/fiat/p2p/config/initial")
        return resp["result"]  # todo: tokens, pairs, ...

    # 20: Список всех платежных методов на бирже
    async def pms(self) -> DictOfDicts:
        pms = await self._post("/fiat/otc/configuration/queryAllPaymentList/")
        pms = pms["result"]["paymentConfigVo"]
        return {
            pm["paymentType"]: {
                "name": pm["paymentName"],
            }
            for pm in pms
        }

    # 21: Список поддерживаемых валют
    async def curs(self) -> FlatDict:
        config = await self._get_config()
        return {c["currencyId"]: c["currencyId"] for c in config["currencies"]}

    # 22: Список платежных методов по каждой валюте
    async def cur_pms_map(self) -> MapOfIdsList:
        pms = await self._post("/fiat/otc/configuration/queryAllPaymentList/")
        return json.loads(pms["result"]["currencyPaymentIdMap"])

    # 23: Список торгуемых монет (с ограничениям по валютам, если есть)
    async def coins(self) -> FlatDict:
        config = await self._get_config()
        cc: set[str] = set()
        for c in config["symbols"]:
            cc.add(c["tokenId"])
        return {c: c for c in cc}

    # 24: Список торгуемых монет (с ограничениям по валютам, если есть)
    async def pairs(self) -> FlatDict:
        config = await self._get_config()
        cc: dict[str, set[str]] = {}
        for c in config["symbols"]:
            cc[c["currencyId"]] = cc.get(c["currencyId"], set()) | {c["tokenId"]}
        return cc

    # 25: Список объяв по (buy/sell, cur, coin, pm)
    async def ads(
        self, coin_exid: str, cur_exid: str, is_sell: bool, pm_exids: list[str | int] = None, amount: int = None
    ) -> ListOfDicts:
        data = {
            "userId": "",
            "tokenId": coin_exid,
            "currencyId": cur_exid,
            "payment": pm_exids or [],
            "side": "0" if is_sell else "1",
            "size": "10",
            "page": "1",
            "amount": str(amount) if amount else "",
            "authMaker": False,
            "canTrade": False,
        }
        ads = await self._post("/fiat/otc/item/online/", data)
        return ads["result"]["items"]


async def main():
    _ = await init_db(PG_DSN, models, True)
    bg = await Ex.get(name="Bybit")
    cl = ExClient(bg)
    # await cl.curs()
    await cl.coins()
    # await cl.ads("BTC", "RUB", True, [1, 289, 375])
    # await cl.pms()
    # await cl.cur_pms_map()
    # await cl.set_pmcurexs()
    # await cl.set_coinexs()
    await cl.close()


if __name__ == "__main__":
    run(main())
