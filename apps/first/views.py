from rest_framework.views import APIView
from apps.first.models import Vacancy, Company, Resume
from rest_framework.response import Response


class CountAPIView(APIView):

    def get(self, request):
        vacancy_count = Vacancy.objects.all().count()
        company_count = Company.objects.all().count()
        resume_count = Resume.objects.all().count()
        data = [
            {
                "vacancy_count": vacancy_count,
                 "company_count": company_count,
                 "resume_count": resume_count
             },
        ]
        return Response(data)

