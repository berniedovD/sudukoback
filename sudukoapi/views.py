from django.shortcuts import render

from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response  import Response

def say_hello(request):
    
    return HttpResponse("Hello World")
@api_view()
def puzzles(request):
    puzList = [
       {"id": "puzzleID1",
        "puzzleString": "010020300004005060070000008006900070000100002030048000500006040000800106008000000"},
       {"id": "p2",
        "puzzleString": "000123000040050060000000000100000003260070081900000002000000000080060040000294000"},
       {"id": "p3",
        "puzzleString": "000943000060010050000000000800000003750060014100000009000000000020050080000374000"},
       {"id": "p4",
        "puzzleString": "1111123000040050060000000000100000003260070081900000002000000000080060040000294000"},
       {"id": "p5",
        "puzzleString": "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......"}
    ]


    return Response(puzList)


