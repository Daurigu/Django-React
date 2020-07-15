from django.shortcuts import render, redirect
from django.http import JsonResponse
from tweets.models import TweetModel
from django.utils.http import is_safe_url
from django.conf import settings

from rest_framework.response  import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes , permission_classes

from .forms import TweetForm
from tweets.serializers import TweetSerializer, ActionSerializer
# Create your views here.



ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def home_view(request):
    
    if request.user.is_authenticated:

        context={

        }

        return render(request, 'pages/home.html', context)
    else:
        #return render(request, 'components/noexstence.html', {})
        return redirect('/')



def tweet_list_view(request):
    qs = TweetModel.objects.all()
    tweet_list = [{'id':x.id, 'content':x.content} for x in qs]
    data = {
        'response': tweet_list
    }
    return JsonResponse(data)



@api_view(['POST'])
#@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def tweet_create_view(request):
    serializer = TweetSerializer(data = request.POST)
    if serializer.is_valid(raise_exception = True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)

    return Response({}, status=400)




@api_view(['GET'])
def tweet_view(request):
    qs = TweetModel.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def tweet_detail_view(request, id):
    qs = TweetModel.objects.filter(id=id)
    if not qs.exists():
        return Response({}, status=404)
    
    serializer = TweetSerializer(qs, many=True)
    
    return Response(serializer.data, status=200)




@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, id):

    qs = TweetModel.objects.filter(id=id)
    if not qs.exists():
        return Response({}, status=404)

    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({'message': 'Unauthorised User'}, status=401)

    obj = qs.first()
    obj.delete()
        
    return Response({{'message': 'Tweet Deleted'}}, status=200)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_actions_view(request):

    serializer = ActionSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        id = data.get('id')
        action = data.get('action')
        
        qs = TweetModel.objects.filter(id=id)
        if not qs.exists():
            return Response({}, status=404)

        qs = qs.filter(user=request.user)
        if not qs.exists():
            return Response({'message': 'Unauthorised User'}, status=401)

        obj = qs.first()
        if action == 'unlike':
            obj.likes.remove(request.user)
        elif action == 'like':
            obj.likes.add(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer, status=200)
        elif action == 'retweet':
            retweet_act = TweetModel.objects.create(user=request.user, parent=obj)
            serializer = TweetSerializer(retweet_actS)
            return Response(serializer, status=200)

                
    return Response({}, status=200)



# --------------------
# VANILLA DJANGO VIEWS
# --------------------


def tweet_create_view_vanilla(request):

    if request.user.is_authenticated:

        form = TweetForm(request.POST or None)
        safeLink = request.POST.get("next") or None

        if form.is_valid():
            obj = form.save(commit= False)
            obj.save()
            print('------------\n SAVED \n ------------')
            if safeLink != None and is_safe_url(safeLink, ALLOWED_HOSTS):
                return redirect(safeLink)
            else:
                return redirect('../')

        context ={
            'form': form
        }

        return render(request, 'components/form.html', context)
    else:
        return render(request, 'components/noexstence.html', {})




def tweet_view_django(request, id):

    data = {
        'id': id,
    }
 
    status = 200

    try:
        obj = TweetModel.objects.get(id=id)
        data['content'] = obj.content
    except:
        data['message'] = 'NOT FOUND'
        status = 404


    return JsonResponse(data, status=status)