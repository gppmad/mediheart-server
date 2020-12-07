import json
import logging
from rest_framework.views import APIView
from rest_framework.response import Response


class TestLog(APIView):
    
    #GET OBJECT WITH ID
    def get(self, request, id=""):

        array_data = json.loads(request.body)

        # Get an instance of a logger
        logger = logging.getLogger(__name__)    
        logger.error("error for user " + str(array_data[0]))
        return Response("log handled ! ",status=500)