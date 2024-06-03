from rest_framework import serializers
from .models import Card
import re

class CardSerializer(serializers.ModelSerializer):
    card_number = serializers.CharField(write_only=True)
    ccv = serializers.CharField(write_only=True)

    class Meta:
        model = Card
        fields = ['id', 'user', 'title', 'censored_number', 'is_valid', 'card_number', 'ccv']
        read_only_fields = ['censored_number', 'is_valid']
        extra_kwargs = {'user': {'read_only': True}}

    def validate_card_number(self, value):
        if not re.fullmatch(r'\d{16}', value):
            raise serializers.ValidationError("Card number must be 16 digits.")
        return value

    def validate_ccv(self, value):
        if not 100 <= int(value) <= 999:
            raise serializers.ValidationError("CCV must be between 100 and 999.")
        return value

    def create(self, validated_data):
        card_number = validated_data.pop('card_number')
        ccv = validated_data.pop('ccv')
        validated_data['censored_number'] = card_number[:4] + '*'*8 + card_number[-4:]
        validated_data['is_valid'] = self.validate_card_validity(card_number, int(ccv))
        validated_data['user'] = self.context['request'].user  # Assign the user from the request context
        return super().create(validated_data)

    def validate_card_validity(self, card_number, ccv):
        pairs = [(int(card_number[i:i+2]), int(card_number[i+2:i+4])) for i in range(0, 16, 4)]
        return all((x ** (y**3) % ccv) % 2 == 0 for x, y in pairs)
