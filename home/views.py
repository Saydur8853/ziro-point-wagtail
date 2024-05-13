# from .models import Newsletter
# from .serializers import NewsletterSerializer
# from rest_framework.generics import CreateAPIView

# class NewsLetterSubscriptionCreateView(CreateAPIView):
#     model = Newsletter
#     serializer_class = NewsletterSerializer



from rest_framework.response import Response
from rest_framework import status
from validate_email import validate_email

from .models import Newsletter
from .serializers import NewsletterSerializer
from rest_framework.generics import CreateAPIView

class NewsLetterSubscriptionCreateView(CreateAPIView):
    model = Newsletter
    serializer_class = NewsletterSerializer

    def perform_create(self, serializer):
        email = serializer.validated_data['email']

        # Validate email using validate_email library
        is_valid = validate_email(email, verify=True)
        print(f"is_valid: {is_valid}")  # Print the result of validation

        if is_valid is None:
            return Response({'error': 'Email validation inconclusive'})
        elif not is_valid:
            return Response({'error': 'Invalid email address'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the email already exists in the database
        if Newsletter.objects.filter(email=email).exists():
            return Response({'error': 'Email already subscribed'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)