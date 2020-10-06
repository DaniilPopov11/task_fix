from django.db import models

class third_party(models.Model):
    first_name = models.CharField('first_name', max_length=128)
    last_name = models.CharField('last_name', max_length=128)
    patronymic = models.CharField('patronymic', max_length=128, blank=True)
    birth_date = models.DateField('birth_date')

    def __str__(self):
        return self._check_column_name_clashes()

class accounts(models.Model):
    third_party = models.ForeignKey(third_party, on_delete=models.CASCADE)
    account_number = models.CharField('account_number', max_length=512)
    start_date = models.DateField('start_date')
    end_date = models.DateField('end_date')

    def __str__(self):
        return self.account_number()