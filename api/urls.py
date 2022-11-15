from django.urls import path
from .views import Signup, MakeUserProfile, ViewUserProfile, EditUserProfile, CheckUserNameAvailability, MakeUserExperience, ViewUserExperience, EditUserExperience, MakeUserProject, ViewUserProject, EditUserProject, MakeUserSkill, ViewUserSkill, EditUserSkill, MakeUserCertificate, ViewUserCertificate, EditUserCertificate, MakeUserLink, ViewUserLink, EditUserLink, SearchUsers, NewUsers, PeopleLikeYou, UpdateProfilePicture, GetUsername, UpdateProjectImage

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
    path('edituserexperience/<int:id>', EditUserExperience),

    path('makeuserproject', MakeUserProject),
    path('viewuserproject/<int:id>', ViewUserProject),
    path('edituserproject/<int:id>', EditUserProject),
    path('updateprojectimage/<int:id>', UpdateProjectImage),

    path('makeuserskill', MakeUserSkill),
    path('viewuserskill/<int:id>', ViewUserSkill),
    path('edituserskill/<int:id>', EditUserSkill),

    path('makeusercertificate', MakeUserCertificate),
    path('viewusercertificate/<int:id>', ViewUserCertificate),
    path('editusercertificate/<int:id>', EditUserCertificate),

    path('makeuserlink', MakeUserLink),
    path('viewuserlink/<int:id>', ViewUserLink),
    path('edituserlink/<int:id>', EditUserLink),

    path('searchuser/<str:username>', SearchUsers),

    path('peoplelikeyou/<str:position>', PeopleLikeYou),

    path('newusers', NewUsers),
]
