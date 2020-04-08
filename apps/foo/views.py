import logging

from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.generic.base import View
from .models import VisitLogModel
# Create your views here.

logger = logging.getLogger("dbloger").getChild(__name__)


class IndexView(View):
    logger = logger.getChild("IndexView")

    def get(self, request, *args, **kwargs):
        """
        """
        logger = self.logger.getChild("get")
        logger.info("start")

        vlm = VisitLogModel(http_url=request.path)
        vlm.save()

        logger.info("complete")
        return JsonResponse({'pk': vlm.id})
