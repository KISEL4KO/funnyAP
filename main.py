import flet as ft
from parser import request

def main(page:ft.Page):
    page.title = 'Main'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    mainText = ft.Text(value='Enter number',color='blue',size=25,italic=True, weight=ft.FontWeight.BOLD)
    txt_number = ft.TextField(value='1',text_align=ft.TextAlign.RIGHT,width=100)

    page.add(
        ft.Row(
            [
                mainText
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )






    def button(e):
        el = request(txt_number.value)
        text = ft.Text(value=el,color='blue',size=25,italic=True, weight=ft.FontWeight.BOLD)
        page.add(
            ft.Row(
                [
                    text
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        )
        page.update()





    page.add(
        ft.Row(
            [
                txt_number,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    ft.Row(
        [
            ft.FilledButton(text="Click me", on_click=button),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    )

ft.app(target=main)

