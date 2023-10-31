from django.http import HttpResponse

def create(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    name = data.get['name']
    email = data.get['email']
    phone = data.get['phone']

def get(request):
  user_id = request.GET.get('user_id', '')
  return HttpResponse("Hello, get user of " + user_id + ".")