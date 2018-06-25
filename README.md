# Sample Appliction to integrate with salesforce

Salesforce is a cloud-based CRM that can turbo-charge your business relationships and
transform the working lives of your team

Simple Salesforce is a basic Salesforce.com REST API client built for Python 2.6, 2.7,
3.3, 3.4, 3.5 and 3.6. The goal is to provide a very low-level interface to the REST
Resource and APEX API, returning a dictionary of the API JSON response.
SOQL queries to  perform CRUD operations

# To create a new 'Contact' in Salesforce:
sf.Contact.create({‘LastName’:’Smith’, ‘Email’:’example@example.com’})

# To get a dictionary with all the information regarding that record, use:
sf.Contact.get_by_custom_id('My_Custom_ID__c', '22')

# To change that contact's last name from 'Smith' to 'Jones' and add a first name of 'John' use:
sf.Contact.update('003e0000003GuNXAA0',{'LastName': 'Jones', 'FirstName': 'John'})

# To delete the contact:
sf.Contact.delete('003e0000003GuNXAA0')

It's also possible to write select queries in Salesforce Object Query Language (SOQL) and search
queries in Salesforce Object Search Language (SOSL).


SOSL queries are done via

# To retrieve basic metadata use:
sf.Contact.metadata()

# To retrieve a description of the object, use:
sf.Contact.describe()

These are the related queries to perform operations on object into the salesforce
You now have a functioning API using Django Rest framework Request and Response objects.
We have extended the API to be able to handle different format suffixes and have explored
how to POST data via the API.

