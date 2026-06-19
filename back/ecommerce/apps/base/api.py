from rest_framework import generics


class GeneralListAPIView(generics.ListAPIView):
    """General ListAPIView"""

    serializer_class = None

    def get_queryset(self):
        """Custom queryset from meta model"""

        model = self.get_serializer().Meta.model
        return model.objects.filter(state=True)
