import re
from asyncio import run, sleep
from json import JSONDecoder

from bs4 import BeautifulSoup, Script
from x_model import init_db
from xync_schema import models
from xync_schema.models import Coin, Cur, Pm, Ad, Ex

from xync_client.Abc.Base import MapOfIdsList, DictOfDicts, FlatDict
from xync_client.Abc.Ex import BaseExClient
from xync_client.loader import PG_DSN


class ExClient(BaseExClient):
    async def cur_pms_map(self) -> MapOfIdsList:
        pass

    async def curs(self) -> FlatDict:
        curs = await self._post("/json_svr/buy_crypto_fiat_setting")
        curs = {cur["fiat"]: cur["fiat"] for cur in curs["datas"] if cur["p2p"]}
        return curs

    async def coins(self, cur: Cur = None) -> list[Coin]: ...

    async def pms(self, cur: Cur = None) -> DictOfDicts:
        await sleep(1)
        doc = await self._get("/p2p")
        await sleep(1)
        soup = BeautifulSoup(doc, "html.parser")
        script: Script = soup.body.find_all("script")[17]  # 17-th not stable
        strng = (
            script.get_text(strip=True)
            .replace("\n", "")
            .replace("  ", "")
            .replace(
                ',\'bank\': {image: "/images/payment/bank.png",index: "2",pay_name: lang_string("银行卡"),pay_type: "bank",rgb: "#FF860D",}',
                "",
            )
        )
        # pattern = r'var c2cData = (\{.*?\})\s+var transLang'
        # pattern = r'payment_settings:\s{1}(\{.*?\}),\s?// 用户放开的支付方式'
        pattern = r"payment_settings:\s{1}(\{.*?\}),paymentIdMap:"
        match = re.search(pattern, strng.replace(",}", "}").replace(",]", "]"), re.DOTALL)
        res = match.group(1)
        pms = JSONDecoder(strict=False).decode(res)
        return {
            pm["index"]: {"name": pm["pay_name"], "logo": pm["image"], "identifier": idf, "type_": pm["base_type"]}
            for idf, pm in pms.items()
        }
        # pmcurs = {
        #     cur.ticker: (await self._get("/v3/c2c/configs/receipt/templates", {"quoteCurrency": cur.ticker}))["data"]
        #     for cur in await self.curs()
        # }
        # pp = {}
        # [[pp.update({p["paymentMethod"]: p["paymentMethodDescription"]}) for p in ps] for ps in pmcurs.values()]
        # pp = {k: v for k, v in sorted(pp.items(), key=lambda x: x[0])}
        # return pp

    async def ads(self, coin: Coin, cur: Cur, is_sell: bool, pms: list[Pm] = None) -> list[Ad]:
        pass


async def main():
    _ = await init_db(PG_DSN, models, True)
    bg = await Ex.get(name="Gate")
    cl = ExClient(bg)
    await cl.curs()
    # await cl.coins()
    pms = await cl.pms()
    print(pms)


if __name__ == "__main__":
    run(main())
