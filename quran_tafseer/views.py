# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from .serializers import TafseerSerializer, TafseerTextSerializer
from .models import Tafseer, TafseerText


class TafseerView(generics.ListAPIView):
    serializer_class = TafseerSerializer
    queryset = Tafseer.objects.all()


class AyahTafseerView(generics.RetrieveAPIView):
    serializer_class = TafseerTextSerializer

    def get_object(self):
        tafseer_id = self.kwargs['tafseer_id']
        sura_id = self.kwargs['sura_id']
        ayah_num = self.kwargs['ayah_numb']
        return TafseerText.objects.get_ayah_tafseer(tafseer_id,
                                                    sura_id,
                                                    ayah_num)


class AyahRangeTafseerView(generics.ListAPIView):
    serializer_class = TafseerTextSerializer

    def get_queryset(self):
        ayah_from_num = self.kwargs['ayah_from_num']
        ayah_to_num = self.kwargs['ayah_to_num']
        sura_id = self.kwargs['sura_id']
        tafseer_id = self.kwargs['tafseer_id']
        return TafseerText.objects.get_ayah_tafseer_range(tafseer_id,
                                                          sura_id,
                                                          ayah_from_num,
                                                          ayah_to_num)
