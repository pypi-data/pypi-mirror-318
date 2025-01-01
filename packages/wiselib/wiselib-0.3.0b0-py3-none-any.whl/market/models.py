from typing import Any

from django.core.exceptions import ValidationError
from django.db import models, transaction, IntegrityError

from market.utils import ExactlyOneNonNullConstraint
from wise.utils.models import BaseModel


class Symbol(BaseModel):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, unique=True)

    def get_or_create_asset(self) -> "Asset":
        try:
            with transaction.atomic():
                return Asset.objects.get_or_create(type=Asset.Type.SYMBOL, symbol=self)[
                    0]
        except IntegrityError:
            return Asset.objects.get(type=Asset.Type.SYMBOL, symbol=self)

    def __str__(self) -> str:
        return self.name


class Pair(BaseModel):
    slug = models.CharField(max_length=256, unique=True)
    base = models.ForeignKey(Symbol, on_delete=models.CASCADE,
                             related_name="base_pairs")
    quote = models.ForeignKey(Symbol, on_delete=models.CASCADE,
                              related_name="quote_pairs")
    name = models.CharField(max_length=256)

    def save(self, *args, **kwargs):
        self.name = f"{self.base.name}{self.quote.name}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    @property
    def assets(self) -> list["Asset"]:
        return list(
            filter(
                lambda asset: asset,  # type: ignore
                [Asset.objects.filter(pair=self).first(),
                 Asset.objects.filter(symbol=self.base).first()],
            )
        )

    def get_or_create_asset(self) -> "Asset":
        try:
            with transaction.atomic():
                return Asset.objects.get_or_create(type=Asset.Type.PAIR, pair=self)[0]
        except IntegrityError:
            return Asset.objects.get(type=Asset.Type.PAIR, pair=self)

    class Meta(BaseModel.Meta):
        unique_together = ["base", "quote"]


class Asset(BaseModel):
    class Type(models.TextChoices):
        SYMBOL = "SYMBOL", "SYMBOL"
        PAIR = "PAIR", "PAIR"

    type = models.CharField(max_length=32, choices=Type.choices)
    symbol = models.OneToOneField(Symbol, on_delete=models.CASCADE, blank=True,
                                  null=True)
    pair = models.OneToOneField(Pair, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def slug(self) -> str:
        match self.type:
            case Asset.Type.SYMBOL:
                assert self.symbol
                return self.symbol.slug
            case Asset.Type.PAIR:
                assert self.pair
                return self.pair.slug
            case _:
                return self.type

    def __str__(self) -> str:
        match self.type:
            case Asset.Type.SYMBOL:
                return self.symbol.__str__()
            case Asset.Type.PAIR:
                return self.pair.__str__()
            case _:
                return self.type

    def clean(self, *args: Any, **kwargs: Any) -> None:
        super().clean()

        is_valid_symbol = self.type == Asset.Type.SYMBOL and self.symbol and not self.pair
        is_valid_pair = self.type == Asset.Type.PAIR and self.pair and not self.symbol
        is_valid = is_valid_symbol or is_valid_pair

        if not is_valid:
            raise ValidationError("Invalid asset fields")

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta(BaseModel.Meta):
        unique_together = ["type", "symbol", "pair"]
        constraints = [ExactlyOneNonNullConstraint(fields=["symbol", "pair"])]


class Market(BaseModel):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.name


class Exchange(BaseModel):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self) -> str:
        return self.name


class ExchangeMarket(BaseModel):
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.exchange.name}-{self.market.name}"

    class Meta(BaseModel.Meta):
        unique_together = ["exchange", "market"]


class ExchangeMarketPairBinding(BaseModel):
    exchange_market = models.ForeignKey(ExchangeMarket, on_delete=models.CASCADE,
                                        related_name="pair_bindings")
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE,
                             related_name="exchange_market_bindings")
    price_decimals = models.IntegerField()
    quantity_decimals = models.IntegerField()
    price_step_size = models.FloatField()
    quantity_step_size = models.FloatField()
    min_notional = models.FloatField()

    class Meta(BaseModel.Meta):
        unique_together = ["exchange_market", "pair"]


class Network(BaseModel):
    name = models.CharField(max_length=256, unique=True, db_index=True)
    slug = models.CharField(max_length=256, unique=True)

    def get_native_symbol(self) -> "Symbol":
        return self.symbol_bindings.get(type=NetworkSymbolType.NATIVE_COIN).symbol


class NetworkSymbolType(models.TextChoices):
    NATIVE_COIN = "COIN", "Native Coin"
    UTILITY_TOKEN = "TOKEN", "Utility Token"


class NetworkSymbolBinding(BaseModel):
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE,
                               related_name="network_bindings", db_index=True)
    network = models.ForeignKey(Network, on_delete=models.CASCADE,
                                related_name="symbol_bindings", db_index=True)

    decimals = models.IntegerField(default=18)
    step_size = models.FloatField(default=1e-18)

    type = models.CharField(
        max_length=64,
        choices=NetworkSymbolType.choices,
        default=NetworkSymbolType.UTILITY_TOKEN,
        db_index=True,
    )

    def save(self, *args, **kwargs):
        if self.decimals:
            self.step_size = 10 ** -self.decimals
        super().save(*args, **kwargs)

    class Meta(BaseModel.Meta):
        unique_together = ["symbol", "network"]
        constraints = [
            models.UniqueConstraint(
                "network",
                "symbol",
                name="network_symbol_binding_unique_network_symbol",
            ),
            models.UniqueConstraint(
                fields=["network"],
                condition=models.Q(type=NetworkSymbolType.NATIVE_COIN),
                name="network_symbol_binding_unique_network_native_coin",
            ),
        ]
