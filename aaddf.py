import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column, Image, OutlinedButton
from flet_core.control_event import ControlEvent
from icecream import ic


def main(page: ft.Page):
    page.title = 'Musinc'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = '#ffffff'
    page.window_width = 585
    page.window_height = 354
    page.window_resizable = False

    # Controls
    text_username: TextField = TextField(label='Username', text_align=ft.TextAlign.LEFT, width=173, height=44,
                                         text_size=16, border_color='#05575B')
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=173, height=44,
                                         password=True, text_size=16, border_color='#05575B')
    checkbox_signup: Checkbox = Checkbox(label='Remember me', value=False, height=25, width=140, fill_color='#05575B',
                                         check_color='#66A5AD')
    button_submit: ElevatedButton = ElevatedButton(text='Submit', width=95, disabled=True,
                                                   style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
                                                   bgcolor='#05575B', color='#66A5AD')
    login_heading: Text = Text("Login", size=35, color='#05575B', weight=ft.FontWeight.W_600, italic=False)
    logo_img: Image = Image(src="image.png", width=229, height=290, fit=ft.ImageFit.CONTAIN)
    back_button: OutlinedButton = OutlinedButton(text='Go Back', disabled=False,
                                                 style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5),
                                                                      color='#05575B'))

    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
        page.update()

    def close_banner(e):
        page.banner.open = False
        page.update()
    page.banner = ft.Banner(
        bgcolor='#05575B',
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color='#66A5AD', size=40),
        content=ft.Text(
            "Password/ Username incorect!", color='#ffffff'
        ),
        actions=[
            ft.TextButton("Close", on_click=close_banner, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5), color='#66A5AD')),
        ],
        )

        # content=ft.Text(
        #     "Password/ Username incorect!", color='#ffffff'
        # ),
        # actions=[
        #     ft.TextButton("Close", on_click=close_banner, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5), color='#66A5AD')),
        # ],
        # )

    def show_banner_click():
        page.banner.open = True
        page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                controls=[
                    Row(
                        controls=[logo_img,
                    Column([
                        ft.Container(
                            content=ft.Column(
                                controls=[ft.Container(content=login_heading, alignment=ft.alignment.center,
                                                       padding=ft.padding.only(bottom=12, top=12)),
                                          ft.Container(content=text_username, alignment=ft.alignment.center),
                                          ft.Container(content=text_password, alignment=ft.alignment.center),
                                          ft.Container(content=checkbox_signup,
                                                       alignment=ft.alignment.bottom_left,
                                                       padding=ft.padding.only(left=12)),
                                          ft.Container(content=button_submit, alignment=ft.alignment.bottom_right,
                                                       padding=ft.padding.only(right=14))]),
                            alignment=ft.alignment.top_center,
                            border_radius=10,
                            width=209,
                            height=276,
                            border=ft.border.all(1, '#05575B'),
                            shadow=ft.BoxShadow(
                                spread_radius=2,
                                blur_radius=5,
                                color=ft.colors.BLACK,
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            ))
                    ])
                        ], spacing=70,
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ], bgcolor='#66A5AD'
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def submit_check(e: ControlEvent):
        if text_password.value == 'abcd':
            page.go("/store")
        else:
            show_banner_click()


    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    checkbox_signup.on_change = validate
    text_password.on_change = validate
    text_username.on_change = validate
    button_submit.on_click = submit_check

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)