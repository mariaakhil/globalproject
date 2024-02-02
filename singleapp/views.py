

# views.py
from django.shortcuts import render, redirect
from .models import ContactFormSubmission,CareerApplication
from django.contrib import messages

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save form data to the database
        submission = ContactFormSubmission(name=name, email=email, phone=phone, subject=subject, message=message)
        submission.save()

        # Optionally, you can add a success message
        messages.success(request, 'Your message was sent successfully!')

        return redirect('home')  # Redirect to a success page

    return render(request, 'index.html')  # Replace 'your_template.html' with the actual template name


def home(request):
    return render(request, 'index.html')


def career(request):
   

    if request.method == 'POST':
       
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        
        education_level = request.POST.get('education_level')
        experience = request.POST.get('experience')
        resume = request.FILES.get('resume')
        contact_number = request.POST.get('contact_number')
        plf = request.POST.get('plf')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')

        career_application = CareerApplication.objects.create(email=email,first_name=first_name,address=address,
            city=city,
            state=state,
            
            education_level=education_level,
            experience=experience,
            resume=resume,
            contact_number=contact_number,
            plf=plf,
            date_of_birth=date_of_birth,
            gender=gender
        )
        career_application.save()
    
        messages.success(request, 'Application submitted successfully.')

        # Redirect to the home page or any other page you want
        return redirect('home')  # Redirect to a success page

    return render(request, 'index.html') 


