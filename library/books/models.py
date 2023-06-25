from django.db import models


class Book(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    author = models.CharField("Автор", max_length=255, blank=True, null=True)
    quantity = models.IntegerField("Количество")

    def __str__(self):
        return f"{self.title}, {self.author}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Reader(models.Model):
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return " ".join((self.last_name, self.first_name))

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"


class Status(models.TextChoices):
    RESERVED = "RES", "Reserved"
    RETURNED = "RET", "Returned"


class Reservation(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.PROTECT, related_name="reserved"
    )
    reader = models.ForeignKey(
        Reader, on_delete=models.PROTECT, related_name="reader_items"
    )
    status = models.CharField(
        choices=Status.choices, default=Status.RESERVED, max_length=10
    )
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book} на руках у {self.reader}"

    class Meta:
        verbose_name = "Резервирование"
        verbose_name_plural = "Резервирование"
