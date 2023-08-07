from ...utils.models import BaseModel, models
from ...apps.users.models import User

# Create your models here.


class Consumption(BaseModel):
    # 真正在数据库中的字段实际上叫 category_id，而category则代表了关联的哪个分类模型对象
    consumption_time = models.DateTimeField(verbose_name="消费日期")
    category = models.CharField(blank=True, null=True, max_length=10, verbose_name='消费类别')
    consumption_way = models.CharField(verbose_name='交易方式')
    is_necessary = models.BooleanField(default=True, verbose_name='是否必需')
    amount = models.FloatField(verbose_name='消费金额')

    class Meta:
        db_table = "consumption"
        verbose_name = "消费信息"
        verbose_name_plural = verbose_name

