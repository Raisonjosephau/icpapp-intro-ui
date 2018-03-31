from rest_framework import serializers
from .models import ProductCatalogue,Product, DataTable
import datetime
import time
class CreateProductCatalogueSerializer(serializers.ModelSerializer):

    class Meta:
       model = ProductCatalogue
       fields = '__all__'


class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class UpdateProductSerializer(serializers.ModelSerializer):
    pcatid = serializers.IntegerField()

    class Meta:
        model = Product
        fields=('pcatid','price','priceType','date','remarks',)


    def create(self, validated_data):
        pcatid = validated_data["pcatid"]
        price = validated_data["price"]
        priceType = validated_data["priceType"]
        date = validated_data["date"]
        remarks = validated_data["remarks"]
        pcat = ProductCatalogue.objects.get(pk=pcatid)
        pcs = Product.objects.filter(user=self.context['request'].user,pcatid=pcatid)
        currentmonth=datetime.datetime.fromtimestamp(int(round(time.time() * 1000)) / 1000.0).month
        currentyear =datetime.datetime.fromtimestamp(int(round(time.time() * 1000)) / 1000.0).year
        print(currentmonth)
        print(currentyear)
        flag =0
        for pc in pcs:
            print(pc)
            month =datetime.datetime.fromtimestamp(pc.date / 1000.0).month
            year = datetime.datetime.fromtimestamp(pc.date/1000.0).year
            print(month)
            print(year)
            if currentmonth==month and currentyear==year:
                pc.date = date
                pc.priceType = priceType
                pc.price = price
                pc.remarks = remarks
                pc.save()


        if not pcs:
            p = Product(productCatalogue=pcat, pcatid=pcatid, price=price, priceType=priceType, date=date,
                        remarks=remarks, user=self.context['request'].user)
            p.save()
        return validated_data



class CreateDataTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataTable
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields='__all__'


class ProductCatalogueSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True,read_only=True)

    class Meta:
        model = ProductCatalogue
        fields=["id","code","itemName","previousPrice","SDP","PDC","image","products"]
        read_only_fields = ('id',)


class ListFullProducts(serializers.ModelSerializer):
    catalogues = ProductCatalogueSerializer(many=True,read_only=True)

    class Meta:
        model = DataTable
        fields =["phase","tableid","category","catalogues"]