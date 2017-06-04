from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
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
                        <br>
                        <label>Address:</label></br> 
                        {}
                        <br>                                
                        <label>Telephone:</label><br>
                        {}
                        <br>                        
                        <label>E-mail:</label><br>
                        <a href=/add_email>Add Email..</a><br>
                        <br>
                    </form>                       
                        
                    <h5>Write description of person here:</h5>                    
                    <textarea rows="4" cols="50" name="description" form="new_form">
Enter text here...
                    </textarea><br>
                    <button type="submit" name="submit" value="name" form="new_form">Add New!</button>   
                  
                </html>"""

    def get(self, request):
        address = None
        in_form_address = """
                City: {}, Street: {}, House Number: {}, Door Number: {} 
                <a href=/add_address>Change Address..</a><br>            
                """

        telephone = None
        in_form_telephone = """
                Number: {}, Number Type: {} 
                <a href=/add_telephone>Change Telephone..</a><br>            
                """

        response = HttpResponse()
        # try:  # try get data form DB
        address = Address.objects.get(pk=1)
        telephone = Telephone.objects.get(pk=1)
        # except ObjectDoesNotExist:  # if there is no such tables in DB

        # first display with no data inputed in the address,telephone and mail
        if address is None:
            response.write(self.HTML.format("<a href=/add_address>Add Address..</a><br>", in_form_telephone))
        else:
            city = address.city
            street = address.street
            h_number = address.house_number
            d_number = address.door_number
            in_form_address = in_form_address.format(city, street, h_number, d_number)

        ##################################################################

        if telephone is None:
            response.write(self.HTML.format(in_form_address, "<a href=/add_telephone>Add Telephone..</a><br>"))
        else:
            telephone = Telephone.objects.get(pk=1)
            number = telephone.number
            num_type = telephone.get_type_display()

            in_form_telephone = in_form_telephone.format(number, num_type)


        response.write(self.HTML.format(in_form_address, in_form_telephone))
        return response

    def post(self, request):

        # when you want to save all person data into DB
        response = HttpResponse()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

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
        # response = HttpResponse()

        city = request.POST.get("city")
        street = request.POST.get("street")
        h_number = request.POST.get("h_number")
        d_number = request.POST.get("d_number")
        Address.objects.create(city=city, street=street, house_number=h_number, door_number=d_number)
        return HttpResponseRedirect('/new_person')


class AddTelephone(View):
    HTML = """
               <h2>You are adding new telephone! </h2>
                   <form method="post" action="" id="new_form">
                       <label>Number:</label><br>
                       <input name="number" type="number" value=""/><br>
                       <label>Type of telephone:</label><br>
                       <select name = "num_type">
                           <option value="1">Home Number</option>
                           <option value="2">Work Number</option>
                       </select>
                       <button type="submit" name="submit" value="telephone" form="new_form">Add Number!</button>   
                   </form>
                """

    def get(self, request):
        response = HttpResponse()
        response.write(self.HTML)
        return response

    def post(self, request):
        number = request.POST.get("number")
        num_type = request.POST.get("num_type")
        Telephone.objects.create(number=number, type=num_type)
        return HttpResponseRedirect('/new_person')


class AddEmail(View):
    def get(self, request):
        response = HttpResponse()
        response.write("Add New Email")
        return response