from django.db import models


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, null=True)
    contract_number = models.CharField(max_length=16, unique=True, null=True)

    class Meta:
        db_table = 'company'

    def __str__(self):
        return str(self.name)


class Contract(models.Model):
    contract_number = models.CharField(max_length=16, primary_key=True)
    contract_date = models.DateTimeField(null=True)
    contractor = models.CharField(max_length=20, blank=True)
    shipping_company = models.CharField(max_length=40, blank=True)
    customer_company = models.CharField(max_length=40, blank=True)
    departure_address = models.CharField(max_length=80, blank=True)
    arrival_address = models.CharField(max_length=80, blank=True)

    class Meta:
        db_table = 'contract'

    def __str__(self):
        return str(self.contract_number)


class Package(models.Model):
    contract_number = models.ForeignKey(Contract, on_delete=models.CASCADE, db_column='contract_number', null=True, related_name='packages')
    package_number = models.CharField(max_length=16, primary_key=True)
    package_name = models.CharField(max_length=100, blank=True)
    quantity = models.IntegerField(null=True)

    class Meta:
        managed = False
        db_table = 'package'



class PackageLog(models.Model):
    package_number = models.CharField(max_length=16, primary_key=True)
    time = models.DateTimeField(null=False)
    temperature = models.FloatField(null=True)
    humidity = models.IntegerField(null=True)
    shipping_stage = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'package_log'
        unique_together = (('package_number', 'time'),)  # 이 부분은 두 필드를 함께 기본 키로 설정하는 것을 의미합니다.

    def __str__(self):
        return f"{self.package_number} - {self.time}"

