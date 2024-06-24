from django.shortcuts import render,get_object_or_404
from .models import Seminer_Time,Seminer_Image_Text,CourseInfo

from Deshboard.models import All_category_text,All_Category_model,All_Category_Card_Data

    

def All_course_Page_views(request):
    # all cattegoroy and card show code
    show_all_category = All_Category_model.objects.all()
    
    category_card_data = {}
    for category in show_all_category:
        cards = All_Category_Card_Data.objects.filter(Category_Name = category)
        category_card_data[category] = cards
        
    
    # seminer show code
    
    seminer_time = Seminer_Time.objects.all()[:3]
    seminerText = Seminer_Image_Text.objects.last()

    if not seminerText:
        # Handle case where no Seminer_Image_Text objects exist
        seminerText = None
   
    return render(request, 'all_course_page.html', {'show_all_category': show_all_category, 'category_card_data': category_card_data, 'seminer_time':seminer_time, 'seminerText': seminerText})





def Seminer_Page_views(request, category_slug = None):
    seminer = Seminer_Time.objects.all()
    seminerText = Seminer_Image_Text.objects.last()

    if not seminerText:
        seminerText = None  
    
    
      
    # 4. All Cagegory
    all_cagegory = All_Category_model.objects.all()
    card_data = All_Category_Card_Data.objects.all()
    if category_slug is not None:
        
        CategoryName = All_Category_model.objects.get(slug =category_slug )
        
        
        card_data = All_Category_Card_Data.objects.filter(Category_Name = CategoryName)
        
    
    all_cattogory_top_text = All_category_text.objects.last()
    
    
    return render(request, 'join_seminer.html', {
        'seminer': seminer,
        'seminerText': seminerText,
        'all_cagegory': all_cagegory,
        'card_data':card_data,
        'all_cattogory_top_text':all_cattogory_top_text,
        
    }) 
                
                