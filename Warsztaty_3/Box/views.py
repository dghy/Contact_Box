from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db import models
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from Box.models import *


# def try_db(table_name, id):
#     try:
#         table_row = table_name.objects.get(pk=id)
#         return table_row
#     except ObjectDoesNotExist:
#         table_row = None
#         return table_row


class ShowAll(View):
    def get(self, request):
        response = HttpResponse()
        response.write("<h1>Contact list..</h1>")
        persons = Person.objects.all()
        response.write('<ol>')
        for person in persons:
            mod_button = """<form action="/modify_person/{}"
                            style="display:inline;>
                                   margin: 0; 
                                   padding: 0;">
                                <input type="submit" value="Modify Person Data" />
                            </form>""".format(person.id)

            del_button = """<form action="/delete_person/{}"
                            style="display:inline;
                                   margin: 0; 
                                   padding: 0;">
                                <input type="submit" value="Delete Person" />
                            </form>""".format(person.id)

            response.write('<li><a href="/show_person/{}">{} {}</a> {} {}</li><br>'.format(person.id,
                                                                                           person.first_name,
                                                                                           person.last_name,
                                                                                           mod_button,
                                                                                           del_button))
        response.write('</ol><br>')
        new_button = """<form action="/new_person">
                            <input type="submit" value="Add New Person" />
                        </form>"""

        response.write(new_button)
        return response


class NewPerson(View):
    HTML = """
            <html>
                <h2>You are adding new person!</h2>                   
                <form method="post" action="" id="new_form">
                    <label><u>First Name</u></label><br>
                    <input name="first_name" type="text" maxlength="255" value=""/><br>
                    <label><u>Last Name</u></label><br>
                    <input name="last_name" type="text" maxlength="255" value=""/><br>                         
                   
                    <h4><u>Address</u></h4>
                    <label>City:</label>
                    <input name="city" type="text" maxlength="255" value=""/><br>
                    <label>Street:</label>
                    <input name="street" type="text" maxlength="255" value=""/><br>
                    <label>House Number:</label>
                    <input name="h_number" type="number" min=1  value="1"/><br>
                    <label>Door Number:</label>
                    <input name="d_number" type="number" min=1  value="1"/><br>                                                                
                    
                    <h4><u>Telephone</u></h4>
                    <label>Telephone Number:</label><br>
                    <input name="tel_number" type="number" min=1 step="1"  value="11111111"/><br>
                    <label>Telephone Type:</label><br>
                    <select name = "tel_type">
                        <option value="1">Home Number</option>
                        <option value="2">Work Number</option>
                    </select>                                                                
                                       
                    <h4><u>E-mail</u></h4>
                    <label>E-mail:</label><br> 
                    <input name="email" type="text" maxlength="255" value=""/><br>
                    <label>E-mail Type:</label><br> 
                    <select name="email_type" value="">
                        <option value="1">Home Email</option>
                        <option value="2">Work Email</option>
                    </select>
                </form>                
                <h5>Write description of person here:</h5>                    
                <textarea rows="4" cols="50" name="description" form="new_form">
                Enter description here..
                </textarea><br>
                <button type="submit" name="submit" value="name"
                 form="new_form">Add!</button>   
            </html>"""

    def get(self, request):
        response = HttpResponse()
        response.write(self.HTML)
        return response

    def post(self, request):
        address = Address.objects.create(city=request.POST.get('city'),
                                         street=request.POST.get('street'),
                                         house_number=int(request.POST.get('h_number')),
                                         door_number=int(request.POST.get('d_number')))

        telephone = Telephone.objects.create(number=int(request.POST.get('tel_number')),
                                             type=int(request.POST.get('tel_type')))

        email = Email.objects.create(email=request.POST.get('email'),
                                     type=request.POST.get('email_type'))

        Person.objects.create(first_name=request.POST.get('first_name'),
                              last_name=request.POST.get('last_name'),
                              address=address, telephone=telephone, e_mail=email,
                              description=request.POST.get('description'))
        return HttpResponseRedirect("/")


class ShowPerson(View):
    def get(self, request, id):
        response = HttpResponse()
        person = Person.objects.get(pk=id)
        table = """
                <table border="1">  
                    <tr>
                        <th colspan ="2">{} {}</th>
                    </tr>
                    <tr>
                        <th>Address</th>
                        <td>{} {} {} {}</td>
                    </tr>
                    <tr>
                        <th>Telephone</th>
                        <td>{} {}</td>
                    </tr>
                    <tr>
                        <th>Email</th>
                        <td>{} {}</td>
                    </tr>
                    <tr>
                        <th>Description</th>
                        <td>{}</td>
                    </tr> 
                </table>
                """.format(person.first_name, person.last_name,
                           person.address.city, person.address.street,
                           person.address.house_number, person.address.door_number,
                           person.telephone.number, person.telephone.type,
                           person.e_mail.email, person.e_mail.type,
                           person.description)

        response.write(table)
        back_button = """<form action="/">                        
                            <input type="submit" value="Back.." />
                        </form>""".format(person.id)
        response.write(back_button)
        return response


