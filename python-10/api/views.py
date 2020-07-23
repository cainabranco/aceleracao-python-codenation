from collections import Counter

from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['POST'])
def lambda_function(request):
    request_data = request.data.get('question')

    counter = Counter()
    for number in request_data:
        counter[number] += 1

    solution = []
    for i in counter.most_common():
        for _ in range(i[1]):
            solution.append(i[0])

    return Response({'solution' : solution})