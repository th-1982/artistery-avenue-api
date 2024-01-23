from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Serializer for the currently logged in user
    """   
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """
        Lists what aditional fields are returned
        along with the userdtails
        """
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )