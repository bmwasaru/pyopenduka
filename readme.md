##Unofficial Python Library for [Open Duka platform](http://www.openduka.org/)

###Usage

```
$ git clone https://github.com/bmwasaru/pyopenduka.git 

$ cd pyopenduka

$ python setup.py install 

```

#### From the python interpreter

Obtain [Sign Up](http://www.openduka.org/index.php/api/) for an API key.

e.g d3@1shturuhe9009090 as API key and seach term 'kenya power'

```
>> from openduka import OpendukaClient
 
>> entities = OpendukaClient('d3@1shturuhe9009090') 

>> entities.name('kenya power') # get by name
[{u'ID': u'1968', u'Name': u'Joseph Njoroge; Managing Director, Kenya Power And Lighting Company'}, {u'ID': u'1969', u'Name': u'Eng. Kaburu Mwarichia; Managing Director, Kenya Power And Lighting Company'}, {u'ID': u'1972', u'Name': u'Eng. David Mwangi; Chief Corporate Planning Manager,kenya Power And Lighting Company'}, {u'ID': u'4954', u'Name': u'Kenya Power & Lighting'}, {u'ID': u'11066', u'Name': u'Kenya Power And Lighting Co. Ltd'}, {u'ID': u'11086', u'Name': u'Kenya Power'}, {u'ID': u'12735', u'Name': u'Kenya Power And Lighting Company Limited'}]

>> entities.id(120) # get by ID
{u'data': [{u'dataset_type': [{u'Gazette': [{u'dataset': [{u'Name_E_': u'0,120,', u'Name': u'Betty Chepkemoi Koech (ms.)', u'EffectiveDate': u'1/01/2012 : ', u'Appointer': u'Willy Mutunga: Chief Justice/president, Supreme Court Of Kenya.', u'Name2': u'Children`s Court', u'Action': u'appointed', u'Name2_E_': u'0,121,', u'Gazette_Number': u'2011_GAZ'}, {u'Name_E_': u'0,1120,', u'Name': u'Anthony Matende Itui', u'EffectiveDate': u'01/07/2009 : 2012', u'Appointer': u'James Orengo: Minister For Lands', u'Name2': u'Valuers Registration Board', u'Action': u'appointed', u'Name2_E_': u'0,1119,', u'Gazette_Number': u'2010_GAZ3481'},...

```

