class Faq(models.Model):

    GENERAL = '일반'
    ACCOUNT = '계정'
    ETC = '기타'

    CATEGORY_CHOICES = [
        (GENERAL, '일반'),
        (ACCOUNT, '계정'),
        (ETC, '기타'),
    ]
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=0,
    )

    def is_upperclass(self):
        return self.category in {self.GENERAL, self.ETC}

    quest      = models.CharField('질문', max_length=126, null=False)
    answer     = models.TextField('답변', null=False)
    auther     = models.CharField('생성자', max_length=16, null=False)
    created_at = models.DateTimeField('생성일시', auto_now_add=True)
