import os
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import UserSerializer, UserProfileSerializer, UserExperienceSerializer, UserProjectSerializer, UserSkillSerializer, UserCertificateSerializer, UserLinkSerializer
from .models import UserProfile, UserExperience, UserProject, UserSkill, UserCertificate, UserLink
from django.contrib.auth.models import User


# Create your views here.


# >>>   SIGNUP VIEWS HERE
@api_view(['POST'])
def Signup(request):
    try:
        if User.objects.filter(username=request.data['username']):
            return JsonResponse(status=406, data={'message': 'Username already exists!'}, safe=False)
        else:
            user = User.objects.create_user(
                username=request.data['username'], email=request.data['email'], password=request.data['password'])
            user.save()
            refresh = RefreshToken.for_user(user)
            return JsonResponse(status=200, data={'message': 'user was successfully created!', 'refresh': str(refresh), 'access': str(refresh.access_token)}, safe=False)
    except:
        return JsonResponse(status=406, data={'message': 'Entry Was Not Registered!'}, safe=False)


# >>>   USER PROFILE VIEWS HERE
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def MakeUserProfile(request):
    if UserProfile.objects.filter(belongsTo=request.data['belongsTo']):
        return JsonResponse(status=406, data={'message': 'Userprofile already created!'}, safe=False)
    else:
        data = UserProfileSerializer(data=request.data, partial=True)
        if data.is_valid():
            data.save()
            return JsonResponse(status=200, data={'message': 'Userprofile was made!'}, safe=False)
        else:
            return JsonResponse(status=406, data={'message': 'Corrupt data received!'}, safe=False)


