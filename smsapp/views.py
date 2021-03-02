from django.shortcuts import render, Http404
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET','POST','PUT','DELETE'])
def stuop(request, id=None):
	if request.method=="GET":
		if id is None:
			result= StudentModel.objects.all()
			sresult= StudentSerializer(result, many=True)
			return Response(sresult.data)
		else:
			try:
				result= StudentModel.objects.get(rno=id)
				sresult= StudentSerializer(result)
				return Response(sresult.data)
			except StudentModel.DoesNotExist:
				raise Http404

	elif request.method == "POST":
		stu= StudentSerializer(data=request.data)
		if stu.is_valid():
			stu.save()
			return Response({'msg':'student added'})
		else:
			return Response(stu.errors)

	elif request.method == "PUT":
		try:
			stu= StudentModel.objects.get(rno=id)
			save_stu= StudentSerializer(stu, data=request.data, partial=True)
			if save_stu.is_valid():
				save_stu.save()
				return Response({'msg':'record updated'})
			else:
				return Response(save_stu.errors)
		except StudentModel.DoesNotExist:
			raise Http404
	elif request.method == "DELETE":
		try:
			stu= StudentModel.objects.get(rno=id)
			stu.delete()
			return Response({'msg':'record delted'})
		
		except StudentModel.DoesNotExist:		
			raise Http404






