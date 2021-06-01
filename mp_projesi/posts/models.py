from django.db import models

# Create your models here.

class Post(models.Model): # mesaj panelinde gönderi içeriğini saklamak için b, model oluşturmaya çalışalım
    text = models.TextField()
    # Burada Şuan veri tabanında text alanına sahip post isminde bir veritabanu modeli oluşturmuş olduk
    # her ne zaman bir model oluşturur yada modifiye edersek 2 adımda django yu güncellemek gerekir
    # ilk olarak makemagretions sonra migrat
    # makemagretions ile bi magretions dosyası oluşturulur böylece Insttal Ap kısmında yüklü appler için sqllite komutları üretilir.
    # migrate komutu ile asıl veri tabanını kuracağız ve böylece migrations dosyasındaki bilgiler çalışacak
    # yani kısaca modeli veri tabanına taşımak için migrate komutu kullanılır.
    def __str__(self):
        return self.text[:40] # bu str fonk textteki ilk 40 karakteri döndürsün yani postobject yazmak yerine yazdıklarımı göstersin