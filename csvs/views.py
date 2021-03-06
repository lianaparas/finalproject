import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import Location

# Create your views here.

#one parameter named request
def file_upload(request):
	template = "csv_upload.html"
	data	 = Location.objects.all()

	#prompt is a context variable that can have different values depending on their context
	#prompt = {
	#'order'	: 'Order of the csv should be created_at,place,locat,lat,lon',
	#'file'  : data
	#}

	# GET request returns the value of the data with the specified key.
	if request.method == "GET":
		return render(request, template)
	csv_file = request.FILES['file']
    
    # let's check if it is a csv file
	if not csv_file.name.endswith('.csv'):
		messages.error(request, 'THIS IS NOT A CSV FILE')
	data_set = csv_file.read().decode('UTF-8')
  
	# setup a stream which is when we loop through each line we are able to handle a data in a stream
	io_string = io.StringIO(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',', quotechar="|"):
		_, created = Location.objects.update_or_create(
    	locat=column[0],
    	total=column[1]
    )
	
	return render(request, template, {})

