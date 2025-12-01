from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.serializers import JobSerializer, ResumeSerializer, ApplicationSerializer
from core.models import Job, Resume, Application
from agents.coordinator import CoordinatorAgent
from django.contrib.auth.models import User
from rest_framework import status

@api_view(['GET'])
def jobs_list(request):
    jobs = Job.objects.all()
    return Response(JobSerializer(jobs, many=True).data)

@api_view(['POST'])
def agent_endpoint(request):
    '''
    Expects JSON:
    {
      "type": "job"|"resume"|"interview"|"apply",
      "input": <depends on type>
    }
    '''
    payload = request.data
    req_type = payload.get('type')
    input_data = payload.get('input')
    coord = CoordinatorAgent()
    result = coord.handle(req_type, input_data, user=request.user if request.user.is_authenticated else None)
    return Response({'result': result})

@api_view(['POST'])
def create_job(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
