# Source: https://www.youtube.com/watch?v=ptzRQ5CCjJ4
# (Basic Animation Tutorial in Flet Using Python )


import flet as ft
from time import sleep


def main(page: ft.Page):
    page.title = 'Flet Animated Icons'

    page.window.width = 300
    page.window.height = 620

    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    _main_row = ft.Container(
        expand=True,
        # bgcolor=ft.colors.PINK_600,
        # border_radius=25,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.START,
            controls=[
            ],
        ),
    )

    _icons_list = [
        ft.icons.DISCORD_ROUNDED,
        ft.icons.PERSON_ADD,
        ft.icons.SEARCH_ROUNDED,
        ft.icons.FAVORITE_ROUNDED,
        ft.icons.NOTIFICATION_ADD_ROUNDED,
    ]

    def _animate_hover(e):
        if e.data == 'true':
            if e.control.scale == ft.transform.Scale(1):
                e.control.scale = ft.transform.Scale(0.85)
                e.control.content.style.color = "white"

                e.control.update()
            else:
                e.control.scale = 1

                e.control.update()
        else:
            e.control.scale = ft.transform.Scale(1)

            e.control.update()

    def _animate_click(e):
        e.control.scale = ft.transform.Scale(0.75)
        e.control.update()
        sleep(0.15)
        e.control.scale = ft.transform.Scale(1)
        e.control.update()

        for control in _main_row.content.controls:
            control.content.selected = False
            control.content.style.color = "white70"

            control.update()

            if e.control.selected is not True:
                control.content.selected = True
                e.control.style.color = "white"

                e.control.update()

    for icon in _icons_list:
        _main_row.content.controls.append(
            ft.Container(

                # The 1st animation in video: hover
                # Enable bottom line if you wan't animate hover
                # on_hover=lambda e: _animate_hover(e),

                content=ft.IconButton(

                    icon=icon,
                    icon_size=22,

                    # https://github.com/flet-dev/flet/discussions/4061
                    animate_scale=ft.animation.Animation(
                        duration=250,
                        curve=ft.AnimationCurve.BOUNCE_OUT
                    ),

                    style=ft.ButtonStyle(
                        color={"": "white70"}),

                    selected=False,

                    # Disable this if you wan't animate hover on line 74
                    on_click=lambda e: _animate_click(e),

                )
            )
        )

    _main_container = ft.Container(
        width=280,
        height=590,
        bgcolor='black',
        alignment=ft.alignment.bottom_center,
        border_radius=35,
        padding=20,

        content=_main_row
    )

    page.add(_main_container)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
