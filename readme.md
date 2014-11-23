##Python Library for [Open Duka platform](http://www.openduka.org/)

###Usage

```
$ git clone https://github.com/bmwasaru/pyopenduka.git 

cd pyopenduka

python setup.py install 

```

#### From python interpret

Obtain [Sign Up](http://www.openduka.org/index.php/api/) for an API key. e.g d3@1shturuhe9009090 as API key and seach term 'kenya power'

```
>> import pyopenduka

>> pyopenduka.get('d3@1shturuhe9009090', 'kenya power')
[{u'ID': u'1968', u'Name': u'Joseph Njoroge; Managing Director, Kenya Power And Lighting Company'}, {u'ID': u'1969', u'Name': u'Eng. Kaburu Mwarichia; Managing Director, Kenya Power And Lighting Company'}, {u'ID': u'1972', u'Name': u'Eng. David Mwangi; Chief Corporate Planning Manager,kenya Power And Lighting Company'}, {u'ID': u'4954', u'Name': u'Kenya Power & Lighting'}, {u'ID': u'11066', u'Name': u'Kenya Power And Lighting Co. Ltd'}, {u'ID': u'11086', u'Name': u'Kenya Power'}, {u'ID': u'12735', u'Name': u'Kenya Power And Lighting Company Limited'}]

```

