from django import forms

class USPhoneNumberMultiWidget(forms.MultiWidget):
    """
    A Widget that splits US Phone number input into three <input type='text'> boxes.
    """
    def __init__(self,attrs=None):
        widgets = (
            forms.TextInput(attrs={'size':'3','maxlength':'3', 'class':'phone'}),
            forms.TextInput(attrs={'size':'3','maxlength':'3', 'class':'phone'}),
            forms.TextInput(attrs={'size':'4','maxlength':'4', 'class':'phone'}),
        )
        super(USPhoneNumberMultiWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value.split('-')
        return (None,None,None)

    def value_from_datadict(self, data, files, name):
        value = [u'',u'',u'']
        # look for keys like name_1, get the index from the end
        # and make a new list for the string replacement values
        for d in filter(lambda x: x.startswith(name), data):
            index = int(d[len(name)+1:]) 
            value[index] = data[d]
        if value[0] == value[1] == value[2] == u'':
            return None
        return u'%s-%s-%s' % tuple(value)
