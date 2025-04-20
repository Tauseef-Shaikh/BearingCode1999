from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import json

def login_user(request):
    #data_json={}
    #data_json = json.dumps(py_dict_list)
	
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and 'admin' not in username:
            login(request, user)
            with open (__package__+'/data/'+str(request.user)+'.csv','w') as cf:
                cf.write('GrpEntry,BearingType,SubType,Code,Quantity,DateTime,LastAmt,CodeB4Split,EntryNo')
                cf.write('\n')

            with open (__package__+'/data/solo_'+str(request.user)+'.csv','w') as cf:
                cf.write('GrpEntry,BearingType,SubType,Code,Quantity,DateTime,LastAmt,CodeB4Split,EntryNo')
                cf.write('\n')
            
            return redirect('create_entry')

        elif user is not None and username == 'admin':
            login(request, user)            
            return redirect('admin_view')
		
        elif user is not None and username == 'super_admin':
            login(request, user)            
            return redirect('super_admin_view')	
        
        elif user is not None and username == 'hisab_admin':
            login(request, user)            
            return redirect('hisab_admin_view')	
			
        else:
            # Handle invalid login credentials here                        
            loginErrMsg = {'errMsg': 'Invalid Username or Password Entered',}

            return render(request, 'myapp/login.html', {'loginErrMsg':loginErrMsg})
            
    
    return render(request, 'myapp/login.html')