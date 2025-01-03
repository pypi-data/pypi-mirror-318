from typing import Any
from typing import List
from typing import Tuple

from django.contrib import admin
from django.db.models import Q
from django.db.models import QuerySet
from django.http import HttpRequest
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from lsb.constants import OLD_STOCK_THRESHOLD


class AccountTypeListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("account type")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "type"

    def lookups(
        self, request: HttpRequest, model_admin: Any
    ) -> List[Tuple[str, str]]:
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """

        return [
            ("unranked", "Unranked"),
            ("ranked", "Ranked"),
            ("handleveled", "Handleveled"),
        ]

    def queryset(self, request: HttpRequest, queryset: QuerySet[Any]):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """

        if self.value() is None:
            return queryset

        account_type = self.value()
        if account_type == "unranked":
            queryset = queryset.filter(
                Q(rank="UNRANKED"),
                is_handleveled=False,
            )
        elif account_type == "handleveled":
            queryset = queryset.filter(is_handleveled=True)
        elif account_type == "ranked":
            queryset = queryset.exclude(rank="UNRANKED")
        elif account_type == "baremetal":
            queryset = queryset.filter(is_baremetal=True)
        return queryset


class IsDisabledFilter(admin.SimpleListFilter):
    title = _("is disabled")
    # Parameter for the filter that will be used in the URL query.
    parameter_name = "is_disabled"

    def lookups(
        self, request: HttpRequest, model_admin: Any
    ) -> List[Tuple[str, str]]:
        return [
            ("yes", "Yes"),
            ("no", "No"),
        ]

    def queryset(self, request: HttpRequest, queryset: QuerySet[Any]):
        if self.value() is None:
            return queryset
        if self.value() == "yes":
            queryset = queryset.filter(disabled_until__gte=timezone.now())
        elif self.value() == "no":
            queryset = queryset.filter(disabled_until__lt=timezone.now())
        return queryset


class ValidAcccountFilter(admin.SimpleListFilter):
    title = _("is valid/purchasable")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "is_valid"

    def lookups(
        self, request: HttpRequest, model_admin: Any
    ) -> List[Tuple[str, str]]:
        return [
            ("yes", "Yes"),
            ("no", "No"),
        ]

    def queryset(self, request: HttpRequest, queryset: QuerySet[Any]):
        if self.value() is None:
            return queryset

        valid_account_filter = {
            "is_purchased": False,
            "is_banned": False,
            "is_auth_error": False,
            "disabled_until__lt": timezone.now(),
        }

        if self.value() == "yes":
            queryset = queryset.filter(**valid_account_filter)
        elif self.value() == "no":
            queryset = queryset.exclude(**valid_account_filter)
        return queryset


class OldStockFilter(admin.SimpleListFilter):
    title = _("is old stock")
    # Parameter for the filter that will be used in the URL query.
    parameter_name = "is_old_stock"

    def lookups(
        self, request: HttpRequest, model_admin: Any
    ) -> List[Tuple[str, str]]:
        return [
            ("yes", "Yes"),
            ("no", "No"),
        ]

    def queryset(self, request: HttpRequest, queryset: QuerySet[Any]):
        if self.value() is None:
            return queryset

        old_stock_filter = Q(date_last_played__isnull=False) & Q(
            date_last_played__date__lte=OLD_STOCK_THRESHOLD
        )

        if self.value() == "yes":
            queryset = queryset.filter(old_stock_filter)
        elif self.value() == "no":
            queryset = queryset.exclude(old_stock_filter)
        return queryset
