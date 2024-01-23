from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
         """
        Returns true if the user is the creator of the comment
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
         """
        Returns a human readable time since the
        comment was created
        eg. '2 days ago'
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
         """
        Returns a human readable time since the
        comment was updated
        eg. '15 minutes ago'
        """
        return naturaltime(obj.updated_at)

    class Meta:
        """
        Lists all the filds to be included in
        the data returned by this api
        """
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')