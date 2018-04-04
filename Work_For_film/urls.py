"""Work_For_film URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from user.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('user/', include('user.urls')),
    path('location_financial/', include('location_financials.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls')),
    path('location_pitch/', include('location_pitch.urls')),
    path('location_psndc/', include('location_psndc.urls')),
    path('location_subcategory/', include('location_subcategory.urls')),
    path('messages/', include('message.urls')),
    path('mimicry_artist/', include('mimicry_artist.urls')),
    path('model/', include('model.urls')),
    path('musician/', include('musician.urls')),
    path('officer_contact/', include('officer_contact.urls')),
    path('permit_query/', include('permit_query.urls')),
    path('pets/', include('pets.urls')),
    path('police_station/', include('police_station.urls')),
    path('platform_works/', include('platform_works.urls')),
    path('portfolio_element/', include('portfolio_element.urls')),
    path('profile_projects/', include('Profile_Projects.urls')),
    path('subcription_plan/', include('Subcription_Plan.urls')),
    path('talent_profile/', include('TalentProfile.urls')),
    path('user_coin_box/', include('UserCoinBox.urls')),

    path('help_center/', include('help_center.urls')),
    path('help_subcategory/', include('help_subcategory.urls')),
    path('location/', include('Location.urls')),
    path('location_authorities/', include('Location_Authorities.urls')),
    path('prop/', include('Prop.urls')),
    path('ratings/', include('Ratings.urls')),
    path('help_category/', include('help_category.urls')),
    path('help_qna/', include('help_Qna.urls')),
    path('letter_pdf/', include('Letter_pdf.urls')),
    path('location_amenitie/', include('Location_Amenitie.urls')),
    path('location_category/', include('Location_Category.urls')),
    path('quick_requirements/', include('Quick_Requirements.urls')),
    path('review/', include('Review.urls')),
    path('search/', include('Search.urls')),

    path('costumes/', include('Costumes.urls')),
    path('dancers/', include('Dancers.urls')),
    path('dashboards/', include('Dashboards.urls')),
    path('districts/', include('Districts.urls')),
    path('educationinfos/', include('EducationInfos.urls')),
    path('film_location_from_guided_withserial/', include('FilmLocationFromGuidedWithSerial.urls')),
    path('film_location_schedule_for_permit/', include('FilmLocationScheduleForPermit.urls')),
    path('film_project_for_permit/', include('FilmProjectForPermit.urls')),
    path('film_recce_route/', include('FilmRecceRoute.urls')),
    path('film_recce_tour_guide/', include('FilmRecceTourGuide.urls')),
    path('service_category/', include('ServiceCatagory.urls')),
    path('service_subcategory/', include('ServiceSubcatagory.urls')),
    path('singer/', include('Singer.urls')),
    path('special_art/', include('SpecialArt.urls')),
    path('state/', include('State.urls')),
    path('action_vehicle/', include('actionvehicle.urls')),
    path('actors/', include('actors.urls')),
    path('amenity_adresses/', include('Amenity_Adresses.urls')),
    path('booking/', include('Booking.urls')),
    path('child_artist/', include('ChildArtist.urls')),
    path('circle_invite/', include('CircleInvite.urls')),
    path('client/', include('Client.urls')),
    path('comments/', include('Comments.urls')),
    path('contact_messages/', include('ContactMessages.urls')),
    path('conversations/', include('conversations.urls')),
    path('user_details/', include('userdetails.urls')),
    path('user_professional_info/', include('userprofessionalinfo.urls')),
    path('voice_over_artsit/', include('VoiceOverArtist.urls')),
    # path('theater_actor/', include('Theater_Actor.urls')),

]
