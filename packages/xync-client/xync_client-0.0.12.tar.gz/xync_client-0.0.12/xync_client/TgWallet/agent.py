from enum import StrEnum
from typing import Literal

from xync_schema.enums import AdStatus

from xync_client.Abc.Base import ListOfDicts
from xync_client.TgWallet.auth import AuthClient
from xync_schema.models import User, Cur, Order, Coin, OrderStatus, Pmex, Fiat, Ad, Pm
from xync_schema.pydantic import FiatNew

from xync_client.Abc.Agent import BaseAgentClient


class Exceptions(StrEnum):
    PM_KYC = "OFFER_FIAT_COUNTRY_NOT_SUPPORTED_BY_USER_KYC_COUNTRY"


# class Status(IntEnum):
#     ALL_ACTIVE = OrderStatus.active


class AgentClient(BaseAgentClient, AuthClient):
    # 0: Получшение ордеров в статусе status, по монете coin, в валюте coin, в направлении is_sell: bool
    async def get_orders(self, status: OrderStatus = OrderStatus.created, coin: Coin = None, cur: Cur = None, is_sell: bool = None) -> list[Order]:
        orders = await self._post(
            "/p2p/public-api/v2/offer/order/history/get-by-user-id",
            {"offset": 0, "limit": 100, "filter": {"status": "ALL_ACTIVE"}},  # "limit": 20
        )
        return orders

    # 1: [T] Получшение ордеров в статусе status, по монете coin, в валюте coin, в направлении is_sell: bool
    async def order_request(self, ad_id: int, amount: float) -> dict:
        pass

    # 25: Список реквизитов моих платежных методов
    async def my_fiats(self, cur: Cur = None) -> ListOfDicts:
        fiats = await self._post("/p2p/public-api/v3/payment-details/get/by-user-id")
        fiats = {fiat["id"]: fiat for fiat in fiats["data"]}
        return fiats

    # 26: Создание
    async def fiat_new(self, fiat: FiatNew) -> Fiat.pyd():
        pmex = await Pmex.get_or_create(pm_id=fiat.pm_id, ex=self.agent.ex)  # .prefetch_related('pm')
        cur = await Cur[fiat.cur_id]
        add_fiat = await self._post(
            "/p2p/public-api/v3/payment-details/create",
            {
                "paymentMethodCode": pmex.exid,
                "currencyCode": cur.ticker,
                "name": fiat.name,
                "attributes": {"version": "V1", "values": [{"name": "PAYMENT_DETAILS_NUMBER", "value": fiat.detail}]},
            },
        )
        return add_fiat

    # 27: Редактирование
    async def fiat_upd(self, fiat_id: int, detail: str, name: str = None) -> Fiat.pyd():
        edit_fiat = await self._post(
            "/p2p/public-api/v3/payment-details/edit",
            {
                "id": fiat_id,
                # "paymentMethodCode": code_pms,
                # "currencyCode": cur,
                "name": name,
                "attributes": {"version": "V1", "values": [{"name": "PAYMENT_DETAILS_NUMBER", "value": detail}]},
            },
        )
        return edit_fiat

    # 28: Удаление
    async def fiat_del(self, fiat_id: int) -> bool:
        del_fiat = await self._post("/p2p/public-api/v3/payment-details/delete", {"id": fiat_id})
        return del_fiat

    # 29: Список моих ad
    async def my_ads(self, status: AdStatus = None) -> ListOfDicts:
        mapping = {
            AdStatus.defActive: "INACTIVE",
            AdStatus.active: "ACTIVE"
        }
        ads = await self._post(
            "/p2p/public-api/v2/offer/user-own/list", {"offset": 0, "limit": 20, "offerType": "SALE"}
        )
        return [ad for ad in ads["data"] if ad["status"] == mapping[status]] if status else ads

    # 30: Создание ad
    async def ad_new(
        self,
        coin: Coin,
        cur: Cur,
        is_sell: bool,
        pms: list[Pm],
        amount: int,
        price: float,
        is_float: bool = True,
        min_fiat: int = None,
        details: str = None,
        autoreply: str = None,
        status: AdStatus = AdStatus.active
    ) -> Ad.pyd():
        create = await self._post(
            "/p2p/public-api/v2/offer/create",
            {
                "type": "SALE" if is_sell else "BUY",
                "initVolume": {"currencyCode": coin.ticker, "amount": f"{amount}"},
                "orderRoundingRequired": False,
                "price": {"type": "FIXED", "baseCurrencyCode": coin.ticker, "quoteCurrencyCode": cur.ticker, "value": price},
                "orderAmountLimits": {"min": min_fiat},
                "paymentConfirmTimeout": "PT15M" if is_sell else "PT3H",
                "comment": "",
                "paymentDetailsIds": pms,
            },
        )
        return create

    async def _get_my_ad(self, offer_id: int):
        get_own = await self._post('/p2p/public-api/v2/offer/get-user-own/', {"offerId": offer_id})
        return get_own['data']

    # 31: Редактирование
    async def ad_upd(
            self,
            offer_id: int,
            amount: int,
            pms: [Pm] = None,
            price: float = None,
            is_float: bool = None,
            min_fiat: int = None,
            details: str = None,
            autoreply: str = None,
            status: AdStatus = None,
    ) -> Ad.pyd():
        ad = await self._get_my_ad(offer_id)
        upd = await self._post(
            "/p2p/public-api/v2/offer/edit",
            {
                "offerId": offer_id,
                "paymentConfirmTimeout": ad['paymentConfirmTimeout'],
                "type": ad['type'],
                "orderRoundingRequired": False,
                "price": {"type": "FIXED", "value": price},
                "orderAmountLimits": {"min": min_fiat},
                "comment": "",  # TODO: comment
                "volume": f"{amount}",
                "paymentDetailsIds": pms,
            },
        )
        return upd

    # 32: Удаление
    async def ad_del(self, offer_id: int) -> bool:
        ad = await self._get_my_ad(offer_id)
        ad_del = await self._post("/p2p/public-api/v2/offer/delete", {"type": ad['type'], "offerId": offer_id})
        return ad_del

    # 33: Вкл/выкл объявления
    async def ad_switch(self, offer_id: int, active: bool) -> bool:
        ad = await self._get_my_ad(offer_id)
        if active:
            active = await self._post("/p2p/public-api/v2/offer/activate", {"type": ad['type'], "offerId": offer_id})
            return active
        else:
            off = await self._post("/p2p/public-api/v2/offer/deactivate", {"type": ad['type'], "offerId": offer_id})
            return off

    # 34: Вкл/выкл всех объявлений
    async def ads_switch(self, active: bool) -> bool:
        pass

    # 35: Получить объект юзера по его ид
    async def get_user(self, user_id) -> dict:
        pass

    # 36: Отправка сообщения юзеру с приложенным файлом
    async def send_user_msg(self, msg: str, file=None) -> bool:
        pass

    # 37: (Раз)Блокировать юзера
    async def block_user(self, is_blocked: bool = True) -> bool:
        pass

    # 38: Поставить отзыв юзеру
    async def rate_user(self, positive: bool) -> bool:
        pass

    # 39: Балансы моих монет
    async def my_assets(self) -> dict: ...

    # base_url = 'https://p2p.walletbot.me'
    # middle_url = '/p2p/'

    # 6: Отмена сделки
    async def cancel_order(self, orderId: int):
        data = {"orderId": orderId}
        cancel = await self._post("/p2p/public-api/v2/offer/order/cancel/by-buyer", json=data)
        return cancel

    # 15 - order_approve
    async def order_approve(self, order_id: int, typ: str):
        approve = await self._post("/p2p/public-api/v2/offer/order/accept", {"orderId": order_id, "type": typ})
        return approve

    # 16 - order_reject
    async def order_reject(self, order_id: str):
        reject = await self._post("/p2p/public-api/v2/offer/order/cancel/by-seller", {"orderId": order_id})
        return reject

    async def upload_file(self, order_id: int, path_to_file: str):
        url = f"public-api/v2/file-storage/file/upload?orderId={order_id}&uploadType=UPLOAD_BUYER_PAYMENT_RECEIPT"
        data = {"file": open(path_to_file, "rb")}
        upload_file = await self._post(url, data)
        return upload_file

    # 19 - order_paid
    async def order_paid(self, order_id: str, file: dict):
        paid = await self._post(
            "/p2p/public-api/v2/offer/order/confirm-sending-payment", {"orderId": order_id, "paymentReceipt": file}
        )
        return paid

    # 20 - order_payment_confirm
    async def order_payment_confirm(self, order_id: str):
        payment_confirm = await self._post("/p2p/public-api/v2/payment-details/confirm", {"orderId": order_id})
        return payment_confirm
