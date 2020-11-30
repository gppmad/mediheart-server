from rest_framework.views import APIView
from rest_framework.response import Response
import logging

class TestLog(APIView):
    
    #GET OBJECT WITH ID
    def get(self, request, id=""):

        # Get an instance of a logger
        logger = logging.getLogger(__name__)    
        logger.info("test")
        #logger.error("error test")
        return Response("hello", status=500)