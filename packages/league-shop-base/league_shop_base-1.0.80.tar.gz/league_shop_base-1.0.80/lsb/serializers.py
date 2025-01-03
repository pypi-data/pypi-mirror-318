"""Serializers module"""

from rest_framework import serializers  # type: ignore

from .models import Champion
from .models import Product
from .models import Skin


class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = ["id", "name", "roles", "lanes"]


class SkinSerializer(serializers.ModelSerializer):
    """SkinSerializer class"""

    champion = serializers.CharField(source="champion.name")
    lanes = serializers.CharField(source="champion.lanes")
    roles = serializers.CharField(source="champion.roles")

    class Meta:
        model = Skin
        fields = ["id", "name", "champion", "tier", "value", "lanes", "roles"]


class ProductSerializer(serializers.ModelSerializer):
    """ProductSerializer class"""

    level = serializers.IntegerField(source="discrete_level")
    blue_essence = serializers.IntegerField(source="discrete_blue_essence")
    skins = serializers.SlugRelatedField(
        slug_field="name", many=True, read_only=True
    )
    owned_skins = serializers.SlugRelatedField(
        slug_field="name", many=True, read_only=True
    )
    permanent_skins = serializers.SlugRelatedField(
        slug_field="name", many=True, read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "level",
            "blue_essence",
            "orange_essence",
            "mythic_essence",
            "region",
            "skins",
            "owned_skins",
            "permanent_skins",
            "rank",
            "division",
            "is_current_season_rank",
            "is_handleveled",
            "is_bare_metal",
            "quickplay_wins",
            "quickplay_losses",
            "date_last_played",
        ]


class ProductUploadSerializer(serializers.ModelSerializer):
    """ProductUploadSerializer class"""

    skins = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Skin.objects.all()
    )
    permanent_skins = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Skin.objects.all()
    )
    owned_skins = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Skin.objects.all()
    )

    class Meta:
        model = Product
        fields = [
            "username",
            "password",
            "summoner_name",
            "level",
            "blue_essence",
            "orange_essence",
            "mythic_essence",
            "region",
            "country",
            "is_safe",
            "is_handleveled",
            "is_bare_metal",
            "rank",
            "division",
            "flash_key",
            "solo_wins",
            "solo_losses",
            "skins",
            "permanent_skins",
            "owned_skins",
            "email",
            "date_sign_up",
            "dob",
            "ip_address",
            "city",
            "disabled_until",
            "is_auth_error",
            "is_banned",
            "ban_reason",
            "status",
            "remarks",
            "uploaded_by",
            "date_checked",
            "date_last_played",
        ]


class PurchasedProductSerializer(serializers.ModelSerializer):
    """PurchasedProductSerializer class"""

    level = serializers.IntegerField(source="discrete_level")
    blue_essence = serializers.IntegerField(source="discrete_blue_essence")
    is_premium = serializers.BooleanField(source="is_bare_metal")
    skins = serializers.SlugRelatedField(
        slug_field="name", many=True, read_only=True
    )
    owned_skins = serializers.SlugRelatedField(
        slug_field="name", many=True, read_only=True
    )
    permanent_skins = serializers.SlugRelatedField(
        slug_field="name", many=True, read_only=True
    )

    class Meta:
        model = Product
        fields = [
            "username",
            "password",
            "level",
            "blue_essence",
            "orange_essence",
            "mythic_essence",
            "region",
            "skins",
            "owned_skins",
            "permanent_skins",
            "is_safe",
            "is_handleveled",
            "is_premium",
            "rank",
            "division",
            "is_current_season_rank",
            "flash_key",
            "solo_wins",
            "solo_losses",
            "date_last_played",
        ]
