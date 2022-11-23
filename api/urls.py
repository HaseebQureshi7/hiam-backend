from django.urls import path
from .views import Signup, MakeUserProfile, ViewUserProfile, EditUserProfile, CheckUserNameAvailability, MakeUserExperience, ViewUserExperience, EditUserExperience, MakeUserProject, ViewUserProject, EditUserProject, MakeUserSkill, ViewUserSkill, EditUserSkill, MakeUserCertificate, ViewUserCertificate, EditUserCertificate, MakeUserLink, ViewUserLink, EditUserLink, SearchUsers, NewUsers, PeopleLikeYou, UpdateProfilePicture, GetUsername, UpdateProjectImage, ViewSingleExperience, ViewSingleProject, ViewSingleCertificate, DeleteUserExperience, DeleteUserProject, DeleteUserSkill, DeleteUserCertificate, Statistics, FuzzySearch
urlpatterns = [
    path('signup', Signup),

    path('makeuserprofile', MakeUserProfile),
    path('viewuserprofile/<int:id>', ViewUserProfile),
    path('edituserprofile/<int:id>', EditUserProfile),
    path('editprofilepicture/<int:id>', UpdateProfilePicture),
    path('checkuseravailability', CheckUserNameAvailability),
    path('getusername/<int:id>', GetUsername),

    path('makeuserexperience', MakeUserExperience),
    path('viewuserexperience/<int:id>', ViewUserExperience),
    path('viewsingleexperience/<int:id>', ViewSingleExperience),
    path('edituserexperience/<int:id>', EditUserExperience),
    path('deleteuserexperience/<int:id>', DeleteUserExperience),

    path('makeuserproject', MakeUserProject),
    path('viewuserproject/<int:id>', ViewUserProject),
    path('viewsingleproject/<int:id>', ViewSingleProject),
    path('edituserproject/<int:id>', EditUserProject),
    path('updateprojectimage/<int:id>', UpdateProjectImage),
    path('deleteuserproject/<int:id>', DeleteUserProject),


    path('makeuserskill', MakeUserSkill),
    path('viewuserskill/<int:id>', ViewUserSkill),
    path('edituserskill/<int:id>', EditUserSkill),
    path('deleteuserskill/<int:id>', DeleteUserSkill),

    path('makeusercertificate', MakeUserCertificate),
    path('viewusercertificate/<int:id>', ViewUserCertificate),
    path('viewsinglecertificate/<int:id>', ViewSingleCertificate),
    path('editusercertificate/<int:id>', EditUserCertificate),
    path('deleteusercertificate/<int:id>', DeleteUserCertificate),


    path('makeuserlink', MakeUserLink),
    path('viewuserlink/<int:id>', ViewUserLink),
    path('edituserlink/<int:id>', EditUserLink),

    path('searchuser/<str:username>', SearchUsers),

    path('peoplelikeyou/<str:position>', PeopleLikeYou),

    path('newusers', NewUsers),

    path('statistics/', Statistics),

    path('fuzzysearch/<str:username>', FuzzySearch),
]
