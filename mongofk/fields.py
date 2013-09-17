from django.db.models import Model, get_model
from django.utils import six

from mongoengine.base import BaseField


class ForeignKey(BaseField):
    """A reference to a Django model that will be automatically dereferenced on
    access (lazily)."""

    def __init__(self, model, **kwargs):
        if not isinstance(model, six.string_types):
            if not issubclass(model, (Model, six.string_types)):
                self.error(
                    'Argument to ForeignKey constructor must be a Django model '
                    'class or a string')

        self.model_obj = model

        super(ForeignKey, self).__init__(**kwargs)

    @property
    def model(self):
        if isinstance(self.model_obj, six.string_types):
            self.model_obj = get_model(*self.model_obj.split('.'))

        return self.model_obj

    def to_mongo(self, model_obj):
        id_ = model_obj.pk
        if id_ is None:
            self.error(
                'You can only reference objects once they have been save to '
                'the database')

        return id_

    def to_python(self, value):
        return self.model.objects.get(pk=value)

    def prepare_query_value(self, op, value):
        if value is None:
            return None

        return self.to_mongo(value)

    def validate(self, value):
        if not isinstance(value, self.model_obj):
            self.error('A ForeignKey only accepts Django objects')

        if isinstance(value, Model) and value.id is None:
            self.error(
                'You can only reference Django objects once they have been '
                'saved to the database')

    def lookup_member(self, member_name):
        return self.model_obj._fields.get(member_name)
