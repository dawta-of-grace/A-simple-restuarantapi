from rest_framework import serializers
from .models import MenuItem, Order
from django.contrib.auth.models import User


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
     model = MenuItem
     fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only = True)
    item_ids = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all(), many=True, write_only =True)

    class Meta: 
      model = Order
      fields = ['id','ordered_at', 'user', 'items','item_ids']
      read_only_fields =['user']

    def create(self, validated_data):
       items = validated_data.pop('item_ids')
       user=self.context['request'].user if 'request' in self.context else None
       validated_data.pop('user', None)
       order = Order.objects.create(user=user, **validated_data)
       order.items.set(items)
       return order 
    
class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ['username', 'password']
      extra_kwargs = {'password': {'write_only':True}}

    
       
