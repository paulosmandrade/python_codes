from flet import *
from utils.colors import *


class ForgotPassword(Container):
    def __init__(self, page:Page):
        super().__init__()
        self.expand = True
        self.bgcolor = blue
        self.alignment = alignment.center

        # Container para criar text email
        self.email_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding =padding.only(
                    top=0,bottom=0,right=20,left=20),
                hint_style=TextStyle(
                    size=12, color="#858796"
                ),
                hint_text= 'Digite seu email...',
                cursor_color='#858796',
                text_style=TextStyle(
                    size=14,
                    color='black',
                )

            ),
            border=border.all(width=1, color='#bdcdf4'),
            border_radius=30
        )

        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(
                    width=500,
                    border_radius=12,
                    padding=40,
                    bgcolor='white',
                    content=Column(
                        alignment='center',
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                value = "Esqueceu sua senha?",
                                size =20,
                                color='black',
                                text_align='center'
                            ),
                            Text(
                                value='Clique no botão para você receber uma nova senha no seu email.',
                                size=16,
                                color='#858796',
                                text_align='center'
                            ),
                            Container(height=0),
                            self.email_box,

                            Container(
                                alignment=alignment.center,
                                bgcolor='#4e73df',
                                height=40,
                                border_radius=30,
                                content=Text(
                                    value='Enviar email'
                                ),
                                on_click=self.reset_password
                            ),
                            Container(height=10),

                            Container(
                                content=Text(
                                    value='Criar Conta!',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: self.page.go('/signup')
                            ),
                            Container(
                                content=Text(
                                    value='Voltar para login!',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: self.page.go('/login')
                            )
                        ]
                    )

                )
            ]
        )

    def reset_password(self, e):
        pass