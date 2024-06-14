"""
Views for the recipe APIs.
"""
from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from core.models import (
    Recipe,
    Tag,
    Ingredient
)
from recipe import serializers


# ModelViewSet is a class that has bases:
# - mixins.CreateModelMixin
# - mixins.RetrieveModelMixin
# - mixins.UpdateModelMixin
# - mixins.DestroyModelMixin
# - mixins.ListModelMixin
# - GenericViewSet
class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    # This docstring above is directly translated to the online
    # swagger documentation of the API
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for auth user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request"""
        return (
            serializers.RecipeSerializer
            if self.action == "list"
            else self.serializer_class
        )

    def perform_create(self, serializer):
        """ Create a new recipe"""
        serializer.save(user=self.request.user)


class BaseRecipeAttrViewSet(mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to auth user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')


# This is an explicit way of specifying the required operations
class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database"""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()


class IngredientViewSet(BaseRecipeAttrViewSet):
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()
