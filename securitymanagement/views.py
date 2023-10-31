from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect;
from securitymanagement.models import visitor,securityShift,securityIncident,securitydata;
from django.db.models import Q;
from django.urls import reverse;
from .models import securityShift


# Create your views here.

# Create your views here.


def loginpage(request):
    return render(request, "loginpage.html")


def loginguard(request):
    return render(request, "loginguard.html")


def loginfelo(request):
    return render(request, "loginfelo.html")


def loginadmin(request):
    return render(request, "loginadmin.html")


def Securityhome(request):
    return render(request, "Securityhome.html")


def felohome(request):
    return render(request, "felohome.html")

#------------------------------------------------------------------------------------------------------------------------------------
    
#add visitor data (security)

def register_visitor(request):
    if request.method == 'POST':
        a_visitorName = request.POST['visitorName']
        a_visitorIc = request.POST['visitorIc']
        a_visitorPhone = request.POST['visitorPhone']
        a_visitorDate = request.POST['visitorDate']
        data = visitor(visitorName=a_visitorName,visitorIc= a_visitorIc,visitorPhone= a_visitorPhone,visitorDate =a_visitorDate)
        data.save()
        dict = {
            'message':'Data save'
        }
        return render(request, 'register_visitor.html',dict)
    else:
        dict ={
            'message':' '
        }
        return render(request,'register_visitor.html')
    


#view visitor table (felo)

def feloviewvisitor(request):
    alldata = visitor.objects.all()
    dict={
        'alldata': alldata
    }
    return render (request,'feloviewvisitor.html',dict)


#edit and delete table visitor (admin)


#------------------------------------------------------------------------------------------------------------------------------------
#add table shift(felo)

from django.shortcuts import render, redirect
from .models import securityShift  # Import your model

def feloaddshift(request):
    if request.method == 'POST':
        a_securityID = request.POST['securityID']
        f_securityID = securitydata.objects.get(securityID=a_securityID)
        a_shiftDate = request.POST['shiftDate']
        a_startTime = request.POST['startTime']
        a_endTime = request.POST['endTime']
        a_Shiftdesc = request.POST['Shiftdesc']
        data = securityShift(
            securityID=f_securityID,
            shiftDate=a_shiftDate,
            startTime=a_startTime,
            endTime=a_endTime,
            Shiftdesc=a_Shiftdesc
        )
        data.save()
        return render(request, "feloaddshift.html", dict)

    else:
        dict = {
            'message': ' '
        }
        return render(request, "feloaddshift.html", dict)




#view table shift (security)


def Security_shift(request):
    # Retrieve all data from the securityShift model
    all_security_shifts = securityShift.objects.all()
    return render(request, 'Security_shift.html', {'all_security_shifts': all_security_shifts})

#edit and delete table shift (felo)


def shiftedit(request):
    return render(request, 'shiftedit.html')
#view table before update/delete






    


#------------------------------------------------------------------------------------------------------------------------------------


#create incident report (security)

def Security_incidentreport(request):  
    if request.method == 'POST':
        a_incidentID = request.POST['incidentID']
        a_incidentDate = request.POST['incidentDate']
        a_incidentLoc = request.POST['incidentLoc']
        a_incidentDesc = request.POST['incidentDesc']
        data = securityIncident(incidentID=a_incidentID,incidentDate= a_incidentDate,incidentLoc= a_incidentLoc, incidentDesc =a_incidentDesc)
        data.save()
        dict = {
            'message':'Data save'
        }
        return render(request, 'Security_incidentreport.html',dict)
    else:
        dict ={
            'message':' '
        }
        return render(request,'Security_incidentreport.html')
    



#felo view table incident (felo)

def feloviewincident(request):
    alldata = securityIncident.objects.all()
    dict={
        'alldata': alldata
    }
    return render (request,'feloviewincident.html',dict)

#edit and delete table incident (security)


#------------------------------------------------------------------------------------------------------------------------------------

# add table security data (felo)

def addsecuritydata(request):
    if request.method == 'POST':
        a_securityID = request.POST['securityID']
        a_securityName = request.POST['securityName']
        a_securityIC = request.POST['securityIC']
        a_securityNophone = request.POST['securityNophone']
        data = securitydata(securityID=a_securityID,securityName= a_securityName,securityIC= a_securityIC,securityNophone =a_securityNophone)
        data.save()
        dict = {
            'message':'Data save'
        }
        return render(request, 'feloaddsecurity.html',dict)
    else:
        dict ={
            'message':' '
        }
        return render(request,'feloaddsecurity.html')


# view table security data (felo)


def feloviewsecurity(request):
    alldata = securitydata.objects.all()
    dict={
        'alldata': alldata
    }
    return render (request,'feloviewsecurity.html',dict)


# edit and delete table security



#------------------------------------------------------------------------------------------------------------------------

def updelshift(request):
    # Retrieve all data from the securityShift model
    all_security_shifts = securityShift.objects.all()
    return render(request, 'updelshift.html', {'all_security_shifts': all_security_shifts})

def delete_shift(request, pk):
    try:
        shift = securityShift.objects.get(pk=pk)
        shift.delete()
    except securityShift.DoesNotExist:
        pass  # Handle the case where the shift does not exist
    return redirect('updelshift')  # Redirect back to the view displaying the shifts

def update_shift(request, pk):
    shift = get_object_or_404(securityShift, pk=pk)
    
    if request.method == 'POST':
        # Retrieve updated data from the form
        updated_securityID = request.POST['securityID']
        updated_shiftDate = request.POST['shiftDate']
        updated_startTime = request.POST['startTime']
        updated_endTime = request.POST['endTime']
        updated_Shiftdesc = request.POST['Shiftdesc']

        # Update the securityShift object with the new data
        shift.securityID.securityID = updated_securityID
        shift.shiftDate = updated_shiftDate
        shift.startTime = updated_startTime
        shift.endTime = updated_endTime
        shift.Shiftdesc = updated_Shiftdesc

        # Save the updated object to the database
        shift.save()

        return redirect('updelshift')  # Redirect to the 'updelshift' view after successful update

    return render(request, 'updateshift.html', {'shift': shift})





#---------------------------------------------------------------------------------------------------


def adminhomepage(request):
    return render(request, 'adminhomepage.html')

def adminvisitor(request):
    visitors = visitor.objects.all()
    return render(request, 'adminvisitor.html', {'visitors': visitors})

def updatevisitor(request,visitorIc):
   
  
    p_visitorIc=request.POST['visitorIc']
    p_visitorName=request.POST['visitorName']
    p_visitorPhone=request.POST['visitorPhone']
    p_visitorDate=request.POST['visitorDate']

    data=visitor.objects.get(visitorIc=visitorIc)
   
   
    data.visitorIc=p_visitorIc
    data.visitorName=p_visitorName
    data.visitorPhone=p_visitorPhone
    data.visitorDate=p_visitorDate
    data.save()
    return HttpResponseRedirect(reverse("adminvisitor.html"))







def adminincident(request):
    incidents = securityIncident.objects.all()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'delete':
            incident_id = request.POST.get('incident_id')
            incident = get_object_or_404(securityIncident, incidentID=incident_id)
            incident.delete()
            # You can handle the response as per your requirement
            return HttpResponseRedirect(request.path_info)  # Refresh the page

    return render(request, 'adminincident.html', {'incidents': incidents})

def delete_incident(request, incident_id):
    incident = get_object_or_404(securityIncident, incidentID=incident_id)
    incident.delete()
    return redirect('adminincident')