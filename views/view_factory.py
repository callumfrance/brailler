"""
This class determines what 
"""
# import views.view_cli as view_cli
# import views.view_braille as view_braille

from views.view_cli import ViewCLI
from views.view_braille import ViewBraille

view_types = ['CLIView', 'BrailleView',]


class ViewFactory:


    def make_view(self, view_type='CLIView'):
        view = None
        if view_type == view_types[0]:
            view = ViewCLI()
        elif view_type == view_types[1]:
            view = ViewBraille()

        return(view)


if __name__ == '__main__':
    from view_cli import ViewCLI
    from view_braille import ViewBraille

    v = ViewFactory()

    c = v.make_view('CLIView')
    b = v.make_view('BrailleView')

    print(c)
    print(b)
