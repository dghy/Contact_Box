from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from Box.models import *


class ShowAll(View):
     
    def get(self, request):     
        response = HttpResponse()
        response.write("Show All")
        return response 


class NewPerson(View):
    HTML = """
                <html>
                    <h2>You are adding new person! </h2>
                    <form method="post" action="" id="new_form">
                        <label>First Name</label><br>
                        <input name="first_name" type="text" maxlength="255" value=""/><br>
                        <label>Last Name</label><br>
                        <input name="last_name" type="text" maxlength="255" value=""/><br>
                        
                        <label>Address:</label></br> 
                        {}
                                
                                                            
                        <label>Telephone:</label><br>
                        <a href=/add_telephone>Add Telephone..</a><br>
                                                
                        <label>E-mail:</label><br>
                        <a href=/add_email>Add Email..</a><br>
                        
                    </form>                       
                        
                    <h5>Write description of person here:</h5>                    
                    <textarea rows="4" cols="50" name="description" form="new_form">
Enter text here...
                    </textarea><br>
                    <button type="submit" name="submit" value="name" form="new_form">Add New!</button>   
                    
                    
                </html>"""


    def get(self, request, address=None, telephone=None, email=None):

        response = HttpResponse()
        
        address = response.write(request.GET.get('address'))
        address = request.GET.get('address')

#         response.write(self.HTML)

        # first display with no data inputed in the address,telephone and mail
        if address == None:
            
            response.write(self.HTML.format("<a href=/add_address>Add Adress..</a><br>"))    
        else:
#               response.write(address)
            city = address[0]
            street = address[1]
            d_number = address[2]
            h_number = address[3]
            
            in_form = """
                    City: {}, Street: {}, House Number: {}, Door Number: {} <br>             
                    """.format(city, street, h_number, d_number)            
            
            response.write(self.HTML.format(in_form)) 
        
        
        
        return response
    
    def post(self, request):        
        
        response = HttpResponse()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
                
                
#         Person.objects.create()





        response.write(first_name)
        response.write(" ")
        response.write(last_name)
        
        return response
     
     
     
     
class ShowPerson(View):
 
    def get(self, request):     
        response = HttpResponse()
        response.write("Show Person")
        return response      
     
     
     
class DeletePerson(View):

    def get(self, request):     
        response = HttpResponse()
        response.write("Delete Person")
        return response 
     
               
class ModifyPerson(View):
 
    def get(self, request):     
        response = HttpResponse()
        response.write("Modify Person")
        return response 
     
     
class AddAddress(View):    
    HTML = """
            <h2>You are adding new address! </h2>
                <form method="post" action="" id="new_form">
                    <label>City:</label><br>
                    <input name="city" type="text" maxlength="255" value=""/><br>
                        
                    <label>Street:</label><br>
                    <input name="street" type="text" maxlength="255" value=""/><br>
                        
                    <label>House Number:</label></br> 
                    <input name="h_number" type="number" min="1" value="1"/><br>
                                                            
                    <label>Door Number:</label><br>
                    <input name="d_number" type="number" min="1" value="1"/><br>

                    <button type="submit" name="submit" value="name" form="new_form">Add Address!</button>   
                </form>
             """ 
                   
 
    def get(self, request):     
        response = HttpResponse()        
        response.write(self.HTML)
        return response
    
   
    def post(self, request):
        response = HttpResponse()
        
        city = request.POST.get("city")
        street = request.POST.get("street")    
        h_number = request.POST.get("h_number")
        d_number = request.POST.get("d_number")
        
#         address = Address.objects.create(city=city, street=street, house_number=h_number, door_number=d_number)
         
        address = ((city), (street), (d_number), (h_number))                
#                 
#         return HttpResponseRedirect('/new_person?city={}&street={}&h_number={}&d_number={}'.format(city, street, h_number, d_number))
        
        return HttpResponseRedirect('/new_person?address={}'.format(address))


















        
class AddTelephone(View):

    def get(self, request):     
        response = HttpResponse()
        response.write("Add New Telephone")
        return response
        
        
         
class AddEmail(View):
  
    def get(self, request):     
        response = HttpResponse()
        response.write("Add New Email")
        response.write("girhjfeigbfjewbhfjioewhbjiofewghb")
        return response   
        
         
         
         
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
