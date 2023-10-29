from .models import Transfer,FromWhere,ToWhere,Car,Extras,Blog
from modeltranslation.translator import TranslationOptions,register


@register(FromWhere)
class FromWhereTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(ToWhere)
class ToWhereTranslationOptions(TranslationOptions):
    fields = ("name",)

@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields=("name","fromwhere","towhere","capasity")

@register(Transfer)
class TransferTranslationOptions(TranslationOptions):
    fields=("fromwhere","towhere")

@register(Extras)
class ExtrasTranslationOptions(TranslationOptions):
    fields = ("name","price")

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ("title","content")