@api_view(['GET'])
def ViewUserProfile(request, id):
    try:
        userprofile = UserProfile.objects.filter(belongsTo=id)
        if userprofile:
            serializedUserProfile = UserProfileSerializer(
                userprofile, many=True)
            return JsonResponse(status=200, data={'data': serializedUserProfile.data}, safe=False)
        else:
            return JsonResponse(status=204, data={'message': f'No Userprofile Found under ID: {id} !'}, safe=False)
    except:
        return JsonResponse(status=406, data={'message': 'Uncaught Error!'}, safe=False)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def EditUserProfile(request, id):
    selectedProfile = UserProfile.objects.get(belongsTo=id)
    if selectedProfile:
        parsedData = JSONParser().parse(request)
        data = UserProfileSerializer(
            selectedProfile, data=parsedData, partial=True)
        if data.is_valid():
            data.save()
            return JsonResponse(status=200, data={'message': 'Profile Updated!'}, safe=False)
        else:
            return JsonResponse(status=406, data={'message': 'Django Error (BAD DATA)!'}, safe=False)
    else:
        return JsonResponse(status=406, data={'message': 'No Userprofile Found!'}, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UpdateProfilePicture(request, id):
    try:
        post = UserProfile.objects.get(belongsTo=id)
        try:
            os.remove(post.profilePicture.path)
            response = {
                'response': 'Old post image deleted...! path = '+str(post.image.path)}
        except Exception as e:
            response = {'response': 'No image for delete '+str(e)}
            return JsonResponse(status=406, data=response, safe=False)

        post.profilePicture = request.FILES['profilePicture']
        post.save()
        return JsonResponse(status=200, data='success', safe=False)

    except Exception as e:
        print(e)
        response = {
            'response': 'Error: Post image update failed...!'
        }
    return JsonResponse(status=406, data='fail', safe=False)


# >>>   USER NAME AVAILABILITY CHECK
@api_view(["POST"])
def CheckUserNameAvailability(request):
    try:
        Username = User.objects.get(username=request.data['username'])
        if Username:
            return JsonResponse(status=406, data={'message': 'Username Already Taken!'}, safe=False)
    except:
        return JsonResponse(status=200, data={'message': 'Username Available!'}, safe=False)

# >>>   USER NAME AVAILABILITY CHECK


@api_view(["GET"])
def GetUsername(request, id):
    try:
        user = User.objects.get(id=id)
        if user:
            return JsonResponse(status=200, data=user.username, safe=False)
        else:
            return JsonResponse(status=204, data={'message': "couldn't find the user!"}, safe=False)
    except:
        return JsonResponse(status=204, data={'message': "couldn't find the user!"}, safe=False)


# >>>   USER EXPERIENCE VIEWS HERE
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def MakeUserExperience(request):
    if UserExperience.objects.filter(belongsTo=request.data['belongsTo'], companyName=request.data['companyName'], position=request.data['position']):
        return JsonResponse(status=406, data={'message': 'Experience Already Added!'})
    else:
        data = UserExperienceSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(status=200, data={'message': 'Experience Added Successfully!'}, safe=False)
        else:
            return JsonResponse(status=406, data={'message': 'Invalid Data Received!'})


@api_view(['GET'])
def ViewUserExperience(request, id):
    try:
        userExperience = UserExperience.objects.filter(belongsTo=id)
        if userExperience:
            serializedUserExperience = UserExperienceSerializer(
                userExperience, many=True)
            return JsonResponse(status=200, data={'data': serializedUserExperience.data}, safe=False)
        else:
            return JsonResponse(status=204, data={'message': f'No User Experience Found under ID: {id} !'}, safe=False)
    except:
        return JsonResponse(status=406, data={'message': 'Uncaught Error!'}, safe=False)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def EditUserExperience(request, id):
    current_user = request.user.id
    selectedExperience = UserExperience.objects.get(
        id=id, belongsTo=current_user)
    if selectedExperience:
        parsedData = JSONParser().parse(request)
        data = UserExperienceSerializer(
            selectedExperience, data=parsedData, partial=True)
        if data.is_valid():
            data.save()
            return JsonResponse(status=200, data={'message': 'Experience Updated!'}, safe=False)
        else:
            return JsonResponse(status=406, data={'message': 'Bad Data Received!'}, safe=False)
    else:
        return JsonResponse(status=406, data={'message': 'No Experience Found!'}, safe=False)


# >>>   USER PROJECTS VIEWS HERE
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def MakeUserProject(request):
    if UserProject.objects.filter(belongsTo=request.data['belongsTo'], name=request.data['name']):
        return JsonResponse(status=406, data={'message': 'Project Already Added!'})
    else:
        data = UserProjectSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(status=200, data={'message': 'Project Added Successfully!'}, safe=False)
        else:
            return JsonResponse(status=406, data={'message': 'Invalid Data Received!'})


@api_view(['GET'])
def ViewUserProject(request, id):
    try:
        userProject = UserProject.objects.filter(belongsTo=id)
        if userProject:
            serializedUserProject = UserProjectSerializer(
                userProject, many=True)
            return JsonResponse(status=200, data={'data': serializedUserProject.data}, safe=False)
        else:
            return JsonResponse(status=204, data={'message': f'No User Projects Found under ID: {id} !'}, safe=False)
    except:
        return JsonResponse(status=406, data={'message': 'Uncaught Error!'}, safe=False)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def EditUserProject(request, id):
    current_user = request.user.id
    selectedProject = UserProject.objects.get(id=id, belongsTo=current_user)
    if selectedProject:
        parsedData = JSONParser().parse(request)
        data = UserProjectSerializer(
            selectedProject, data=parsedData, partial=True)
        if data.is_valid():
            data.save()
            return JsonResponse(status=200, data={'message': 'Project Updated!'}, safe=False)
        else:
            return JsonResponse(status=406, data={'message': 'Bad Data Received!'}, safe=False)
    else:
        return JsonResponse(status=406, data={'message': 'No Projects Found!'}, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def UpdateProjectImage(request, id):
    try:
        current_user = request.user.id
        post = UserProject.objects.get(id=id, belongsTo=current_user)
        try:
            os.remove(post.projectImage.path)
            response = {
                'response': 'Old post image deleted...! path = '+str(post.image.path)}
        except Exception as e:
            response = {'response': 'No image for delete '+str(e)}
            return JsonResponse(status=406, data=response, safe=False)

        post.projectImage = request.FILES['projectImage']
        post.save()
        return JsonResponse(status=200, data='success', safe=False)

    except Exception as e:
        print(e)
        response = {
            'response': 'Error: Post image update failed...!'
        }
    return JsonResponse(status=406, data='fail', safe=False)


# >>>   USER SKILL VIEWS HERE
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def MakeUserSkill(request):
    if UserSkill.objects.filter(belongsTo=request.data['belongsTo'], name=request.data['name']):
        return JsonResponse(status=406, data={'message': 'Skill Already Added!'})
    else:
        data = UserSkillSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(status=200, data={'message': 'Skill Added Successfully!'}, safe=False)
        else:
            return JsonResponse(status=406, data={'message': 'Invalid Data Received!'})


@api_view(['GET'])
def ViewUserSkill(request, id):
    try:
        userSkill = UserSkill.objects.filter(belongsTo=id).order_by('level')
        if userSkill:
            serializedUserSkill = UserSkillSerializer(
                userSkill, many=True)
            return JsonResponse(status=200, data=serializedUserSkill.data, safe=False)
        else:
            return JsonResponse(status=204, data={'message': f'No User Skills Found under ID: {id} !'}, safe=False)
    except:
        return JsonResponse(status=406, data={'message': 'Uncaught Error!'}, safe=False)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def EditUserSkill(request, id):
    current_user = request.user.id
    selectedSkill = UserSkill.objects.get(id=id, belongsTo=current_user)
    if selectedSkill:
        parsedData = JSONParser().parse(request)
        data = UserSkillSerializer(
            selectedSkill, data=parsedData, partial=True)
        if data.is_valid():
            data.save()
            return JsonResponse(status=200, data={'message': 'Skill Updated!'}, safe=False)
        else:
            return JsonResponse(status=406, data={'message': 'Bad Data Received!'}, safe=False)
    else:
        return JsonResponse(status=406, data={'message': 'No Skills Found!'}, safe=False)


# >>>   USER CERTIFICATES VIEWS HERE
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def MakeUserCertificate(request):
    if UserCertificate.objects.filter(belongsTo=request.data['belongsTo'], name=request.data['name']):
        return JsonResponse(status=406, data={'message': 'Certificate Already Added!'})
    else:
        data = UserCertificateSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(status=200, data={'message': 'Certificate Added Successfully!'}, safe=False)
        else:
            return JsonResponse(status=406, data={'message': 'Invalid Data Received!'})


@api_view(['GET'])
def ViewUserCertificate(request, id):
    try:
        userCertificate = UserCertificate.objects.filter(belongsTo=id)
        if userCertificate:
            serializedUserCertificate = UserCertificateSerializer(
                userCertificate, many=True)
            return JsonResponse(status=200, data={'data': serializedUserCertificate.data}, safe=False)
        else:
            return JsonResponse(status=204, data={'message': f'No User Certificate Found under ID: {id} !'}, safe=False)
    except:
        return JsonResponse(status=406, data={'message': 'Uncaught Error!'}, safe=False)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def EditUserCertificate(request, id):
    try:
        current_user = request.user.id
        selectedCertificate = UserCertificate.objects.get(
            id=id, belongsTo=current_user)
        if selectedCertificate:
            parsedData = JSONParser().parse(request)
            data = UserSkillSerializer(
                selectedCertificate, data=parsedData, partial=True)
            if data.is_valid():
                data.save()
                return JsonResponse(status=200, data={'message': 'Certificate Updated!'}, safe=False)
            else:
                return JsonResponse(status=406, data={'message': 'Bad Data Received!'}, safe=False)
        else:
            return JsonResponse(status=406, data={'message': 'No Certificates Found!'}, safe=False)
    except:
        return JsonResponse(status=406, data={'message': 'Fatal Error!'}, safe=False)


# >>>   USER LINKS VIEWS HERE
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def MakeUserLink(request):
    if UserLink.objects.filter(belongsTo=request.data['belongsTo'], name=request.data['name']):
        return JsonResponse(status=406, data={'message': 'User Link Already Added!'})
    else:
        data = UserLinkSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return JsonResponse(status=200, data={'message': 'User Link Added Successfully!'}, safe=False)
        else:
            return JsonResponse(status=406, data={'message': 'Invalid Data Received!'})


@api_view(['GET'])
def ViewUserLink(request, id):
    try:
        userLink = UserLink.objects.filter(belongsTo=id).order_by('-name')
        if userLink:
            serializedUserLink = UserLinkSerializer(
                userLink, many=True)
            return JsonResponse(status=200, data={'data': serializedUserLink.data}, safe=False)
        else:
            return JsonResponse(status=204, data={'message': f'No User Links Found under ID: {id} !'}, safe=False)
    except:
        return JsonResponse(status=406, data={'message': 'Uncaught Error!'}, safe=False)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def EditUserLink(request, id):
    try:
        current_user = request.user.id
        selectedLink = UserLink.objects.get(id=id, belongsTo=current_user)
        if selectedLink:
            parsedData = JSONParser().parse(request)
            data = UserLinkSerializer(
                selectedLink, data=parsedData, partial=True)
            if data.is_valid():
                data.save()
                return JsonResponse(status=200, data={'message': 'Link Updated!'}, safe=False)
            else:
                return JsonResponse(status=406, data={'message': 'Bad Data Received!'}, safe=False)
        else:
            return JsonResponse(status=406, data={'message': 'No Link Found!'}, safe=False)
    except:
        return JsonResponse(status=406, data={'message': 'Fatal Error!'}, safe=False)


# >>>   SEARCH USERS VIEW
@api_view(['GET'])
def SearchUsers(request, username):
    try:
        username = username[0].upper() + username[1:]
        userProfile = UserProfile.objects.get(
            fname=username, isDiscoverable=True)
        if userProfile:
            serializedUserProfile = UserProfileSerializer(userProfile)
            return JsonResponse(status=200, data={'user': serializedUserProfile.data}, safe=False)
        else:
            return JsonResponse(status=204, data={'message': 'No user found!'}, safe=False)
    except:
        return JsonResponse(status=204, data={'message': 'No user found!'}, safe=False)


# >>>   PEOPLE LIKE YOU  VIEW
@  api_view(['GET'])
def PeopleLikeYou(request, position):
    similarPeople = UserProfile.objects.filter(
        position=position, isDiscoverable=True)[:8]
    if similarPeople:
        serializedPeople = UserProfileSerializer(similarPeople, many=True)
        return JsonResponse(status=200, data={'people': serializedPeople.data})
    else:
        return JsonResponse(status=204, data={'message': 'No Similar People Found!'}, safe=False)


# >>>   NEW USERS  VIEW
@  api_view(['GET'])
def NewUsers(request):
    newUsers = UserProfile.objects.filter(
        isDiscoverable=True).order_by('-createdAt')[:4]
    if newUsers:
        serializedUsers = UserProfileSerializer(newUsers, many=True)
        return JsonResponse(status=200, data={'users': serializedUsers.data}, safe=False)
    else:
        return JsonResponse(status=406, data={'message': 'No Users or Error!'}, safe=False)
