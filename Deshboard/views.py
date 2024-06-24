from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from . models import BannerModel, All_category_text,All_Category_model,All_Category_Card_Data,HomeOurService,Our_Service_Text,Success_history_video

from . models import HomeInstituteBanner,HomeInstituteBannersecond,HomeEvent,HomeExpertTeacher,HomeStudentOpenion,our_partner
from HomePage.models import Seminer_Time,Seminer_Image_Text,CourseInfo
from django.views.generic import DetailView
from Social_Media.models import Popup_banner,ContractUs_Form


# Create your views here. 

def HomeView(request, category_slug = None):
     
    # 2. Banner Model ses
    
    last_banner = BannerModel.objects.last()
    if last_banner:
        video_url = last_banner.Banner_video.url
    else:
        video_url = None
    
    
    
     
    all_cagegory = All_Category_model.objects.all()
    card_data = All_Category_Card_Data.objects.all()
    
    
    if category_slug:
        try:
            CategoryName = All_Category_model.objects.get(slug=category_slug)
            card_data = All_Category_Card_Data.objects.filter(Category_Name=CategoryName)
        except All_Category_model.DoesNotExist:
            CategoryName = None

            
            
    # 4.1 all Cagegory 
    all_cattogory_top_text = All_category_text.objects.last()

    

    # 5. Our Special Service ses
    ourService = HomeOurService.objects.all()
    
    
    # 5.1 Our Special Service
    ourService_text_image = Our_Service_Text.objects.last()
    
     
    # 6.Category Wise Show ses
    
    all_cagegorys = All_Category_model.objects.all()[:3]
    category_card_data = {}
    
    for category in all_cagegorys:
        cards = All_Category_Card_Data.objects.filter(Category_Name = category) [:3]
        category_card_data[category] = cards
        
        
    # 7.Join Our Free Seminer ses
    
    seminer_time = Seminer_Time.objects.all()[:3]
    seminerText = Seminer_Image_Text.objects.last()

    if not seminerText:
        # Handle case where no Seminer_Image_Text objects exist
        seminerText = None
    
    # 8. Institute Banner ses
    
    institute_Banner = HomeInstituteBanner.objects.all()
    
    # 8.1 institute banner ses
    institute_Banner_second = HomeInstituteBannersecond.objects.all()
    
    
    # 9. Success history text
    success_text = Success_history_video.objects.last()
    
    # 9.1 Success history video
    latest_success_video = Success_history_video.objects.all()[:4]
   


    
    # 10. Event And Acctivities  ses
    
    Event = HomeEvent.objects.all()
     
    # 11.Our Expert Teacher ses
    ExpertTeacher = HomeExpertTeacher.objects.all()
    
    # 12. Our Student Openion ses
    
    StudentOpenion = HomeStudentOpenion.objects.all()
    
    # 14. Our partner image
    
    partner = our_partner.objects.all()
    
    # popup Banner
    
    popupBanner = Popup_banner.objects.last()
    
    
    
    return render(request, 'home.html',{
        'last_banner':last_banner,
        'video_url':video_url,
        'all_cagegory':all_cagegory, 
        'all_cattogory_top_text':all_cattogory_top_text,
        'ourService':ourService,
        'ourService_text_image':ourService_text_image,
        'category_card_data':category_card_data,
        'Free_seminer':seminer_time, 
        'seminerText':seminerText,
        'institute_Banner':institute_Banner,
        'institute_banner_sec':institute_Banner_second,
        'Event':Event, 
        'ExpertTeacher':ExpertTeacher, 
        'StudentOpenion':StudentOpenion,
        'card_data':card_data,
        'partner':partner,
        'success_text':success_text,
        'success_video':latest_success_video,
        'CategoryName': CategoryName if category_slug else None,
        'popupBanner':popupBanner,
        

        })


def detail_category_page(request, id):
    category = get_object_or_404(All_Category_model, pk=id)
    showAllCard = All_Category_Card_Data.objects.filter(Category_Name = category)
    latest_courseinfo = CourseInfo.objects.filter(Category=category).order_by('-id').first()
   
   
    
    return render(request, 'category_page.html', {'category': category, 'showAllCard': showAllCard,'courseinfo': latest_courseinfo })






def Contract_us_forms_reqturn(request):
    return render(request, 'home.html')

def Contract_us_forms_view(request):
    if request.method == 'POST':
        people_name = request.POST.get('people_name')
        people_email = request.POST.get('people_email')
        message = request.POST.get('message')
        
        try:
            ContractUs_Form.objects.create(
                people_name=people_name,
                people_email=people_email,
                message=message
            )
            messages.success(request, 'Form submitted successfully!')
            return redirect('homepage')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('homepage')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('homepage')