def HTMLDecorator(func):
    def func(mesg):
        print('<p>', end='')
        print(mesg, end='')
        print('</p>')
        return HTMLDecorator(mesg)
    return func

@HTMLDecorator
def getText(mesg):
    return mesg


mesg = input('Text your name: ')
getText(mesg)