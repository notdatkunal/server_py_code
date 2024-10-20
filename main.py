from fasthtml.common import *

app,rt = fast_app()

@dataclass
class Link:
    title:str
    link:str

my_list :list[Link]= [
    Link(title='instagram',link='https://www.instagram.com/notdatkunal')
    ,Link(title='X',link='https://www.X.com/notdatkunal')
    ,Link(title='github',link='https://www.github.com/notdatkunal')
    ,Link(title='youtube',link='https://www.youtube.com/notdatkunal')

]

@rt('/links')
def get():
    head = Ul(
        *[
            Li(A(item.title.capitalize(),href=item.link,target_id='_blank')) for item in my_list
        ]

    )

    return Div(head,Titled(P(f'this is links page')),A('go back',href='/'))


@rt('/')
def get():
    return Div(P(f'Welcome to my application'),A('go to nice page',href='/links'), hx_get="/change")

serve(port=8000)