class DeletePerson(View):
    def get(self, request, id):
        Person.objects.get(pk=id).delete()
        return HttpResponseRedirect('/')


class ModifyPerson(View):
    def get(self, request, id):
        response = HttpResponse()
        person = Person.objects.get(pk=id)
        address_button = """<form action="/{}/add_address/"
                                    style="display:inline;>
                                           margin: 0; 
                                           padding: 0;">
                                        <input type="submit" value="Change Address" />
                                    </form>""".format(person.id)
        telephone_button = """<form action="/{}/add_telephone/"
                                    style="display:inline;>
                                           margin: 0; 
                                           padding: 0;">
                                        <input type="submit" value="Change Telephone" />
                                    </form>""".format(person.id)

        email_button = """<form action="/{}/add_email/"
                                    style="display:inline;>
                                           margin: 0; 
                                           padding: 0;">
                                        <input type="submit" value="Change Email" />
                                    </form>""".format(person.id)

        HTML = """
                        <html>
                            <h2>You are editing {} {}! </h2>                   
                            <form method="post" action="" id="new_form">
                                <label><u>First Name</u></label><br>
                                <input name="first_name" type="text" maxlength="255" value="{}"/><br>
                                <label><u>Last Name</u></label><br>
                                <input name="last_name" type="text" maxlength="255" value="{}"/><br>                         
                            </form>
                            {}
                            {}   
                            {}
                            <h5>Write description of person here:</h5>                    
                            <textarea rows="4" cols="50" name="description" form="new_form">
{}
                            </textarea><br>
                            <button type="submit" name="submit" value="name"
                             form="new_form">Change!</button>   
                        </html>""".format(person.first_name,person.last_name,
                                          person.first_name, person.last_name,
                                          address_button,
                                          telephone_button,
                                          email_button,
                                          person.description)
        response.write(HTML)
        return response

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        person.first_name = request.POST.get('first_name')
        person.last_name = request.POST.get('last_name')
        person.description = request.POST.get('description')
        person.save()
        return HttpResponseRedirect("/")


class AddAddress(View):
    back_button = """<form action="/modify_person/{}">                        
                         <input type="submit" value="Back.." />
                     </form>"""
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

                    <button type="submit" name="submit" value="name" form="new_form">
                    Add Address!</button>   
                </form>
                {}
             """

    def get(self, request, id):
        response = HttpResponse()
        back_button = self.back_button.format(id)
        response.write(self.HTML.format(back_button))
        return response

    def post(self, request, id):
        city = request.POST.get("city")
        street = request.POST.get("street")
        h_number = request.POST.get("h_number")
        d_number = request.POST.get("d_number")
        address = Address.objects.create(city=city, street=street, house_number=h_number,
                               door_number=d_number)
        person = Person.objects.get(pk=id)
        person.address = address
        person.save()
        return HttpResponseRedirect('/modify_person/{}'.format(id))


class AddTelephone(View):
    back_button = """<form action="/modify_person/{}">                        
                         <input type="submit" value="Back.." />
                     </form>"""
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
                       <button type="submit" name="submit" value="telephone" form="new_form">
                       Add Number!</button>   
                   </form>
                   {}
                """


    def get(self, request, id):
        response = HttpResponse()
        back_button = self.back_button.format(id)
        response.write(self.HTML.format(back_button))
        return response

    def post(self, request, id):
        number = request.POST.get("number")
        num_type = request.POST.get("num_type")
        person = Person.objects.get(pk=id)
        telephone = Telephone.objects.create(number=number, type=num_type)
        person.telephone = telephone
        person.save()
        return HttpResponseRedirect('/modify_person/{}'.format(id))


class AddEmail(View):
    back_button = """<form action="/modify_person/{}">                        
                             <input type="submit" value="Back.." />
                         </form>"""

    HTML = """
               <h2>You are adding new email! </h2>
                   <form method="post" action="" id="new_form">
                       <label>Email:</label><br>
                       <input name="email" type="text" maxlength="255" value=""/><br>
                       <label>Type of telephone:</label><br>
                       <select name = "email_type">
                           <option value="1">Home Email</option>
                           <option value="2">Work Email</option>
                       </select>
                       <button type="submit" name="submit" value="email" form="new_form">
                       Add Email!</button>   
                   </form>
                   {}
                """

    def get(self, request, id):
        response = HttpResponse()
        back_button = self.back_button.format(id)
        response.write(self.HTML.format(back_button))

        return response

    def post(self, request, id):
        email = request.POST.get("email")
        email_type = request.POST.get("email_type")
        person = Person.objects.get(pk=id)
        email = Email.objects.create(email=email, type=email_type)
        person.e_mail = email
        person.save()
        return HttpResponseRedirect('/modify_person/{}'.format(id))
