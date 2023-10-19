

from rest_framework import serializers


class InterfacesSerilizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    tester = serializers.CharField()

    projects = serializers.PrimaryKeyRelatedField()
